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

    def creer_playlist(self, nom_playlist: str, list_son: list(list()) = []):

        utilisateur = Session().utilisateur
        playlist = Playlist(utilisateur, None, nom_playlist, list_son)
        Session().playlist = Playlist_DAO().ajouter_playlist(playlist)

    def supprimer_playlist(self):

        playlist = Session().playlist
        if Playlist_DAO().supprimer_playlist(playlist):
            Session().playlist = None

    def modifier_nom_playlist(self, nouveau_nom):

        playlist_a_modif = Session().playlist
        Session().playlist.nom_playlist = nouveau_nom

        Playlist_DAO().modifier_nom_playlist(playlist_a_modif, nouveau_nom)

    def changer_ordre_son(self, son: Son, ordre: int):

        playlist = Session().playlist

        playlist.changer_ordre(son, ordre)

        Session().playlist = playlist

        Playlist_DAO().changer_ordre(playlist, son, ordre)

    def retirer_son_playlist(self, son: Son):

        playlist = Session().playlist
        Playlist_DAO().supprimer_son(playlist, son)
        playlist.supprimer_son(son)
        Session().playlist = playlist

    def copier_playlist(self):
        playlist = Session().playlist
        self.creer_playlist(playlist.nom_playlist, playlist.list_son)

    def ajouter_son_a_playlist(self, son, ordre):
        playlist = Session().playlist
        Playlist_DAO().ajouter_son(playlist, son, ordre)
        playlist.ajouter_son_playlist(son, ordre)
        Session().playlist = playlist

    def play_playlist(self, canal=1):
        playlist = Session().playlist
        playlist_ordonnee = sorted(playlist.list_son, key=lambda x: x[1])
        for son, _ in playlist_ordonnee:
            SonService().play_channel(son, canal)

    def play_next_son():  # il faut l'info sur le son en cours relativement à la playlist
        pass

    def afficher_playlist(self):
        utilisateur = Session().utilisateur
        liste_playlist = Playlist_DAO().get_all_playlists_by_user(utilisateur)
        return liste_playlist

    def afficher_playlist_tous(self):
        liste_playlist = Playlist_DAO().get_all_playlist()
        return liste_playlist
        # je sais pas quoi faire


if __name__ == "__main__":
    from Object.utilisateur import Utilisateur

    son_test = Son(1, path_stockage="./data/test.mp3")
    utilisateur = Utilisateur("user1", "hashed_password")
    p_test = Playlist(
        utilisateur,
        1,
        "My Playlist",
        [[son_test, 1]],
    )
    Session().utilisateur = utilisateur
    Session().playlist = p_test
    PlaylistService().play_playlist()
