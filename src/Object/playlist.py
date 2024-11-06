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
        if not isinstance(id_playlist, int):
            raise TypeError("L'id de la playlist doit être de type int.")
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

    """
    def ajouter_son_playlist(self, son: Son, ordre: int):
        # Réajuster les ordres si l'ordre est déjà pris
        for item in self.list_son:
            if item[1] >= ordre:
                item[1] += 1

        # Ajouter le nouveau son à la playlist avec l'ordre spécifié
        self.list_son.append([ordre, son])

        # Trier la playlist par ordre croissant
        self.list_son.sort(key=lambda x: x[1])
    """

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
        self.list_son.append([ordre, son])

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

    def changer_ordre(self, son, ordre: int):
        if ordre > len(self.list_son) + 1 or ordre < 0:
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

    """
    def changer_ordre(self, son, ordre: int):
        # Vérifier si la position demandée est valide
        if ordre < 1 or ordre > len(self.list_son):
            raise ValueError(
                "La position ne peut être inférieure à 1 ou supérieure à la taille de la liste"
            )

        # Trouver l'index du 'son' actuel dans la liste
        index_a_changer = None
        for index, item in enumerate(self.list_son):
            if item[0] == son:
                index_a_changer = index
                break

        if index_a_changer is None:
            raise ValueError("Le son spécifié n'est pas présent dans la liste.")

        # Supprimer le 'son' de sa position actuelle
        element = self.list_son.pop(index_a_changer)

        # Ajuster l'index pour l'insertion car `ordre` est en base 1
        nouvel_index = ordre - 1

        # Insérer l'élément à la nouvelle position
        self.list_son.insert(nouvel_index, element)

        # Réindexer la liste pour que les ordres soient cohérents (base 1)
        for i, item in enumerate(self.list_son):
            item[1] = i + 1  # Assigner un ordre basé sur la position actuelle dans la liste


    """

    def changer_nom_playlist(self, nouveau_nom):
        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nouveau nom doit être un str.")

        self.nom_playlist = nouveau_nom

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
print(son1)
print(utilisateur)
playlist = Playlist(
    utilisateur=utilisateur,
    id_playlist=1,
    nom_playlist="test",
    list_son=[[son1, 1], [son2, 2]],
)
print(playlist)

playlist.ajouter_son_playlist(son3, 3)
print(playlist)
