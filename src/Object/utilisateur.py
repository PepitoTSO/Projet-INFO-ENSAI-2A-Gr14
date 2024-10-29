class Utilisateur:
    def __init__(self, pseudo: str, mdp_hache: str, list_playlist: list = []):

        self.pseudo = pseudo
        self.mdp_hache = mdp_hache
        self.list.playlist = list_playlist
