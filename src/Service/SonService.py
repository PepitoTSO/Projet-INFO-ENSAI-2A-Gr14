from DAO.son_DAO import Son_DAO
from Object.son import Son
import pygame
import time
import random

# Initialiser Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(8) # pour superposer jusqu'à 8 sons


class SonService():
    """
    Implemente les méthodes associées à la classe Son
    """
    ##La partie DAO
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

    ## la partie lecteur son

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
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def jouer_en_boucle(self, son: Son, temps: int):
        if not isinstance(temps, int):
            raise TypeError("temps doit être int")
        pygame.mixer.music.load(str(son.path_stockage))
        pygame.mixer.music.play(-1)  # -1 pour jouer en boucle
        time.sleep(temps)
        self.stop()

    # elle est un peu bizarre celle là
    def play_multiple_sounds(self, sound_files):  # Chatgpt
        sounds = [
            Son(i, f"sound_{i}", "test", file) for i, file in enumerate(sound_files)
        ]
        for sound in sounds:
            sound.play()
            time.sleep(
                0.1
            )  # Un léger délai pour éviter de jouer tous les sons en même temps

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
            self.play(son)
            attente_random = random.uniform(attente_min, attente_max)
            time.sleep(attente_random)
        self.stop()

    def superposer_son(self, son: Son):
        '''
        Joue un son avec Pygame
        Params:
        son : Son
            Une instance de son
        Returns:
    
        '''
        # Charger et jouer la musique
        pygame.mixer.music.load(str(son.path_stockage))
        channel_libre = pygame.mixer.find_channel()
        if channel_libre:
            channel_libre.play(son)

        # Attendre que la musique soit terminée
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    def play_channel(self, son: Son, canal = None):
        '''
        Joue un son avec Pygame
        Params:
        son : Son
            Une instance de son
        Returns:
    
        '''
        son_a_jouer = pygame.mixer.Sound(str(son.path_stockage))
        if canal is None:
            canal = pygame.mixer.find_channel()
        else:
            canal = pygame.mixer.Channel(canal)
        canal.play(son_a_jouer)


if __name__ == '__main__':
    son_test = Son(1, path_stockage='./data/test.mp3')
    SonService().play_channel(son_test, 2)
    time.sleep(3)
    SonService().play_channel(son_test, 3)
    time.sleep(3)
