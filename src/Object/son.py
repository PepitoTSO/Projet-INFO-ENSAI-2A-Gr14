import pygame
import time
from pathlib import Path




class Son:
    """
    Classe qui contient la définition d'un son : ses caractéristiques
    """

    def __init__(
        self, id_son, nom="pas_de_nom", tags=("pas", "de", "tags"), path_stockage=None
    ) -> None:
        if not isinstance(id_son, int):
            raise TypeError("id_son doit être int")
        if not isinstance(nom, str):
            raise TypeError("nom doit être str")
        if not isinstance(tags, list):
            raise TypeError("tags doit être list")
        self.id_son = id_son
        self.nom = nom
        self.tags = tags
        self.path_stockage = Path(path_stockage)
        if path_stockage == None:  # gestion si pas de path_stocakge
            try:
                self.path_stockage = Path(f"./data/son/{id_son}.mp3")
            except Exception as e:
                print(
                    f"Prblm pour trouver le fichier son. La solution la plus simple est de télécharger correctement le fichier :{e}"
                )

    """
    def __repr__(self):  # plus joli pour afficher dans la commande
        return f"{self.id_son=}, {self.nom=}, {self.caracteristiques=}"
    """

    # Tom :
    def __str__(self):
        tags_str = ", ".join(
            self.tags
        )  # Convert tags list to a string for easy display
        return f"Son ID: {self.id_son}, Nom: '{self.nom}', Tags: [{tags_str}], Chemin: {self.path_stockage}"


