'''
Oui
'''
from Object.son import Son

class SonService():
    def __init__(self, son: son):
        if not isinstance(son, son):
            raise TypeError("La son n'est pas type son.")

        self.son = son

    def supprimer_son(self):
        son_DAO.supprimer_son(self.son.id_son)

    def modifier_nom_son(self, nouveau_nom: str):
        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nom doit être de type str.")

        son_DAO.modifier_nom_son(self.son.id_son, nouveau_nom)

    def changer_ordre_son(self, son: Son, ordre: int):

        id_son = self.son.id_son
        ancien_ordre = son_DAO().get_ordre_son(id_son, son)
        son_DAO().supprimer_son(id_son, son)
        son_DAO().changer_ordre_son(id_son, ancien_ordre, False)
        son_DAO().changer_ordre_son(id_son, ordre, True)
        son_DAO().ajouter_son(id_son, son, ordre)

    def retirer_son_son(self, son: Son):

        id_son = self.son.id_son
        ancien_ordre = son_DAO().get_ordre_son(id_son, son)
        son_DAO().supprimer_son(id_son, son)
        son_DAO().changer_ordre_son(id_son, ancien_ordre, False)

    def copier_son(self):

        id_son = self.son.id_son
        son_DAO().copier_son(id_son)
        # crée une son identique
        # avec id différent et utilisateur différent

    def ajouter_son_a_son(self, son, ordre):

        id_son = self.son.id_son
        son_DAO().changer_ordre_son(id_son, ordre, True)
        son_DAO().ajouter_son(id_son, son, ordre)

    def changer_nom_son(self, nouveau_nom):

        id_son = self.son.id_son
        son_DAO().modifier_nom_son(id_son, nouveau_nom)

    def jouer_son(self):

        n = len(self.son.list_son)
        for i in range(n):
            son = self.son.list_son[i][0]
            SonService().telecharger_son(son.id_son)

        for j in range(n):
            for i in range(n):
                if self.son.list_son[i][1] == j:
                    son = self.son.list_son[i][0]
                    SonService().jouer_son(son.id_son)
