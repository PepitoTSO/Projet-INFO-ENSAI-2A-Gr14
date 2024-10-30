from Object.utilisateur import Utilisateur
from Object.son import Son


class Playlist:
    """
    Voici la classe qui gère les playlist
    """


def __init__(
    self, utilisateur: Utilisateur, id_playlist: int, nom_playlist: str, dict_son: dict
):

    if not isinstance(utilisateur, Utilisateur):
        raise TypeError("L'utilisateur n'est pas de la classe Utilisateur.")
    if not isinstance(id_playlist, int):
        raise TypeError("L'id de la playlist doit être de type int.")
    if not isinstance(nom_playlist, str):
        raise TypeError("Le nom de la playlist doit être un str.")
    if not isinstance(dict_son, dict):
        raise TypeError("La liste de son doit être un dictionnaire.")

    for key, value in dict_son.items():
        if not isinstance(key, int):
            raise TypeError("L'élement de clé du dictionnaire n'est pas de type int.")
        if not isinstance(value, Son):
            raise TypeError(
                "L'élement de valeur du dictionnaire n'est pas de type Son."
            )

    self.utilisateur = utilisateur
    self.id_playlist = id_playlist
    self.nom_playlist = nom_playlist
    self.dict_son = dict_son

    def ajouter_son(self, son: Son, ordre: int):
        """Ajouter un nouveau son à la playlist à une position spécifique,
        et décaler les sons existants vers l'arrière pour libérer la place.

        Parameters
        ----------
        son : Son
            L'objet Son que vous souhaitez ajouter à la playlist.
        ordre : int
            L'ordre auquel ajouter le son dans la playlist.

        Raises
        ------
        TypeError
            Si 'son' n'est pas de type Son ou 'ordre' n'est pas un entier.
        """
        # Type checks
        if not isinstance(son, Son):
            raise TypeError("Le son ajouté doit être une instance de la classe Son.")
        if not isinstance(ordre, int):
            raise TypeError("L'ordre doit être un entier.")

        # Decale les sons existants à partir de la position spécifiée vers l'arrière
        if ordre in self.dict_son:
            for key in sorted(self.dict_son.keys(), reverse=True):
                if key >= ordre:
                    # Shift the existing song to the next order
                    self.dict_son[key + 1] = self.dict_son[key]

        # Ajouter le nouveau son à la position spécifiée
        self.dict_son[ordre] = son

    def supprimer_son(self, son: Son):
        for i in range(len(self.list_son)):
            if self.list_son[i][0] == son:
                ordre = self.list_son[i][1]
                self.list_son.pop(i)
        for i in range(len(self.list_son)):
            if self.list_son[i][1] > ordre:
                self.list_son[i][1] += -1

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

    def changer_nom_playlist(self, nouveau_nom):

        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nouveau nom doit être un str.")

        self.nom_playlist = nouveau_nom
