from DAO.son_DAO import Son_DAO
from Object.son import Son
import pygame
import time
import random
import asyncio

# Initialiser Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(8)  # pour superposer jusqu'à 8 sons
pygame.mixer.set_reserved(1)  # reserve le channel 1 pour playlist


class SonService:
    """
    Implemente les méthodes associées à la classe Son
    """

    # La partie DAO
    def supprimer_son(self, son: Son):
        """
        Supprime un son selon la DAO
        Params:
        son : Son
            Une instance de son
        Returns:
        """
        if not isinstance(son.id_son, int):
            raise TypeError("id_son doit être int")
        Son_DAO().supprimer_son(son.id_son)

    def ajouter_son(self, son: Son):
        """
        Ajoute un son selon la DAO
        Params:
        son : Son
            Une instance de son
        Returns:
        """
        r = Son_DAO().ajouter_son(son)
        if r is None:
            print("Erreur lors de l'ajout")
        return r

    def lister_son(self):
        """
        Retourne la liste des sons d'un utilisateur selon la DAO
        """
        r = Son_DAO().get_all_son()
        if r is None:
            print("Erreur lors de la consultation bdd")
        return r

    # la partie lecteur son général

    async def play(self, son: Son, duree=None):
        """
        Joue un son avec Pygame
        Params:
        son : Son
            Une instance de son
        duree : int
            Permet d'avoir une preview
        Returns:

        """
        # Charger et jouer la musique
        pygame.mixer.music.load(str(son.path_stockage))
        pygame.mixer.music.play()

        # Attendre que la musique soit terminée
        if duree:
            await asyncio.sleep(duree)
        else:
            while pygame.mixer.music.get_busy():
                await asyncio.sleep(0.1)
        pygame.mixer.music.stop()

    def pause(self, etat):
        """Met en pause tous les sons en cours de lecture"""
        if etat == 0:
            pygame.mixer.pause()
            print("Pause")
        if etat == 1:
            pygame.mixer.unpause()
            print("Reprise")

    def stop(self):
        """Stop général de tous les channels avec diminution du son (on peut faire un stop aussi)"""
        pygame.mixer.fadeout(3)
        print("Fin de la lecture")

    # La partie lecteur par canal

    def stop_channel(self, canal):
        """Stop sur un canal determine"""
        if not isinstance(canal, int):
            raise TypeError("canal doit être int")
        canal = self.selectionner_canal(canal)
        canal.stop()

    def stop_sauf_plist(self):
        """
        Stop les channels sauf le 1 pour avoir une base propre pour la playlist
        """
        n_channels = pygame.mixer.get_num_channels()
        for i in range(2, n_channels):
            self.stop_channel(i)

    def selectionner_canal(self, canal=None):
        """
        Permet de trouver un canal disponible
        """
        if canal is None:
            canal = pygame.mixer.find_channel()
        else:
            canal = pygame.mixer.Channel(canal)
        return canal

    # Les fonctions asynchrones
    async def play_canal(self, son: Son, temps=None, canal=None):
        """
        Joue un son avec Pygame
        Params:
        son : Son
            Une instance de son
        """
        try:
            son_a_jouer = pygame.mixer.Sound(str(son.path_stockage))
        except Exception as e:
            print(f"Impossible de charger le son : {e}")
            print("Essayer de le télécharger")
            return
        canal = self.selectionner_canal(canal)
        # print(f"lecture du son :{son.nom}")
        if temps:
            canal.play(son_a_jouer, loops=-1)
            await asyncio.sleep(temps)
        else:
            canal.play(son_a_jouer)
            while canal.get_busy():
                await asyncio.sleep(0.1)
        canal.stop()

    def pause_canal(self, canal):
        """Met en pause le son en cours si un canal est en lecture."""
        obj_canal = self.selectionner_canal(canal)
        if obj_canal.get_busy():
            self.temps_restant = obj_canal.get_pos()
            obj_canal.stop()
            print(f"Son mis en pause à {self.temps_restant}ms")

    async def jouer_aleatoire(
        self, son: Son, attente_min: int, attente_max: int, duree: int, canal=None
    ):
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
        # Evite de couper les sons
        temps_fadeout = 2
        # Charger le son et selection canal
        canal = self.selectionner_canal(canal)
        son_a_jouer = pygame.mixer.Sound(str(son.path_stockage))

        # Boucle de lecture aleatoire
        debut = time.time()
        while time.time() - debut < duree:
            canal.play(son_a_jouer)
            attente_random = random.uniform(attente_min, attente_max)
            await asyncio.sleep(attente_random)
            canal.fadeout(temps_fadeout)
