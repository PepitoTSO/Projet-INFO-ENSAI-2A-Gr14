from DAO.son_DAO import Son_DAO
from Object.son import Son
import pygame
import time
import random

# Initialiser Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(8)  # pour superposer jusqu'à 8 sons
pygame.mixer.set_reserved(1)  # reserve le channel 1 pour playlist


class SonService():
    """
    Implemente les méthodes associées à la classe Son
    """
    # La partie DAO
    def supprimer_son(self, son: Son):
        '''
        Supprime un son selon la DAO
        Params:
        son : Son
            Une instance de son
        Returns:
        '''
        if not isinstance(son.id_son, int):
            raise TypeError('id_son doit être int')
        Son_DAO().supprimer_son(son.id_son)

    def ajouter_son(self, son: Son):
        '''
        Ajoute un son selon la DAO
        Params:
        son : Son
            Une instance de son
        Returns:
        '''
        r = Son_DAO().ajouter_son(son)
        if r is None:
            print("Erreur lors de l'ajout")
        return r

    # la partie lecteur son général

    def play(self, son: Son):
        '''
        Joue un son avec Pygame
        Params:
        son : Son
            Une instance de son
        Returns:

        '''
        # Charger et jouer la musique
        pygame.mixer.music.load(str(son.path_stockage))
        pygame.mixer.music.play()

        # Attendre que la musique soit terminée
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    def pause(self):
        '''Pause général de tous les channels'''
        pygame.mixer.music.pause()

    def unpause(self):
        '''Pause général de tous les channels'''
        pygame.mixer.music.unpause()

    def stop(self):
        '''Stop général de tous les channels avec diminution du son (on peut faire un stop aussi)'''
        pygame.mixer.fadeout(1000)

    # La partie lecteur par canal
    def play_channel(self, son: Son, canal=None):
        '''
        Joue un son avec Pygame
        Params:
        son : Son
            Une instance de son
        Returns:
        '''
        son_a_jouer = pygame.mixer.Sound(str(son.path_stockage))
        canal = self.selectionner_canal(canal)
        canal.play(son_a_jouer)

    def stop_channel(self, canal):
        if not isinstance(canal, int):
            raise TypeError("canal doit être int")
        self.selectionner_canal(canal)
        canal.stop()

    def stop_sauf_plist(self):
        '''
        Stop les channels sauf le 1 pour avoir une base propre pour la playlist
        '''
        n_channels = pygame.mixer.get_num_channels()
        for i in range(2, n_channels):
            self.stop_channel(i)

    def selectionner_canal(self, canal=None):  # idéalement on va retourner aussi le numéro du canal pour pas être perdu + il va y avoir des problèmes pour réserver canal 1 pour playlist
        if canal is None:
            canal = pygame.mixer.find_channel()
        else:
            canal = pygame.mixer.Channel(canal)
        return canal

    # Les fonctions
    def jouer_en_boucle(self, son: Son, canal, temps: int):
        '''
        Joue un son avec Pygame
        Params:
        son : Son
            Une instance de son
        Returns:
        '''
        son_a_jouer = pygame.mixer.Sound(str(son.path_stockage))
        canal = self.selectionner_canal(canal)
        canal.play(son_a_jouer, -1, temps)

    def jouer_aleatoire(self, son: Son, attente_min, attente_max, duree):
        """
        Methode pour jouer un son aléatoirement pendant une duree et à une fréquence définie par attente_min et max.
        Par exemple, des bruits d'éclair ou d'animaux qui seront superposés à ceux d'une forêt
        """
        if not isinstance(duree, int):
            raise TypeError("duree doit etre int")
        if not isinstance(attente_min, int) and attente_min > 0:
            raise TypeError("attente_min doit etre int et positif")
        if not isinstance(attente_max, int) and attente_max > attente_min:
            raise TypeError("attente_max doit etre int et plus grand que attente_min")

        debut = time.time()
        while time.time() - debut < duree:
            self.play_channel(son)  # y'a surement moyen de casser la fonction avec un son trop long par rapport à la duree
            attente_random = random.uniform(attente_min, attente_max)
            time.sleep(attente_random)

    def avancer_xtemps(self, temps):
        '''permet d'avancer 10/20/x secondes du son'''
        pass


if __name__ == '__main__':
    son_test = Son(1, path_stockage='./data/test.mp3')
    SonService().jouer_en_boucle(son_test, 2, 300)

