from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

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
                from view.jouer_playlist_view import JouerPlaylistView

                return JouerPlaylistView

            case "Modifier une playlist":
                playlist_service = PlaylistService()
                playlists = playlist_service.afficher_playlist()
                playlists.append("Retour au menu précédent")

                modifier_playlist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()

                if modifier_playlist == "Retour au menu précédent":
                    return PlaylistView()

                from view.modif_playlist_view import ModifPlaylistView

                return ModifPlaylistView

            case "Créer une playlist":
                nom_playlist = inquirer.text(
                    message="Nommez votre playlist : "
                ).execute()

                PlaylistService().creer_playlist(nom_playlist)
                return PlaylistView()

            case "Supprimer une playlist":
                playlist_service = PlaylistService()
                playlists = playlist_service.afficher_playlist()
                playlists.append("Retour au menu précédent")

                modifier_playlist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()

                if modifier_playlist == "Retour au menu précédent":
                    return PlaylistView()

                playlist_service.supprimer_playlist()
                from view.menu_principal_view import MenuView

                return MenuView()

            # case "Copier une playlist":
