from src.Object.utilisateur import Utilisateur

class Playlist:

    def __init__(self, utilisateur : Utilisateur, id_playlist : int, nom_playlist, dict_son):
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_playlist, int):
            raise TypeError("L'id de la playlist doit être de type int.")
        
        self.__utilisateur = utilisateur
        self.__id_playlist = id_playlist
        self.__nom_playlist = nom_playlist
        self.__dict_son = dict_son
