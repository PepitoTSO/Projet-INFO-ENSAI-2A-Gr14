from src.Object.utilisateur import Utilisateur

class Playlist:

    def __init__(self, utilisateur : Utilisateur, id_playlist : int, nom_playlist, dict_son):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_playlist, int):
            raise TypeError("L'id de la playlist doit être de type int.")
        if not isinstance(nom_playlist, str):
            raise TypeError("Le nom de la playlist doit être un str")
        if not isinstance(dict_son, list):
            raise TypeError("La liste de son doit être une liste.")

        self.utilisateur = utilisateur
        self.id_playlist = id_playlist
        self.nom_playlist = nom_playlist
        self.dict_son = dict_son

    def ajouter_son(self, son : Son, ordre : int):
        if not isinstance(ordre, int):
            raise TypeError("L'ordre doit être un int.")
        if not isinstance(son, Son):
            raise TypeError("son doit être un objet de classe Son.")

        for i in range(len(self.dict_son)):
            if self.dict_son[i][1] > ordre:
                self.dict_son[i][1] += 1

        self.dict_son.append([son, ordre])

        PlaylistService(self).ajouter_son_a_playlist(son)

    def supprimer_son(self, son : Son):
        for i in range(len(self.dict_son)):
            if self.dict_son[i][0] == son:
                ordre = self.dict_son[i][1]
                self.dict_son.pop(i)
        for i in range(len(self.dict_son)):
            if self.dict_son[i][1] > ordre:
                self.dict_son[i][1] += -1

        PlaylistService(self).retirer_son_de_playlist(son)

        service = PlaylistService(self).retirer_son_de_playlist(son : Son)

    def changer_ordre(self, son, ordre : int):

        for i in range(len[self.dict_son]):
            if self.dict_son[i][0] == son:
                ordre_ancien = self.dict_son[i][1]
                self.dict_son.pop(i)

        for i in range(len[self.dict_son]):
            if self.dict_son[i][1] > ordre_ancien:
                self.dict_son[i][1] += -1

        for i in range(len[self.dict_son]):
            if self.dict_son[i][1] >= ordre:
                self.dict_son[i][1] += 1

        self.dict_son.append([son, ordre])

        PlaylistService(self).changer_ordre_son(son, ordre)

    def changer_nom_playlist(self, nouveau_nom):
        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nouveau nom doit être un str.")

        self.nom_playlist = nouveau_nom

        PlaylistService(self).changer_nom_playlist(nouveau_nom)




