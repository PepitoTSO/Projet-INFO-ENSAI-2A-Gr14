from pathlib import Path
import nava

class Son():
    '''
    Classe qui contient la définition d'un son : ses caractéristiques
    '''
    def __init__(self, id_son, nom, caracteristiques, path=None) -> None:
        self.id_son = id_son
        self.nom = nom
        self.caracteristiques = caracteristiques
        self.path_stockage = Path(path)
        self.musique = nava.Audio(self.path_stockage)

    def __repr__(self):
        return f"{self.id_son=},{self.nom=},{self.caracteristiques=}"

    ## a relier à l'interface graphique
    def play(self):
        self.musique.play()

    def pause(self):
        self.musique.pause()

    def unpause(self):
        self.musique.resume()

    def stop(self):
        self.musique.stop()

    def jouer_en_boucle(self, temps):
        self.musique.loop(temps)

if __name__ == "__main__":
    test=Son(1,'test','oui','data/test.mp3')
    repr(test)
    test.play()