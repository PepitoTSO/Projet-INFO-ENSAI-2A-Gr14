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

    def __init__(self, id_son, nom="pas_def", caracteristiques="pas_def") -> None:
        self.id_son = id_son
        self.nom = nom  # à voir si on fait pas DAO.trouver_son_par_id
        self.caracteristiques = (
            caracteristiques  # à voir si on fait pas DAO.trouver_son_par_id
        )
        self.path_stockage = Path(f"./data/son/{id_son}.mp3")

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


if __name__ == "__main__":
    test = Son(1, "test", "oui", "data/test.mp3")
    print(test.id_son)
    print(repr(test))
    test.play()
