import pygame
import time
from pathlib import Path

# Initialiser Pygame
pygame.init()
pygame.mixer.init()


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

    def __repr__(self):  # plus joli pour afficher dans la commande
        return f"{self.id_son=}, {self.nom=}, {self.caracteristiques=}"

    # La partie lecture d'un unique son. Dans quelle classe?
    def play(self):
        # Charger et jouer la musique
        pygame.mixer.music.load(str(self.path_stockage))
        pygame.mixer.music.play()

        # Attendre que la musique soit terminée
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def jouer_en_boucle(self, temps):
        pygame.mixer.music.load(str(self.path_stockage))
        pygame.mixer.music.play(-1)  # -1 pour jouer en boucle
        time.sleep(temps)
        self.stop()
