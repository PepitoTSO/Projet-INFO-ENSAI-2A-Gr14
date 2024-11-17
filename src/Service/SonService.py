from DAO.son_DAO import Son_DAO
from Object.son import Son
import pygame
import time
import random
import asyncio
from view.session import Session

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

    def play(self, son: Son, duree=None):
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
            time.sleep(duree)
        else:
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        pygame.mixer.music.stop()

    def pause(self):
        """Pause général de tous les channels"""
        pygame.mixer.music.pause()

    def unpause(self):
        """Pause général de tous les channels"""
        pygame.mixer.music.unpause()

    def stop(self):
        """Stop général de tous les channels avec diminution du son (on peut faire un stop aussi)"""
        pygame.mixer.fadeout(3)

    # La partie lecteur par canal

    def stop_channel(self, canal):
        if not isinstance(canal, int):
            raise TypeError("canal doit être int")
        self.selectionner_canal(canal)
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
    async def play_channel(self, son: Son, temps=None, canal=None):
        """
        Joue un son avec Pygame
        Params:
        son : Son
            Une instance de son
        Returns:
        """
        son_a_jouer = pygame.mixer.Sound(str(son.path_stockage))
        canal = self.selectionner_canal(canal)
        print(f"lecture du son :{son.nom}")
        if temps:
            canal.play(son_a_jouer, loops=-1)
            await asyncio.sleep(temps)
        else:
            canal.play(son_a_jouer)
            while canal.get_busy():
                await asyncio.sleep(1)
        canal.stop()

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


async def main():
    son_test = Son(1, path_stockage="./data/test.mp3")
    son2 = Son(2, path_stockage="./data/son/57740.mp3")

    son_service = SonService()

    t1 = asyncio.create_task(son_service.play_channel(son_test, 10))
    t2 = asyncio.create_task(son_service.jouer_aleatoire(son2, 2, 5, 20))

    await t1
    await t2


if __name__ == "__main__":
    asyncio.run(main())
