import pygame
import time
from pathlib import Path

# Initialiser Pygame
pygame.init()
pygame.mixer.init()

class Son():
    '''
    Classe qui contient la définition d'un son : ses caractéristiques
    '''
    def __init__(self, id_son, nom, caracteristiques, path=None) -> None:
        self.id_son = id_son
        self.nom = nom
        self.caracteristiques = caracteristiques
        self.path_stockage = Path(path)

    def __repr__(self):
        return f"{self.id_son=}, {self.nom=}, {self.caracteristiques=}"

    ## à relier à l'interface graphique
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
        time.sleep(temps)  # Attendre le temps spécifié
        self.stop()



if __name__ == "__main__":
    test = Son(1, 'test', 'oui', 'data/test.mp3')
    print(test.id_son)
    print(repr(test))

