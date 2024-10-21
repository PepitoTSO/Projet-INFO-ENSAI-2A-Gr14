from DAO.db_connection import DBConnection


class Playlist_DAO(metaclass=SingletonMeta):
    def __init__(self):
        self.db = DatabaseConnection.getInstance().get_connection()

    def ajouter_playlist(self, playlist: Playlist) -> bool:
        try:
            cursor = self.db.cursor()
            # Insert into the playlists table
            insert_playlist_query = (
                "INSERT INTO playlists (id_user, nom_playlist) VALUES (?, ?)"
            )
            cursor.execute(
                insert_playlist_query, (playlist.id_user, playlist.nom_playlist)
            )
            playlist_id = cursor.lastrowid  # Get the ID of the inserted playlist
            # Now insert the songs into the playlist_songs table
            for song in playlist.dict_son:
                song_name = song["name"]
                song_order = song["order"]
                insert_song_query = "INSERT INTO playlist_songs (id_playlist, song_name, song_order) VALUES (?, ?, ?)"
                cursor.execute(insert_song_query, (playlist_id, song_name, song_order))
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error adding playlist: {e}")
            return False

    def get_playlist(self, id_playlist: int) -> Playlist:
        try:
            cursor = self.db.cursor()
            select_playlist_query = (
                "SELECT id_user, nom_playlist FROM playlists WHERE id_playlist = ?"
            )
            cursor.execute(select_playlist_query, (id_playlist,))
            row = cursor.fetchone()
            if row:
                id_user, nom_playlist = row
                # Now get the songs
                select_songs_query = "SELECT song_name, song_order FROM playlist_songs WHERE id_playlist = ? ORDER BY song_order"
                cursor.execute(select_songs_query, (id_playlist,))
                songs = [
                    {"name": song_name, "order": song_order}
                    for song_name, song_order in cursor.fetchall()
                ]
                playlist = Playlist(
                    id_user=id_user,
                    id_playlist=id_playlist,
                    nom_playlist=nom_playlist,
                    dict_son=songs,
                )
                return playlist
            else:
                return None
        except Exception as e:
            print(f"Error retrieving playlist: {e}")
            return None

    def get_all_playlists(self) -> List[Playlist]:
        try:
            cursor = self.db.cursor()
            select_all_playlists_query = (
                "SELECT id_playlist, id_user, nom_playlist FROM playlists"
            )
            cursor.execute(select_all_playlists_query)
            playlists = []
            for id_playlist, id_user, nom_playlist in cursor.fetchall():
                # Now get the songs for each playlist
                select_songs_query = "SELECT song_name, song_order FROM playlist_songs WHERE id_playlist = ? ORDER BY song_order"
                cursor.execute(select_songs_query, (id_playlist,))
                songs = [
                    {"name": song_name, "order": song_order}
                    for song_name, song_order in cursor.fetchall()
                ]
                playlist = Playlist(
                    id_user=id_user,
                    id_playlist=id_playlist,
                    nom_playlist=nom_playlist,
                    dict_son=songs,
                )
                playlists.append(playlist)
            return playlists
        except Exception as e:
            print(f"Error retrieving all playlists: {e}")
            return []

    def modifier_playlist(self, id_modif: Dict[str, Any]) -> bool:
        try:
            cursor = self.db.cursor()
            id_playlist = id_modif.get("id_playlist")
            if not id_playlist:
                print("Playlist ID is required for modification.")
                return False
            fields_to_update = id_modif.copy()
            fields_to_update.pop("id_playlist", None)
            if not fields_to_update:
                print("No fields to update.")
                return False
            update_fields = ", ".join([f"{key} = ?" for key in fields_to_update.keys()])
            update_values = list(fields_to_update.values())
            update_values.append(id_playlist)
            update_query = f"UPDATE playlists SET {update_fields} WHERE id_playlist = ?"
            cursor.execute(update_query, update_values)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error modifying playlist: {e}")
            return False

    def supprimer_playlist(self, id_playlist: int) -> bool:
        try:
            cursor = self.db.cursor()
            # Delete songs associated with the playlist
            delete_songs_query = "DELETE FROM playlist_songs WHERE id_playlist = ?"
            cursor.execute(delete_songs_query, (id_playlist,))
            # Delete the playlist itself
            delete_playlist_query = "DELETE FROM playlists WHERE id_playlist = ?"
            cursor.execute(delete_playlist_query, (id_playlist,))
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error deleting playlist: {e}")
            return False
