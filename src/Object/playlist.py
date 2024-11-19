from Object.utilisateur import Utilisateur
from Object.son import Son


class Playlist:
    """
    Représente une playlist gérée par un utilisateur.

    Attributes
    ----------
    utilisateur : Utilisateur
        L'utilisateur propriétaire de la playlist.
    id_playlist : int
        L'identifiant unique de la playlist.
    nom_playlist : str
        Le nom de la playlist.
    list_son : list
        Une liste de tuples contenant les objets Son et leur ordre dans la playlist.
    """

    def __init__(
        self,
        utilisateur: Utilisateur,
        id_playlist: int,
        nom_playlist: str,
        list_son: list,
    ):
        """
        Initialise une nouvelle instance de la classe Playlist.

        Parameters
        ----------
        utilisateur : Utilisateur
            L'utilisateur propriétaire de la playlist.
        id_playlist : int
            L'identifiant unique de la playlist.
        nom_playlist : str
            Le nom de la playlist.
        list_son : list
            Une liste de tuples contenant les objets Son et leur ordre dans la playlist.

        Raises
        ------
        TypeError
            Si les types des paramètres ne sont pas conformes aux attentes.
        """

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe Utilisateur.")
        if not isinstance(id_playlist, (int, type(None))):
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

    def ajouter_son_playlist(self, son: Son, ordre: int):
        """
        Ajoute un son à la playlist à une position spécifiée.

        Parameters
        ----------
        son : Son
            L'objet Son à ajouter à la playlist.
        ordre : int
            La position dans la playlist où le son doit être ajouté.

        Raises
        ------
        ValueError
            Si l'ordre spécifié n'est pas valide.
        """

        # Vérifier si la position demandée est valide
        if ordre < 1:
            raise ValueError("Ordre invalide, ordre doit être > 1")

        if ordre > len(self.list_son) + 1:
            self.list_son.append([son, ordre])

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
        """
        Supprime un son de la playlist.

        Parameters
        ----------
        son : Son
            L'objet Son à supprimer de la playlist.

        Returns
        -------
        bool
            True si le son a été supprimé avec succès, False sinon.
        """

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
        """
        Change l'ordre d'un son dans la playlist.

        Parameters
        ----------
        son : Son
            L'objet Son dont l'ordre doit être changé.
        ordre : int
            La nouvelle position dans la playlist.

        Raises
        ------
        ValueError
            Si l'ordre spécifié est invalide ou si le son n'est pas trouvé dans la playlist.
        """

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
        """
        Change le nom de la playlist.

        Parameters
        ----------
        nouveau_nom : str
            Le nouveau nom de la playlist.

        Raises
        ------
        TypeError
            Si le nouveau nom n'est pas une chaîne de caractères.
        """

        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nouveau nom doit être un str.")

        self.nom_playlist = nouveau_nom

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères de la playlist.

        Returns
        -------
        str
            Représentation en chaîne de caractères de la playlist.
        """

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

print(playlist)
playlist.ajouter_son_playlist(son3, 5)
print(playlist)
