from utils.singleton import Singleton
from DAO.db_connection import DBConnection
from Object.playlist import Playlist
from Object.utilisateur import Utilisateur
from DAO.utilisateur_DAO import Utilisateur_DAO
from DAO.son_DAO import Son_DAO
from Object.son import Son
import logging
from utils.log_decorator import log
import psycopg2
import psycopg2.extras


class Playlist_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Playlist operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def ajouter_playlist(self, playlist: Playlist) -> bool:
        """
        Ajoute une nouvelle playlist et ses sons à la base de données.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor(
                    cursor_factory=psycopg2.extras.RealDictCursor
                ) as cursor:
                    # Insert playlist without specifying id_playlist, since it's auto-generated
                    cursor.execute(
                        """
                        INSERT INTO bdd.playlist (pseudo, nom_playlist)
                        VALUES (%s, %s)
                        RETURNING id_playlist;
                        """,
                        (
                            playlist.utilisateur.pseudo,
                            playlist.nom_playlist,
                        ),
                    )
                    # Fetch the generated id_playlist
                    res = cursor.fetchone()

                    if res:
                        generated_id_playlist = res[
                            "id_playlist"
                        ]  # Get the generated id_playlist
                        # Insert associated sons into the playlist_son_join table
                        for son, ordre in playlist.list_son:
                            cursor.execute(
                                """
                                INSERT INTO bdd.playlist_son_join (id_playlist, id_son, ordre_son_playlist)
                                VALUES (%s, %s, %s);
                                """,
                                (
                                    generated_id_playlist,
                                    son.id_son,
                                    ordre,
                                ),
                            )
                        return True
        except Exception as e:
            print(f"Error adding playlist: {e.__class__.__name__}: {e}")
            return False

        return False  # Retourner False si l'insertion a échoué

    def get_sons_by_playlist(self, playlist: Playlist) -> list[Son]:
        """
        Récupère tous les sons de la playlist spécifiée par id_playlist
        ainsi que leur ordre dans la playlist.
        """
        id_playlist = playlist.id_playlist
        sons = []
        with DBConnection().connection as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:
                cursor.execute(
                    """
                    SELECT s.id_son, s.nom_son, s.tags, s.path_stockage, psj.ordre_son_playlist
                    FROM bdd.son s
                    JOIN bdd.playlist_son_join psj ON s.id_son = psj.id_son
                    WHERE psj.id_playlist = %s;
                    """,
                    (id_playlist,),
                )
                res = cursor.fetchall()

        for son_data in res:
            son = Son(
                id_son=son_data["id_son"],
                nom=son_data["nom_son"],
                tags=[son_data["tags"]],
                path_stockage=son_data["path_stockage"],
            )
            sons.append([son, son_data["ordre_son_playlist"]])
        return sons

    def get_playlist_by_id_playlist(self, id_playlist: int):
        with DBConnection().connection as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:
                cursor.execute(
                    "SELECT * FROM bdd.playlist WHERE id_playlist = %s;",
                    (id_playlist,),
                )
                res = cursor.fetchone()

        if res:
            user = Utilisateur_DAO().get_utilisateur(res["pseudo"])
            liste_son = self.get_sons_by_id_playlist(id_playlist)
            playlist = Playlist(
                utilisateur=user,
                id_playlist=id_playlist,
                nom_playlist=res["nom_playlist"],
                list_son=liste_son,
            )
            return playlist

        return None  # Playlist n'est pas trouvé

    def get_all_playlists_by_user(self, utilisateur: Utilisateur):
        """
        Récupère toutes les playlists d'un utilisateur
        """
        playlists = []
        pseudo = utilisateur.pseudo
        with DBConnection().connection as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:
                cursor.execute(
                    "SELECT * FROM bdd.playlist WHERE pseudo = %s;",
                    (pseudo,),
                )
                res = cursor.fetchall()

        if res:
            for playlist_data in res:
                liste_son = self.get_sons_by_id_playlist(playlist_data["id_playlist"])
                playlist = Playlist(
                    utilisateur=utilisateur,
                    id_playlist=playlist_data["id_playlist"],
                    nom_playlist=playlist_data["nom_playlist"],
                    list_son=liste_son,
                )
                playlists.append(playlist)

        return playlists

    def supprimer_playlist(self, id_playlist: int) -> bool:
        """
        Supprime la playlist spécifiée par id_playlist ainsi que ses associations de sons.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer les associations des sons avec la playlist dans la table d'association
                    cursor.execute(
                        "DELETE FROM bdd.playlist_son_join WHERE id_playlist = %s;",
                        (id_playlist,),
                    )
                    # Supprimer la playlist elle-même
                    cursor.execute(
                        "DELETE FROM bdd.playlist WHERE id_playlist = %s;",
                        (id_playlist,),
                    )
            return True
        except Exception as e:
            print(f"Error deleting playlist: {e.__class__.__name__}: {e}")
            return False

    def modifier_nom_playlist(self, id_playlist: int, nouveau_nom: str) -> bool:
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE bdd.playlist SET nom_playlist = %s WHERE id_playlist = %s;",
                        (nouveau_nom, id_playlist),
                    )
            return True
        except Exception as e:
            print(f"Error updating playlist name: {e.__class__.__name__}: {e}")
            return False

    def changer_ordre(self, playlist: Playlist, son: Son, ordre: int) -> bool:
        """
        Modifie l'ordre des sons dans une playlist spécifiée.
        """
        try:
            playlist.changer_ordre(son, ordre)
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE bdd.playlist_son_join SET ordre_son_playlist = %s "
                        "WHERE id_playlist = %s AND id_son = %s;",
                        (
                            ordre,
                            playlist.id_playlist,
                            son.id_son,
                        ),
                    )

                    # Modifie l'ordre de tous les sons dans la playlist dans la table playlist.list_son.
                    for s, ordre in playlist.list_son:
                        cursor.execute(
                            "UPDATE bdd.playlist_son_join SET ordre_son_playlist = %s "
                            "WHERE id_playlist = %s AND id_son = %s;",
                            (
                                ordre,
                                playlist.id_playlist,
                                s.id_son,
                            ),
                        )
            return True
        except Exception as e:
            print(f"Error changing order: {e.__class__.__name__}: {e}")
            return False

    def supprimer_son(self, playlist: Playlist, son: Son) -> bool:
        """
        Supprime un son de la playlist spécifiée et ajuste l'ordre des autres sons.
        """
        try:
            playlist.supprimer_son(son)
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le son de la table `playlist_son_join`
                    cursor.execute(
                        "DELETE FROM bdd.playlist_son_join WHERE id_playlist = %s AND id_son = %s;",
                        (
                            playlist.id_playlist,
                            son.id_son,
                        ),
                    )

                    # Mettre à jour l'ordre dans la base de données
                    for s, ordre in playlist.list_son:
                        cursor.execute(
                            "UPDATE bdd.playlist_son_join SET ordre_son_playlist = %s "
                            "WHERE id_playlist = %s AND id_son = %s;",
                            (
                                ordre,
                                playlist.id_playlist,
                                s.id_son,
                            ),
                        )
            return True
        except Exception as e:
            print(f"Error deleting son: {e.__class__.__name__}: {e}")
            return False

    def ajouter_son(self, playlist: Playlist, son: Son, ordre: int) -> bool:
        pass
