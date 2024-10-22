from src.Object.utilisateur import Utilisateur
from src.Object.son import Son
from src.Service.PlaylistService import PlaylistService


class Playlist:
    """Voici la classe qui gère les playlist"""

    def __init__(
        self,
        utilisateur: Utilisateur,
        id_playlist: int,
        nom_playlist: str,
        list_son: list = [],
    ):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_playlist, int):
            raise TypeError("L'id de la playlist doit être de type int.")
        if not isinstance(nom_playlist, str):
            raise TypeError("Le nom de la playlist doit être un str")
        if not isinstance(list_son, list):
            raise TypeError("La liste de son doit être une liste.")

        self.utilisateur = utilisateur
        self.id_playlist = id_playlist
        self.nom_playlist = nom_playlist
        self.list_son = list_son

    def ajouter_son(self, son: Son, ordre: int):
        if not isinstance(ordre, int):
            raise TypeError("L'ordre doit être un int.")
        if not isinstance(son, Son):
            raise TypeError("son doit être un objet de classe Son.")

        for i in range(len(self.list_son)):
            if self.list_son[i][1] > ordre:
                self.list_son[i][1] += 1

        self.list_son.append([son, ordre])

        PlaylistService(self).ajouter_son_a_playlist(son)

    def supprimer_son(self, son: Son):
        for i in range(len(self.list_son)):
            if self.list_son[i][0] == son:
                ordre = self.list_son[i][1]
                self.list_son.pop(i)
        for i in range(len(self.list_son)):
            if self.list_son[i][1] > ordre:
                self.list_son[i][1] += -1

        PlaylistService(self).retirer_son_de_playlist(son)

    def changer_ordre(self, son, ordre: int):

        if ordre > len[self.list_son] + 1 or ordre < 0:
            raise ValueError(
                "La position ne peut etre inférieure à 0 ou supérieure à n + 1"
            )

        for i in range(len[self.list_son]):
            if self.list_son[i][0] == son:
                ordre_ancien = self.list_son[i][1]
                self.list_son.pop(i)

        for i in range(len[self.list_son]):
            if self.list_son[i][1] > ordre_ancien:
                self.list_son[i][1] += -1

        for i in range(len[self.list_son]):
            if self.list_son[i][1] >= ordre:
                self.list_son[i][1] += 1

        self.list_son.append([son, ordre])

        PlaylistService(self).changer_ordre_son(son, ordre)

    def changer_nom_playlist(self, nouveau_nom):

        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nouveau nom doit être un str.")

        self.nom_playlist = nouveau_nom

        PlaylistService(self).changer_nom_playlist(nouveau_nom)
