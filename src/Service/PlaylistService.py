from Object.playlist import Playlist
from DAO.playlist_DAO import Playlist_DAO
from Object.son import Son
from Service.SonService import SonService
from Api_FreeSound import apifreesound


class PlaylistService:

    def __init__(self, playlist: Playlist):
        if not isinstance(playlist, Playlist):
            raise TypeError("La playlist n'est pas type Playlist.")

        self.playlist = playlist

    def creer_playlist(self):
        Playlist_DAO().creer_playlist(self.playlist.nom_playlist)

    def supprimer_playlist(self):
        Playlist_DAO().supprimer_playlist(self.playlist.id_playlist)

    def modifier_nom_playlist(self, nouveau_nom: str):
        if not isinstance(nouveau_nom, str):
            raise TypeError("Le nom doit être de type str.")

        Playlist_DAO().modifier_nom_playlist(self.playlist.id_playlist, nouveau_nom)

    def changer_ordre_son(self, son: Son, ordre: int):

        id_playlist = self.playlist.id_playlist
        ancien_ordre = Playlist_DAO().get_ordre_son(id_playlist, son)
        Playlist_DAO().supprimer_son(id_playlist, son)
        Playlist_DAO().changer_ordre_son(id_playlist, ancien_ordre, False)
        Playlist_DAO().changer_ordre_son(id_playlist, ordre, True)
        Playlist_DAO().ajouter_son(id_playlist, son, ordre)

    def retirer_son_playlist(self, son: Son):

        id_playlist = self.playlist.id_playlist
        ancien_ordre = Playlist_DAO().get_ordre_son(id_playlist, son)
        Playlist_DAO().supprimer_son(id_playlist, son)
        Playlist_DAO().changer_ordre_son(id_playlist, ancien_ordre, False)

    def copier_playlist(self):

        id_playlist = self.playlist.id_playlist
        Playlist_DAO().copier_playlist(id_playlist)
        # crée une playlist identique
        # avec id différent et utilisateur différent

    def ajouter_son_a_playlist(self, son, ordre):

        id_playlist = self.playlist.id_playlist
        Playlist_DAO().changer_ordre_son(id_playlist, ordre, True)
        Playlist_DAO().ajouter_son(id_playlist, son, ordre)



    def jouer_playlist(self):

        n = len(self.playlist.list_son)
        api=apifreesound() # Merlin a modifié ici et après
        for i in range(n):
            son = self.playlist.list_son[i][0]
            api.dl_son(son.id_son)

        for j in range(n):
            for i in range(n):
                if self.playlist.list_son[i][1] == j:
                    son = self.playlist.list_son[i][0]
                    son_a_jouer=SonService(son)
                    son_a_jouer.play()

