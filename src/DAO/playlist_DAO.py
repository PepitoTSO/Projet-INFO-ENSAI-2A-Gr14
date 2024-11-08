from utils.singleton import Singleton
from DAO.db_connection import DBConnection
from Object.playlist import Playlist
from Object.utilisateur import Utilisateur
from DAO.utilisateur_DAO import Utilisateur_DAO
from DAO.son_DAO import Son_DAO
from Object.son import Son
import logging
from utils.log_decorator import log


class Playlist_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Playlist operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def ajouter_playlist(self, playlist: Playlist) -> bool:
        """
        Ajoute une nouvelle playlist et ses sons à la base de données.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO bdd.playlist (id_playlist, pseudo, nom_playlist) "
                    "VALUES (%(id_playlist)s, %(pseudo)s, %(nom_playlist)s) "
                    "RETURNING id_playlist;",
                    {
                        "id_playlist": playlist.id_playlist,
                        "pseudo": playlist.utilisateur.pseudo,
                        "nom_playlist": playlist.nom_playlist,
                    },
                )
                res = cursor.fetchone()

                if res:
                    for son, ordre in playlist.list_son:
                        cursor.execute(
                            "INSERT INTO bdd.playlist_son_join (id_playlist, id_son, ordre_son_playlist) "
                            "VALUES (%(id_playlist)s, %(id_son)s, %(ordre)s);",
                            {
                                "id_playlist": playlist.id_playlist,
                                "id_son": son.id_son,
                                "ordre": ordre,
                            },
                        )
                    return True

        return False  # Retourner False si l'insertion a échoué

    def get_sons_by_id_playlist(self, id_playlist: int) -> list[list]:
        """
        Récupère tous les sons de la playlist spécifiée par id_playlist
        ainsi que leur ordre dans la playlist.
        """
        sons = []
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_son, nom_son, tags, path_stockage, ordre_son_playlist"
                    "FROM bdd.son JOIN bdd.playlist_son_join ON id_playlist                 "
                    "WHERE id_playlist = %(id_playlist)s;                           ",
                    {"id_playlist": id_playlist},
                )
                res = cursor.fetchall()

        for son_data in res:
            son = Son(
                id_son=son_data["id_son"],
                nom=son_data["nom_son"],
                tags=son_data["tags"],
                path_stockage=son_data["path_stockage"],
            )
            sons.append([son, son_data["ordre_son_playlist"]])
        return sons

    def get_playlist_by_id_playlist(self, id_playlist: int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM playlist WHERE id_playlist = %(id_playlist)s",
                    {"id_playlist": id_playlist},
                )

                res = cursor.fetchone()

        if res:
            user = Utilisateur_DAO().get_utilisateur(res["pseudo"])
            liste_son = Playlist_DAO().get_sons_by_id_playlist(id_playlist)
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
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM playlist WHERE pseudo = %(pseudo)s",
                    {"pseudo": pseudo},
                )
                res = cursor.fetchall()

        if res:
            for playlist_data in res:
                liste_son = Playlist_DAO().get_sons_by_id_playlist(
                    playlist_data["id_playlist"]
                )

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
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Supprimer les associations des sons avec la playlist dans la table d'association
                cursor.execute(
                    "DELETE FROM playlist_son_join WHERE id_playlist = %(id_playlist)s",
                    {"id_playlist": id_playlist},
                )

                # Supprimer la playlist elle-même
                cursor.execute(
                    "DELETE FROM playlist WHERE id_playlist = %(id_playlist)s",
                    {"id_playlist": id_playlist},
                )

        return True  # Retourner True si la suppression est réussie

    def modifier_nom_playlist(self, id_playlist, nouveau_nom):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE playlists ET nom_playlist = %(nouveau_nom)s WHERE id_playlist = %(id_playlist)s",
                    {"nouveau_nom": nouveau_nom, "id_playlist": id_playlist},
                )

    def changer_ordre(self, playlist: Playlist, son: Son, ordre: int):
        """
        Modifie l'ordre des sons dans une playlist spécifiée.
        """
        playlist.changer_ordre(son, ordre)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE playlist_son_join SET ordre_son_playlist = %(nouvel_ordre)s "
                    "WHERE id_playlist = %(id_playlist)s AND id_son = %(id_son)s",
                    {
                        "id_playlist": playlist.id_playlist,
                        "id_son": son.id_son,
                        "nouvel_ordre": ordre,
                    },
                )

                # Modifie l'ordre de tous les sons dans la playlist dans la table playlist.list_son.
                for s, ordre in playlist.list_son:
                    cursor.execute(
                        "UPDATE playlist_son_join SET ordre_son_playlist = %(ordre)s "
                        "WHERE id_playlist = %(id_playlist)s AND id_son = %(id_son)s",
                        {
                            "id_playlist": playlist.id_playlist,
                            "id_son": s.id_son,
                            "ordre": ordre,
                        },
                    )

        return True

    def supprimer_son(self, playlist: Playlist, son: Son):
        """
        Supprime un son de la playlist spécifiée et ajuste l'ordre des autres sons.
        """
        playlist.supprimer_son(son)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Supprimer le son de la table `playlist_son_join`
                cursor.execute(
                    "DELETE FROM playlist_son_join WHERE id_playlist = %(id_playlist)s AND id_son = %(id_son)s",
                    {
                        "id_playlist": playlist.id_playlist,
                        "id_son": son.id_son,
                    },
                )

                # Mettre à jour l'ordre dans la base de données
                for s, ordre in playlist.list_son:
                    cursor.execute(
                        "UPDATE playlist_son_join SET ordre_son_playlist = %(ordre)s "
                        "WHERE id_playlist = %(id_playlist)s AND id_son = %(id_son)s",
                        {
                            "id_playlist": playlist.id_playlist,
                            "id_son": s.id_son,
                            "ordre": ordre,
                        },
                    )
        return True

    def ajouter_son(self, playlist: Playlist, son: Son, ordre: int):
        """
        Ajoute un son à une playlist spécifiée et ajuste l'ordre des autres sons.

        """
        playlist.ajouter_son_playlist(son, ordre)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Nouveau son dans la table
                cursor.execute(
                    "INSERT INTO playlist_son_join (id_playlist, id_son, ordre_son_playlist) "
                    "VALUES (%(id_playlist)s, %(id_son)s, %(ordre)s)",
                    {
                        "id_playlist": playlist.id_playlist,
                        "id_son": son.id_son,
                        "ordre": ordre,
                    },
                )

                # Mettre à jour l'ordre dans la base de données
                for s, ordre in playlist.list_son:
                    cursor.execute(
                        "UPDATE playlist_son_join SET ordre_son_playlist = %(ordre)s "
                        "WHERE id_playlist = %(id_playlist)s AND id_son = %(id_son)s",
                        {
                            "id_playlist": playlist.id_playlist,
                            "id_son": s.id_son,
                            "ordre": ordre,
                        },
                    )
        return True

    def copier_playlist(self, id_playlist: int, utilisateur: Utilisateur) -> bool:
        """
        Copie une playlist existante pour un utilisateur donné.

        Arguments:
        - id_playlist: L'identifiant de la playlist à copier.
        - utilisateur: L'utilisateur pour lequel la playlist est copiée.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Récupérer les détails de la playlist originale
                    cursor.execute(
                        "SELECT nom_playlist FROM playlist WHERE id_playlist = %(id_playlist)s;",
                        {"id_playlist": id_playlist},
                    )
                    original_playlist = cursor.fetchone()

                    if not original_playlist:
                        return False  # Si la playlist originale n'existe pas

                    # Créer une nouvelle playlist avec le même nom pour l'utilisateur donné
                    nouveau_nom_playlist = (
                        original_playlist["nom_playlist"] + " (copie)"
                    )
                    cursor.execute(
                        "INSERT INTO playlist (pseudo, nom_playlist) VALUES (%(pseudo)s, %(nom_playlist)s) RETURNING id_playlist;",
                        {
                            "pseudo": utilisateur.pseudo,
                            "nom_playlist": nouveau_nom_playlist,
                        },
                    )
                    new_id_playlist = cursor.fetchone()["id_playlist"]

                    # Si la création de la nouvelle playlist a échoué
                    if not new_id_playlist:
                        return False

                    # Récupérer les sons associés à la playlist originale
                    cursor.execute(
                        "SELECT id_son, ordre_son_playlist FROM playlist_son_join WHERE id_playlist = %(id_playlist)s;",
                        {"id_playlist": id_playlist},
                    )
                    sons = cursor.fetchall()

                    # Copier chaque son de l'ancienne playlist vers la nouvelle
                    for son in sons:
                        cursor.execute(
                            "INSERT INTO playlist_son_join (id_playlist, id_son, ordre_son_playlist) "
                            "VALUES (%(id_playlist)s, %(id_son)s, %(ordre)s);",
                            {
                                "id_playlist": new_id_playlist,
                                "id_son": son["id_son"],
                                "ordre": son["ordre_son_playlist"],
                            },
                        )
        except Exception as e:
            logging.info(e)

        return True  # Retourner True si la copie a réussi
