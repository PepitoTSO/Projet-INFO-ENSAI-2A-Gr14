from src.Object.playlist import Playlist


class Utilisateur:
    def __init__(self, id: int, date_debut, date_derniere_co, playlist):
        if not isinstance(utilisateur, int):
            raise TypeError("L'utilisateur n'est pas de la classe int.")

        self.id = id
        self.date_debut = date_debut
        self.date_derniere_co = date_derniere_co
        self.playlist = []
