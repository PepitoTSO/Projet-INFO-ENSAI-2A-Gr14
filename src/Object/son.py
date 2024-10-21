import pygame
import sys

# Initialiser Pygame
pygame.init()
pygame.mixer.init()



class Son():
    '''
    Classe qui contient definition d'un son : ses caractéristiques

    '''
    def __init__(self,id_son, nom, caracteristiques, path_stcoakge = None) -> None:
        self.id_son = id_son
        self.nom = nom
        self.caracteristiques = caracteristiques
        self.path_stockage = methodelocatedansutils() # à voir comment faire méthode ou variable?
        self.musique = pygame.mixer.Sound(self.path_stockage)

    def afficher_son(self):
        desc = f"{self.id_son=},{self.nom=},{self.caracteristiques=}"
        print(desc)

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
