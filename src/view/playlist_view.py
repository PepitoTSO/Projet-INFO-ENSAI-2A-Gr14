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
                "Revenir au menu précédent",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_view import AccueilView

                return AccueilView("Déconnexion réussie")

            case "Revenir au menu précédent":
                from view.menu_principal_view import MenuView

                return MenuView()

            case "Jouer une playlist":
                from view.jouer_playlist_view import JouerPlaylistView

                return JouerPlaylistView()

            case "Modifier une playlist":
                from view.modif_playlist_view import ModifPlaylistView

                return ModifPlaylistView()

            case "Créer une playlist":
                nom_playlist = inquirer.text(
                    message="Nommez votre playlist : "
                ).execute()
                playlist_service = PlaylistService()
                playlist_service.creer_playlist(nom_playlist)
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
                Session().playlist = modifier_playlist
                playlist_service.supprimer_playlist()
                print("Playlist supprimée")
                Session().playlist = None
                return PlaylistView()

            case "Copier une playlist":
                plist_tous = PlaylistService().afficher_playlist_tous()
                plist_tous.append("Retour au menu précédent")

                copier_plist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=plist_tous,
                ).execute()
                if copier_plist == "Retour au menu précédent":
                    return PlaylistView()
                # maj session avec plist selectionnee
                Session().playlist = copier_plist
                PlaylistService().copier_playlist()

                return PlaylistView()
