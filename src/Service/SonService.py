from Object.son import son
from DAO.son_DAO import son_DAO
from Object.son import Son


class sonService:

    def __init__(self, son: son):
        if not isinstance(son, son):
            raise TypeError("La son n'est pas type son.")

        self.son = son

    def supprimer_son(self):
        son_DAO().supprimer_son(self.son.id_son)

    ## la partie lecteur son
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

    def play_multiple_sounds(sound_files):  # Chatgpt
        sounds = [
            Son(i, f"sound_{i}", "test", file) for i, file in enumerate(sound_files)
        ]
        for sound in sounds:
            sound.play()
            time.sleep(
                0.1
            )  # Un léger délai pour éviter de jouer tous les sons en même temps

    def jouer_aleatoire(self):
        pass