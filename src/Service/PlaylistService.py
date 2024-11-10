from Object.playlist import Playlist
from DAO.playlist_DAO import Playlist_DAO
from Object.son import Son
from view.session import Session
from Service.SonService import SonService
from Api_FreeSound import apifreesound


class PlaylistService:

    # Attention la session doit être modifiée dans la vue,
    # dès qu'il shoisit une playlist ça doit modifier session.Playlist
    # et dès qu'il quitte les menus où il a besoin d'une playlist ça
    # doit la remettre à None

    # ATTENTION CAS PARTICULIER quand on crée ou modifie une playlist, on met la playlist de session direct dedans

    def creer_playlist(self, nom_playlist: str, list_son: list(list()) = [[]]):

        utilisateur = Session().utilisateur

        playlist = Playlist(utilisateur, None, nom_playlist, list_son)
        Session().playlist = Playlist_DAO().ajouter_playlist(playlist)

    def supprimer_playlist(self):

        playlist = Session().playlist
        Playlist_DAO().supprimer_playlist(playlist)

    def modifier_nom_playlist(self, nouveau_nom):

        playlist_a_modif = Session().playlist
        Session().playlist.nom_playlist = nouveau_nom
        nouvelle_playlist = Session().playlist

        Playlist_DAO().modifier_nom_playlist(playlist_a_modif, nouvelle_playlist)

    def changer_ordre_son(self, son: Son, ordre: int):

        playlist = Session().playlist

        playlist.changer_ordre(son, ordre)

        Session().playlist = playlist.changer_ordre(son, ordre)

        Playlist_DAO().changer_ordre(playlist, son, ordre)

    def retirer_son_playlist(self, son: Son):

        playlist = Session().playlist
        playlist.retirer_son(son)
        Session().playlist = playlist

        Playlist_DAO().supprimer_son(playlist, son)
        playlist.retirer_son(son)
        Session().playlist = playlist

    def copier_playlist(self):
        playlist = Session().playlist
        self.creer_playlist(playlist.nom_playlist, playlist.list_son)

    def ajouter_son_a_playlist(self, son, ordre):
        playlist = Session().playlist
        Playlist_DAO().ajouter_son(playlist, son, ordre)
        playlist.ajouter_son_playlist(son, ordre)
        Session().playlist = playlist

    def jouer_playlist(self):

        n = len(self.playlist.list_son)
        api = apifreesound()  # Merlin a modifié ici et après
        for i in range(n):
            son = self.playlist.list_son[i][0]
            api.dl_son(son.id_son)

        for j in range(n):
            for i in range(n):
                if self.playlist.list_son[i][1] == j:
                    son = self.playlist.list_son[i][0]
                    son_a_jouer = SonService(son)
                    son_a_jouer.play()

    def afficher_playlist(self):
        utilisateur = Session().utilisateur
        liste_playlist = Playlist_DAO().get_all_playlists_by_user(utilisateur)
        return liste_playlist
        # je sais pas quoi faire

    # def __init__(self, playlist: Playlist):
    #     if not isinstance(playlist, Playlist):
    #         raise TypeError("La playlist n'est pas type Playlist.")

    #     self.playlist = playlist

    # def creer_playlist(self):
    #     Playlist_DAO().creer_playlist(self.playlist.nom_playlist)

    # def supprimer_playlist(self):
    #     Playlist_DAO().supprimer_playlist(self.playlist.id_playlist)

    # def modifier_nom_playlist(self, nouveau_nom: str):
    #     if not isinstance(nouveau_nom, str):
    #         raise TypeError("Le nom doit être de type str.")

    #     Playlist_DAO().modifier_nom_playlist(self.playlist.id_playlist, nouveau_nom)

    # def changer_ordre_son(self, son: Son, ordre: int):

    #     id_playlist = self.playlist.id_playlist
    #     ancien_ordre = Playlist_DAO().get_ordre_son(id_playlist, son)
    #     Playlist_DAO().supprimer_son(id_playlist, son)
    #     Playlist_DAO().changer_ordre_son(id_playlist, ancien_ordre, False)
    #     Playlist_DAO().changer_ordre_son(id_playlist, ordre, True)
    #     Playlist_DAO().ajouter_son(id_playlist, son, ordre)

    # def retirer_son_playlist(self, son: Son):

    #     id_playlist = self.playlist.id_playlist
    #     ancien_ordre = Playlist_DAO().get_ordre_son(id_playlist, son)
    #     Playlist_DAO().supprimer_son(id_playlist, son)
    #     Playlist_DAO().changer_ordre_son(id_playlist, ancien_ordre, False)

    # def copier_playlist(self):

    #     id_playlist = self.playlist.id_playlist
    #     Playlist_DAO().copier_playlist(id_playlist)
    #     # crée une playlist identique
    #     # avec id différent et utilisateur différent

    # def ajouter_son_a_playlist(self, son, ordre):

    #     id_playlist = self.playlist.id_playlist
    #     Playlist_DAO().changer_ordre_son(id_playlist, ordre, True)
    #     Playlist_DAO().ajouter_son(id_playlist, son, ordre)

    # def jouer_playlist(self):

    #     n = len(self.playlist.list_son)
    #     api = apifreesound()  # Merlin a modifié ici et après
    #     for i in range(n):
    #         son = self.playlist.list_son[i][0]
    #         api.dl_son(son.id_son)

    #     for j in range(n):
    #         for i in range(n):
    #             if self.playlist.list_son[i][1] == j:
    #                 son = self.playlist.list_son[i][0]
    #                 son_a_jouer = SonService(son)
    #                 son_a_jouer.play()
