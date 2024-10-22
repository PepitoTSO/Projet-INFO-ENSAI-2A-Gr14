from typing import List, Dict, Any
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

    def ajouter_playlist(self, nom_playlist) -> bool:
        id_utilisateur = Session().utilisateur.id

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    " INSERT INTO Playlist (id_utilisateur, nom)"
                    "VALUES (%(id_utilisateur)s, %(nom_playlist)s);",
                    {"id_utilisateur": id_utilisateur, "nom_playlist": nom_playlist},
                )
            res = cursor.fetchone()

        if res:
            return True

        return False

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

    def modifier_playlist(self, id_modif: Dict[str, Any]) -> bool:
        try:
            cursor = self.db_connection.cursor()
            id_playlist = id_modif.get("id_playlist")
            if not id_playlist:
                print("Playlist ID is required for modification.")
                return False

            fields_to_update = id_modif.copy()
            fields_to_update.pop("id_playlist", None)
            if not fields_to_update:
                print("No fields to update.")
                return False

            update_fields = ", ".join(
                [f"{key} = %s" for key in fields_to_update.keys()]
            )
            update_values = list(fields_to_update.values())
            update_values.append(id_playlist)
            update_query = (
                f"UPDATE playlists SET {update_fields} WHERE id_playlist = %s"
            )

            cursor.execute(update_query, update_values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error modifying playlist: {e}")
            return False

    def supprimer_playlist(self, id_playlist: int) -> bool:
        try:
            cursor = self.db_connection.cursor()
            # Delete songs associated with the playlist
            delete_songs_query = "DELETE FROM playlist_songs WHERE id_playlist = %s"
            cursor.execute(delete_songs_query, (id_playlist,))
            # Delete the playlist itself
            delete_playlist_query = "DELETE FROM playlists WHERE id_playlist = %s"
            cursor.execute(delete_playlist_query, (id_playlist,))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error deleting playlist: {e}")
            return False
