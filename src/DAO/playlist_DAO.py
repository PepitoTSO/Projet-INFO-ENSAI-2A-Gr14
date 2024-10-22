from typing import List, Dict, Any
from utils.singleton import Singleton  # Importing the Singleton metaclass
from DAO.db_connection import DBConnection
from Object.playlist import Playlist


class Playlist_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Playlist operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def ajouter_playlist(self, playlist) -> bool:
        try:
            cursor = self.db_connection.cursor()
            # Insert into the playlists table
            insert_playlist_query = """
                INSERT INTO playlists (id_user, nom_playlist)
                VALUES (%s, %s)
                RETURNING id_playlist
            """
            cursor.execute(
                insert_playlist_query, (playlist.id_user, playlist.nom_playlist)
            )
            playlist_id = cursor.fetchone()[
                "id_playlist"
            ]  # Get the ID of the inserted playlist

            # Now insert the songs into the playlist_songs table
            for song in playlist.dict_son:
                song_name = song["name"]
                song_order = song["order"]
                insert_song_query = """
                    INSERT INTO playlist_songs (id_playlist, song_name, song_order)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(insert_song_query, (playlist_id, song_name, song_order))

            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error adding playlist: {e}")
            return False

    def get_playlist(self, id_playlist: int):
        try:
            cursor = self.db_connection.cursor()
            select_playlist_query = """
                SELECT id_user, nom_playlist FROM playlists WHERE id_playlist = %s
            """
            cursor.execute(select_playlist_query, (id_playlist,))
            row = cursor.fetchone()
            if row:
                id_user = row["id_user"]
                nom_playlist = row["nom_playlist"]

                # Now get the songs
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
                cursor.close()
                return playlist
            else:
                cursor.close()
                return None
        except Exception as e:
            print(f"Error retrieving playlist: {e}")
            return None

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
