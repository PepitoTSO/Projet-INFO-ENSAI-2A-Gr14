from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Object.utilisateur import Utilisateur
from Object.playlist import Playlist
from Service.PlaylistService import PlaylistService


class PlaylistView(AbstractView):
    """
    Vue du menu de la gestion des playlists
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Playlists\n" + "-" * 50 + "\n")

        playlist_service = PlaylistService()

        playlists = playlist_service.afficher_playlist()

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Jouer une playlist",
                "Modifier une playlist",
                "Créer une playlist",
                "Supprimer une playlist",
                "Copier une playlist",
                "Revenir au menu principal",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_view import AccueilView

                return AccueilView()

            case "Revenir au menu principal":
                from view.menu_principal_view import MenuView

                return MenuView()

            case "Jouer une playlist":
                playlists.append("Retour au Menu Principal")

                jouer_playlist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()

                if jouer_playlist == "Retour au Menu Joueur":
                    from view.menu_principal_view import MenuView

                    return MenuView()

                from view.jouer_playlist_view import JouerPlaylistView

                return JouerPlaylistView

            case "Modifier une playlist":
                playlists.append("Retour au Menu Principal")

                modifier_playlist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()

                if modifier_playlist == "Retour au Menu Joueur":
                    from view.menu_principal_view import MenuView

                    return MenuView()

                from view.modif_playlist_view import ModifPlaylistView

                return ModifPlaylistView

            case "Créer une playlist":
                nom_playlist = inquirer.text(
                    message="Nommez votre playlist : "
                ).execute()
                from Service.PlaylistService import PlaylistService

                PlaylistService().creer_playlist(nom_playlist)

            case "Supprimer une playlist":
                playlists.append("Retour au Menu Principal")

                choix = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()

                if choix == "Retour au Menu Joueur":
                    from view.menu_principal_view import MenuView

                    return MenuView()

                playlist_service.supprimer_playlist()
                from view.menu_principal_view import MenuView

                return MenuView()
