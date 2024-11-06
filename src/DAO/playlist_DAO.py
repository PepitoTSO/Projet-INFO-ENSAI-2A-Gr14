from utils.singleton import Singleton
from DAO.db_connection import DBConnection
from Object.playlist import Playlist
from Object.utilisateur import Utilisateur
from src.DAO.utilisateur_DAO import Utilisateur_DAO
from src.DAO.son_DAO import Son_DAO
from src.Object.son import Son


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
                # Insert the playlist into the playlist table
                cursor.execute(
                    "INSERT INTO playlist (id_playlist, pseudo, nom_playlist) "
                    "VALUES (%(id_playlist)s, %(pseudo)s, %(nom_playlist)s) "
                    "RETURNING id_playlist;",
                    {
                        "id_playlist": playlist.id_playlist,
                        "pseudo": playlist.pseudo,
                        "nom_playlist": playlist.nom_playlist,
                    },
                )
                res = cursor.fetchone()

                if res:
                    for son, ordre in playlist.list_son:
                        cursor.execute(
                            "INSERT INTO playlist_son_join (id_playlist, id_son, ordre_son_playlist) "
                            "VALUES (%(id_playlist)s, %(id_son)s, %(ordre)s);",
                            {
                                "id_playlist": playlist.id_playlist,
                                "id_son": son.id_son,
                                "ordre": ordre
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
                    "FROM son JOIN playlist_son_join ON id_playlist                 "
                    "WHERE id_playlist = %(id_playlist)s;                           ",
                        {"id_playlist": id_playlist}
                    )
                res = cursor.fetchall()

        for son_data in res:
            son = Son(
                id_son=son_data["id_son"],
                nom=son_data["nom_son"],
                tags=son_data["tags"],
                path_stockage=son_data["path_stockage"]
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
                liste_son = Playlist_DAO().get_sons_by_id_playlist(playlist_data["id_playlist"])

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
                    "UPDATE playlists SET nom_playlist = %(nouveau_nom)s WHERE id_playlist = %(id_playlist)s",
                    {"nouveau_nom": nouveau_nom, "id_playlist": id_playlist},
                )
            connection.commit()

    def changer_ordre(self, id_playlist: int, ordre: int, ajout: bool):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                if ajout:
                    # Increment order of songs with order >= ordre
                    cursor.execute(
                        "UPDATE son SET ordre_son_in_plist = ordre_son_in_plist + 1 "
                        "WHERE id_playlist = %(id_playlist)s AND ordre_son_in_plist >= %(ordre)s",
                        {"id_playlist": id_playlist, "ordre": ordre},
                    )
                else:
                    # Decrement order of songs with order > ordre
                    cursor.execute(
                        "UPDATE son SET ordre_son_in_plist = ordre_son_in_plist - 1 "
                        "WHERE id_playlist = %(id_playlist)s AND ordre_son_in_plist > %(ordre)s",
                        {"id_playlist": id_playlist, "ordre": ordre},
                    )
            connection.commit()

    def supprimer_son(self, id_playlist, son: Son):
        id_son = son.id
        Son_DAO().supprimer_son_by_playlist(id_playlist, id_son)

    def ajouter_son(id_playlist, son, ordre):
        id_son = son.id
        Son_DAO().ajouter_son(id_playlist, id_son, ordre)

    def copier_playlist(self, id_playlist: int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Récupérer les détails de la playlist originale
                cursor.execute(
                    "SELECT nom_playlist FROM Playlist WHERE id_playlist = %(id_playlist)s;",
                    {"id_playlist": id_playlist},
                )
                original_playlist = cursor.fetchone()

                if not original_playlist:
                    return False  # Si la playlist originale n'existe pas

                # Créer une nouvelle playlist avec le même nom pour l'utilisateur de session
                new_id_playlist = self.ajouter_playlist(
                    original_playlist["nom_playlist"]
                )

                if not new_id_playlist:
                    return False  # Si la création de la nouvelle playlist a échoué

                # Copier les chansons de la playlist originale dans la nouvelle playlist
                cursor.execute(
                    "SELECT nom, ordre_son_in_plist, tags, path_stockage FROM Son WHERE id_playlist = %(id_playlist)s;",
                    {"id_playlist": id_playlist},
                )
                chansons = cursor.fetchall()

                for chanson in chansons:
                    cursor.execute(
                        "INSERT INTO Son (id_playlist, nom, ordre_son_in_plist, tags, path_stockage) "
                        "VALUES (%(id_playlist)s, %(nom)s, %(ordre)s, %(tags)s, %(path)s);",
                        {
                            "id_playlist": new_id_playlist,
                            "nom": chanson["nom"],
                            "ordre": chanson["ordre_son_in_plist"],
                            "tags": chanson["tags"],
                            "path": chanson["path_stockage"],
                        },
                    )

            connection.commit()
            return True  # Retourner True si la copie a réussi
