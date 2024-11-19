from Object.playlist import Playlist
from DAO.playlist_DAO import Playlist_DAO
from Object.son import Son
from view.session import Session
from Service.SonService import SonService
from Api_FreeSound import apifreesound


class PlaylistService:
    """
    Service qui gère les opérations liées aux playlists, incluant la création, la modification,
    la suppression et l'ajout de sons dans une playlist.
    """

    def creer_playlist(self, nom_playlist: str, list_son: list(list()) = []):
        """
        Crée une nouvelle playlist avec un nom et une liste de sons spécifiés.

        Parameters
        ----------
        nom_playlist : str
            Le nom de la playlist à créer.
        list_son : list, optional
            Liste des sons à ajouter à la playlist (par défaut une liste vide).
        """

        utilisateur = Session().utilisateur
        playlist = Playlist(utilisateur, None, nom_playlist, list_son)
        Session().playlist = Playlist_DAO().ajouter_playlist(playlist)

    def supprimer_playlist(self):
        """
        Supprime la playlist actuelle de la session.
        """

        playlist = Session().playlist
        if Playlist_DAO().supprimer_playlist(playlist):
            Session().playlist = None

    def modifier_nom_playlist(self, nouveau_nom):
        """
        Modifie le nom de la playlist actuelle.

        Parameters
        ----------
        nouveau_nom : str
            Le nouveau nom de la playlist.
        """

        playlist_a_modif = Session().playlist
        Session().playlist.nom_playlist = nouveau_nom

        Playlist_DAO().modifier_nom_playlist(playlist_a_modif, nouveau_nom)

    def changer_ordre_son(self, son: Son, ordre: int):
        """
        Change l'ordre d'un son dans la playlist.

        Parameters
        ----------
        son : Son
            Le son dont l'ordre doit être modifié.
        ordre : int
            Le nouvel ordre du son dans la playlist.
        """

        playlist = Session().playlist

        playlist.changer_ordre(son, ordre)

        Session().playlist = playlist

        return Playlist_DAO().changer_ordre(playlist, son, ordre)

    def retirer_son_playlist(self, son: Son):
        """
        Retire un son de la playlist actuelle.

        Parameters
        ----------
        son : Son
            Le son à retirer de la playlist.
        """

        playlist = Session().playlist
        Playlist_DAO().supprimer_son(playlist, son)
        playlist.supprimer_son(son)
        Session().playlist = playlist

    def copier_playlist(self):
        """
        Crée une copie de la playlist actuelle.

        La nouvelle playlist est ajoutée directement à la session de l'utilisateur.
        """

        playlist = Session().playlist
        self.creer_playlist(playlist.nom_playlist, playlist.list_son)

    def ajouter_son_a_playlist(self, son, ordre):
        """
        Ajoute un son à la playlist avec un ordre spécifié.

        Parameters
        ----------
        son : Son
            Le son à ajouter à la playlist.
        ordre : int
            L'ordre du son dans la playlist.
        """

        playlist = Session().playlist
        Playlist_DAO().ajouter_son(playlist, son, ordre)
        # playlist.ajouter_son_playlist(son, ordre)
        Session().playlist = playlist

    def play_playlist(self, canal=1):
        """
        Joue les sons de la playlist dans l'ordre spécifié.

        Parameters
        ----------
        canal : int, optional
            Le canal sur lequel la playlist sera jouée (par défaut le canal 1).
        """

        playlist = Session().playlist.list_son
        playlist_ordonnee = sorted(playlist.list_son, key=lambda x: x[1])
        for son, _ in playlist_ordonnee:
            Session().son = son
            SonService().play_channel(son, canal)

    def play_next_son(self):
        # Recuperer les infos session
        son = Session().son
        playlist = Session().playlist

        # Trier et recuperer l'indice du son en cours pour itérer dessus
        playlist_ordonnee = sorted(playlist.list_son, key=lambda x: x[1])
        indice_son = next(
            (i for i, s in enumerate(playlist_ordonnee) if s[0] == son), None
        )
        for son, _ in playlist_ordonnee[indice_son:]:
            Session().son = son
            SonService().play_channel(son)

    def afficher_playlist(self):
        """
        Affiche toutes les playlists de l'utilisateur connecté.

        Returns
        -------
        list
            Liste des playlists de l'utilisateur connecté.
        """

        utilisateur = Session().utilisateur
        liste_playlist = Playlist_DAO().get_all_playlists_by_user(utilisateur)
        return liste_playlist

    def afficher_playlist_tous(self):

        liste_playlist = Playlist_DAO().get_all_playlists()
        return liste_playlist
