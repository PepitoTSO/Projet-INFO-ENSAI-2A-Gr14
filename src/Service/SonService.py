'''
Oui
'''
from Object.son import Son
#from DAO.son_DAO import SonDAO

class SonService():
    def __init__(self, son: Son):
        if not isinstance(son, Son):
            raise TypeError("La son n'est pas type son.")

        self.son = son

    def ajouter_son(self, son, id_playlist=None, ordre=None):
        try:
            #SonDAO().ajouter_son(son, id_playlist, ordre)
            return True
        except Exception as e:
            print(f"Prblm ajout son :{e}")
            return False


    def supprimer_son(self):
        #son_DAO().supprimer_son(self.son.id_son)
        pass

    def obtenir_son(self):
        pass

    def lister_son(self):
        pass

    def jouer_son_en_boucle(self):
        pass

    def jouer_son(self):
        print("lecture :",repr(self.son))
        self.son.play()
    
    def changer_tags_son(self):
        pass

    def superposer_son(self):
        pass