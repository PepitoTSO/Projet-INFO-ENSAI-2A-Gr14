from src.Object.playlist import Playlist


class PlaylistService:

    def __init__(self, playlist: Playlist):
        if not isinstance(playlist, Playlist):
            raise TypeError("La plylist n'est pas type Playlist.")

        self.playlist = playlist

    

