from typing import List, Dict, Any
from utils.singleton import Singleton  # Importing the Singleton metaclass
from DAO.db_connection import DBConnection
from Object.playlist import Playlist
from src.View.session import Session
from src.DAO.utilisateur_DAO import Utilisateur_DAO
from src.DAO.son_DAO import Son_DAO


class Playlist_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Playlist operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def __init__(self):
        self.utilisateur = Session().utilisateur


    def ajouter_playlist(self, nom_playlist) -> bool:
        id_utilisateur = self.utilisateur.id

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(" INSERT INTO Playlist (id_utilisateur, nom)"
                                "VALUES (%(id_utilisateur)s, %(nom_playlist)s);",
                                {"id_utilisateur" : id_utilisateur, "nom_playlist" : nom_playlist})
            res = cursor.fetchone()

        if res:
            return True

        return False


    def get_playlist_by_id(self, id_playlist: int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM playlists WHERE id_playlist = %(id)s",
                    {"id": id_playlist})

                res = cursor.fetchone()
        if res:
            user = Utilisateur_DAO.get_utilisateur(self, res["id_user"])
            liste_son = Son_DAO().get_son_ordre_by_playlist(id_playlist)

            playlist = Playlist(
                utilisateur =  user,
                id_playlist= id_playlist,
                nom_playlist= res["nom_playlist"],
                list_son= liste_son,
                )
        return playlist

    def get_all_playlists(self) -> List:
        try:
            cursor = self.db_connection.cursor()
            select_all_playlists_query = """
                SELECT id_playlist, id_user, nom_playlist FROM playlists
            """
            cursor.execute(select_all_playlists_query)
            playlists = []
            for row in cursor.fetchall():
                id_playlist = row["id_playlist"]
                id_user = row["id_user"]
                nom_playlist = row["nom_playlist"]

                # Now get the songs for each playlist
                select_songs_query = """
                    SELECT song_name, song_order FROM playlist_songs
                    WHERE id_playlist = %s ORDER BY song_order
                """
                cursor.execute(select_songs_query, (id_playlist,))
                songs = [
                    {"name": song["song_name"], "order": song["song_order"]}
                    for song in cursor.fetchall()
                ]

                # Assuming you have the Playlist class imported
                playlist = Playlist(
                    id_user=id_user,
                    id_playlist=id_playlist,
                    nom_playlist=nom_playlist,
                    dict_son=songs,
                )
                playlists.append(playlist)
            cursor.close()
            return playlists
        except Exception as e:
            print(f"Error retrieving all playlists: {e}")
            return []

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
