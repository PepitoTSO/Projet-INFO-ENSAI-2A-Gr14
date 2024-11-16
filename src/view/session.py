from datetime import datetime
from Object.utilisateur import Utilisateur
from Object.playlist import Playlist
from Object.son import Son
from utils.singleton import Singleton


class Session(metaclass=Singleton):
    """Stocke les données liées à une session.
    Cela permet par exemple de connaitre le joueur connecté à tout moment
    depuis n'importe quelle classe.
    Sans cela, il faudrait transmettre ce joueur entre les différentes vues.
    """

    def __init__(
        self,
        utilisateur: Utilisateur = None,
        playlist: Playlist = None,
        son: Son = None,
    ):
        """Création de la session"""
        self.utilisateur = utilisateur
        self.playlist = playlist
        self.son = son

    def deconnexion(self):
        """Deconecte l'utilisateur"""
        Session().utilisateur = None
        Session().playlist = None
        Session().son = None

    def afficher(self) -> str:
        """Afficher les informations de connexion"""
        res = "Actuellement en session :\n"
        res += "-------------------------\n"
        for att in list(self.__dict__.items()):
            res += f"{att[0]} : {att[1]}\n"

        return res
