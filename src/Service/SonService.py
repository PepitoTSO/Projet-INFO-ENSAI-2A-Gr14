'''
Oui
'''
from Object.son import Son

class SonService():
    def __init__(self, son: Son):
        if not isinstance(son, Son):
            raise TypeError("La son n'est pas type son.")

        self.son = son

    def ajouter_son(self):
        pass

    def supprimer_son(self):
        son_DAO().supprimer_son(self.son.id_son)

    def obtenir_son(self):
        pass

    def lister_son(self):
        pass

    def jouer_son_en_boucle(self):
        pass

    def jouer_son(self):
        self.son.play()
    
    def changer_tags_son(self):
        pass

    def superposer_son(self):
        pass