class Utilisateur:
    def __init__(self, pseudo: str, mdp_hache: str, list_playlist: list = None):
        if list_playlist is None:
            list_playlist = []
        self.pseudo = pseudo
        self.mdp_hache = mdp_hache
        self.list_playlist = list_playlist
