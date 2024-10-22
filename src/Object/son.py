import pygame
import sys
from pathlib import Path
# Initialiser Pygame
pygame.init()
pygame.mixer.init()



class Son():
    '''
    Classe qui contient definition d'un son : ses caractéristiques

    '''
    def __init__(self,id_son, nom, caracteristiques, path = None) -> None:
        self.id_son = id_son
        self.nom = nom
        self.caracteristiques = caracteristiques
        self.path_stockage = Path(path)
        self.musique = pygame.mixer.Sound(self.path_stockage)

    def __repr__(self):
        return f"{self.id_son=},{self.nom=},{self.caracteristiques=}"

    ## a relier à l'interface graphique
    def play(self):
        
        self.musique.play()

    def pause(self):
        pygame.mixer.pause()

    def unpause(self):
        pygame.mixer.unpause()

    def stop(self):
        self.musique.stop()

    def jouer_en_boucle(self, temps):
        pass


if __name__ == "__main__":
    test=Son(1,'test','oui','data/test.mp3')
    test.play()
