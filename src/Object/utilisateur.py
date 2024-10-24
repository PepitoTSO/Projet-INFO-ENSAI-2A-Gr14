class Utilisateur:
    def __init__(self, id_utilisateur: int, pseudo: str, mdp: str):
        if not isinstance(id, int):
            raise TypeError("L'id de l'utilisateur n'est pas de la classe int.")

        self.id_utilisateur = id_utilisateur
        self.pseudo = pseudo
        self.mdp = mdp
