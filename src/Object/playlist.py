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
        list_son: list,
    ):
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe Utilisateur.")
        if not isinstance(id_playlist, (int, type(None))):
            raise TypeError("L'id de la playlist doit être de type int ou None.")
        if not isinstance(nom_playlist, str):
            raise TypeError("Le nom de la playlist doit être un str.")
        if not isinstance(list_son, list):
            raise TypeError("La liste de son doit être une liste.")

        for item in list_son:
            son, ordre = item
            if not isinstance(son, Son):
                raise TypeError("Les objets sons doivent de type Son")
            if not isinstance(ordre, int):
                raise TypeError("L'ordre dans la playlist doit être de type int")

        self.utilisateur = utilisateur
        self.id_playlist = id_playlist
        self.nom_playlist = nom_playlist
        self.list_son = list_son

    def ajouter_son_playlist(self, son: Son, ordre: int):
        # Vérifier si la position demandée est valide
        if ordre < 1 or ordre > len(self.list_son) + 1:
            raise ValueError(
                "Ordre invalide, doit être entre 1 et len(self.list_son) + 1"
            )

        # Réajuster les ordres si l'ordre est déjà pris
        for item in self.list_son:
            if item[1] >= ordre:
                item[1] += 1

        # Ajouter le nouveau son à la playlist
        self.list_son.append([son, ordre])

        # Trier la playlist par ordre croissant
        self.list_son.sort(key=lambda x: x[1])

        # Réindexer la liste pour garantir des ordres séquentiels cohérents
        for i, item in enumerate(self.list_son):
            item[1] = i + 1

    def supprimer_son(self, son: Son):
        ordre_a_supprimer = None
        for item in self.list_son:
            if item[0] == son:
                ordre_a_supprimer = item[1]
                break
        if ordre_a_supprimer is None:
            # Son n'est pas trouvée dans la playlist
            return False
        # Supprimer son de la playlist
        del self.list_son[ordre_a_supprimer - 1]
        # Shift
        for item in self.list_son:
            if item[1] > ordre_a_supprimer:
                item[1] = item[1] - 1
        return True

    ### La fonctionnalité de voir si son est bien dans playlist n'est pas testé dans le fichier test
    def changer_ordre(self, son: Son, ordre: int):
        # Vérification que son est dans la playlist
        # trouve = False
        # for item in self.list_son:
        #    if item[0].id_son == son.id_son:
        #        trouvé = True
        #        break
        # if trouve == False:
        #    raise ValueError("Son doit être dans la playlist")

        if ordre > len(self.list_son) + 1 or ordre < 1:
            raise ValueError(
                "La position ne peut etre inférieure à 0 ou supérieure à len(list_son)"
            )

        ancien_son = None
        for item in self.list_son:
            if item[1] == ordre:
                ancien_son = item[0]
                item[0] = son

        for item in self.list_son:
            if item[0] == son and item[1] != ordre:
                item[0] = ancien_son

    def changer_nom_playlist(self, nouveau_nom):
        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nouveau nom doit être un str.")

        self.nom_playlist = nouveau_nom

    def retirer_son(self, son: Son):
        # Trouver l'item à supprimer
        item_a_supprimer = None
        for item in self.list_son:
            if item[0] == son:
                item_a_supprimer = item
                break
        if item_a_supprimer is None:
            # Son non trouvé dans la playlist
            return False

        # Obtenir l'ordre du son à supprimer
        ordre_a_supprimer = item_a_supprimer[1]

        # Supprimer le son de la playlist
        self.list_son.remove(item_a_supprimer)

        # Décrémenter l'ordre des sons suivants
        for item in self.list_son:
            if item[1] > ordre_a_supprimer:
                item[1] -= 1

        return True

    def __str__(self):
        # Building a representation of the playlist
        playlist_str = f"Playlist '{self.nom_playlist}' (ID: {self.id_playlist}) by {self.utilisateur}:\n"
        playlist_str += "Liste des Sons:\n"

        for item in self.list_son:
            son, ordre = item
            playlist_str += f"  Ordre {ordre}: {son}\n"

        return playlist_str


son1 = Son(
    id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
)
son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
son3 = Son(id_son=3, nom="son3", tags=["pluie"], path_stockage="data/test.mp3")
utilisateur = Utilisateur("a", "b")

playlist = Playlist(
    utilisateur=utilisateur,
    id_playlist=None,
    nom_playlist="test",
    list_son=[[son1, 1], [son2, 2]],
)
"""
playlist.ajouter_son_playlist(son3, 3)
playlist.supprimer_son(son1)
print(playlist.list_son[1][0])

print(playlist)

playlist.ajouter_son_playlist(son3, 1)
print(playlist)

playlist.supprimer_son(son3)
print(playlist)

playlist.changer_ordre(son1, 2)
print(playlist)

playlist.changer_nom_playlist("playlist1")
print(playlist)
"""
