class Utilisateur:
    def __init__(self, id: int, dd, ddc, playlist):
        if not isinstance(id, int):
            raise TypeError("L'id de l'utilisateur n'est pas de la classe int.")

        self.id = id
        self.date_debut = date_debut
        self.date_derniere_co = date_derniere_co
        self.playlist = playlist
