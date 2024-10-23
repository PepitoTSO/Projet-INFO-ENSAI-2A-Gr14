from utils.singleton import Singleton  # Importing the Singleton metaclass
from DAO.db_connection import DBConnection
from Object.playlist import Playlist
from src.View.session import Session
from src.DAO.utilisateur_DAO import Utilisateur_DAO
from src.DAO.son_DAO import Son_DAO
from src.Object.son import Son


class Playlist_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Playlist operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def ajouter_playlist(self, nom_playlist) -> int:
        id_utilisateur = Session().utilisateur.id

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Playlist (id_utilisateur, nom_playlist) "
                    "VALUES (%(id_utilisateur)s, %(nom_playlist)s) RETURNING id_playlist;",
                    {"id_utilisateur": id_utilisateur, "nom_playlist": nom_playlist},
                )
                res = cursor.fetchone()

        if res:
            return res['id_playlist']  # Retourner l'ID de la nouvelle playlist

        return None  # Retourner None si l'insertion a échoué

    def get_playlist_by_id(self, id_playlist: int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM playlist WHERE id_playlist = %(id)s",
                    {"id": id_playlist},
                )

                res = cursor.fetchone()
        if res:
            user = Utilisateur_DAO.get_utilisateur(self, res["id_user"])
            liste_son = Son_DAO().get_son_ordre_by_playlist(id_playlist)

            playlist = Playlist(
                utilisateur=user,
                id_playlist=id_playlist,
                nom_playlist=res["nom_playlist"],
                list_son=liste_son,
            )
        return playlist

    def get_all_playlists_by_user(self, id_user: int):
        playlists = []
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM playlist WHERE id_utilisateur = %(id_user)s",
                    {"id_user": id_user},
                )

                res = cursor.fetchall()

        if res:
            user = Utilisateur_DAO.get_utilisateur(self, id_user)
            for playlist_data in res:
                liste_son = Son_DAO().get_son_ordre_by_playlist(
                    playlist_data["id_playlist"]
                )
                playlist = Playlist(
                    utilisateur=user,
                    id_playlist=playlist_data["id_playlist"],
                    nom_playlist=playlist_data["nom_playlist"],
                    list_son=liste_son,
                )
                playlists.append(playlist)
        return playlists

    def supprimer_playlist(self, id_playlist):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM son WHERE id_playlist = %(id_playlist)s",
                    {"id_playlist": id_playlist},
                )

                cursor.execute(
                    "DELETE FROM playlist WHERE id_playlist = %(id_playlist)s",
                    {"id_playlist": id_playlist},
                )

            connection.commit()

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
                        {"id_playlist": id_playlist, "ordre": ordre}
                    )
                else:
                    # Decrement order of songs with order > ordre
                    cursor.execute(
                        "UPDATE son SET ordre_son_in_plist = ordre_son_in_plist - 1 "
                        "WHERE id_playlist = %(id_playlist)s AND ordre_son_in_plist > %(ordre)s",
                        {"id_playlist": id_playlist, "ordre": ordre}
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
                    {"id_playlist": id_playlist}
                )
                original_playlist = cursor.fetchone()

                if not original_playlist:
                    return False  # Si la playlist originale n'existe pas

                # Créer une nouvelle playlist avec le même nom pour l'utilisateur de session
                new_id_playlist = self.ajouter_playlist(original_playlist['nom_playlist'])

                if not new_id_playlist:
                    return False  # Si la création de la nouvelle playlist a échoué

                # Copier les chansons de la playlist originale dans la nouvelle playlist
                cursor.execute(
                    "SELECT nom, ordre_son_in_plist, tags, path_stockage FROM Son WHERE id_playlist = %(id_playlist)s;",
                    {"id_playlist": id_playlist}
                )
                chansons = cursor.fetchall()

                for chanson in chansons:
                    cursor.execute(
                        "INSERT INTO Son (id_playlist, nom, ordre_son_in_plist, tags, path_stockage) "
                        "VALUES (%(id_playlist)s, %(nom)s, %(ordre)s, %(tags)s, %(path)s);",
                        {
                            "id_playlist": new_id_playlist,
                            "nom": chanson['nom'],
                            "ordre": chanson['ordre_son_in_plist'],
                            "tags": chanson['tags'],
                            "path": chanson['path_stockage']
                        }
                    )

            connection.commit()
            return True  # Retourner True si la copie a réussi
