class Utilisateur:
    def __init__(self, id: int):
        if not isinstance(id, int):
            raise TypeError("L'id de l'utilisateur n'est pas de la classe int.")

        self.id = id
