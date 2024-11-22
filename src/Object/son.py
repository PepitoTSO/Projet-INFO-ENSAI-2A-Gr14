from pathlib import Path


class Son:
    """
    Classe qui représente un son, avec des informations sur son ID, son nom, ses tags et son chemin de stockage.

    Attributes
    ----------
    id_son : int
        L'identifiant unique du son.
    nom : str
        Le nom du son (par défaut "pas_de_nom").
    tags : list
        Liste des tags associés au son (par défaut une liste vide).
    path_stockage : str
        Le chemin de stockage du fichier sonore. Si non fourni, un chemin par défaut est généré.
    """

    def __init__(self, id_son, nom="pas_de_nom", tags=[], path_stockage=None) -> None:
        """
        Initialise un objet Son avec l'ID, le nom, les tags et le chemin de stockage du fichier sonore.

        Parameters
        ----------
        id_son : int
            L'identifiant unique du son.
        nom : str, optional
            Le nom du son (par défaut "pas_de_nom").
        tags : list, optional
            Liste de tags associés au son (par défaut une liste vide).
        path_stockage : str, optional
            Le chemin du fichier de stockage du son (par défaut, il est généré à partir de l'ID).
        """

        if not isinstance(id_son, int):
            raise TypeError("id_son doit être int")
        if not isinstance(nom, str):
            raise TypeError("nom doit être str")
        if not isinstance(tags, list):
            raise TypeError("tags doit être list")
        self.id_son = id_son
        self.nom = nom
        self.tags = tags
        if path_stockage is None:
            try:
                self.path_stockage = Path(f"./data/son/{id_son}.mp3")
            except Exception as e:
                print(
                    f"Prblm pour trouver le fichier son. La solution la plus simple est\
                        de télécharger correctement le fichier :{e}"
                )
        else:
            self.path_stockage = path_stockage

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le son.

        Returns
        -------
        str
            Représentation sous forme de chaîne de caractères du son avec son ID,
            son nom, ses tags et son chemin de stockage.
        """

        tags_str = ", ".join(self.tags)
        return f"Son ID: {self.id_son}, Nom: '{self.nom}', Tags: [{tags_str}], Chemin: {self.path_stockage}"

    def __eq__(self, other):
        """Permet de définir une égalité entre deux sons, ici sur les arguments"""

        if not isinstance(other, Son):
            return False
        return (
            self.id_son == other.id_son
            and self.nom == other.nom
            and self.tags == other.tags
            and self.path_stockage == other.path_stockage
        )
