class Utilisateur:
    def __init__(self, pseudo: str, mdp_hache: str, list_playlist: list = None):
        self.pseudo = pseudo
        self.mdp_hache = mdp_hache

    def __str__(self):
        return f"Utilisateur: {self.pseudo}"
