from Object.utilisateur import Utilisateur
from Object.son import Son


class Playlist:
    """
    Voici la classe qui gère les playlist
    """

    def __init__(
        self,
        utilisateur: Utilisateur,
        id_playlist: int,
        nom_playlist: str,
        sons_playlist: list,
    ):
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe Utilisateur.")
        if not isinstance(id_playlist, int):
            raise TypeError("L'id de la playlist doit être de type int.")
        if not isinstance(nom_playlist, str):
            raise TypeError("Le nom de la playlist doit être un str.")
        if not isinstance(sons_playlist, list):
            raise TypeError("La liste de son doit être une liste.")

        for item in sons_playlist:
            son, ordre = item
            if not isinstance(son, Son):
                raise TypeError("Les objets sons doivent de type Son")
            if not isinstance(ordre, int):
                raise TypeError("L'ordre dans la playlist doit être de type int")

        self.utilisateur = utilisateur
        self.id_playlist = id_playlist
        self.nom_playlist = nom_playlist
        self.sons_playlist = sons_playlist

    def ajouter_son_playlist(self, son: Son, ordre: int):
        # Réajuster les ordres si l'ordre est déjà pris
        for item in self.sons_playlist:
            if item[0] >= ordre:
                item[0] += 1

        # Ajouter le nouveau son à la playlist avec l'ordre spécifié
        self.sons_playlist.append([ordre, son])

        # Trier la playlist par ordre croissant
        self.sons_playlist.sort(key=lambda x: x[0])

    def supprimer_son(self, son: Son):

        ordre_to_remove = None
        for ordre, existing_son in :
            if existing_son == son:
                ordre_to_remove = ordre
                break
        if ordre_to_remove is None:
            # Son not found in the playlist
            return
        # Remove the son from the playlist
        del self.dict_son[ordre_to_remove]
        # Shift orders of subsequent songs
        for ordre in sorted(self.dict_son.keys()):
            if ordre > ordre_to_remove:
                self.dict_son[ordre - 1] = self.dict_son.pop(ordre)

    def changer_ordre(self, son, ordre: int):

        if ordre > len[self.sons_playlist] + 1 or ordre < 0:
            raise ValueError(
                "La position ne peut etre inférieure à 0 ou supérieure à n + 1"
            )

        for i in range(len[self.sons_playlist]):
            if self.sons_playlist[i][0] == son:
                ordre_ancien = self.sons_playlist[i][1]
                self.sons_playlist.pop(i)

        for i in range(len[self.sons_playlist]):
            if self.sons_playlist[i][1] > ordre_ancien:
                self.sons_playlist[i][1] += -1

        for i in range(len[self.sons_playlist]):
            if self.sons_playlist[i][1] >= ordre:
                self.sons_playlist[i][1] += 1

        self.sons_playlist.append([son, ordre])

    def changer_nom_playlist(self, nouveau_nom):

        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nouveau nom doit être un str.")

        self.nom_playlist = nouveau_nom


son1 = Son(id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage=None)
son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage=None)
son3 = Son(id_son=3, nom="son3", tags=["pluie"], path_stockage=None)


