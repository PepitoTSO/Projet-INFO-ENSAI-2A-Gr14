from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Service.PlaylistService import PlaylistService
from Service.SonService import SonService


class JouerPlaylistView(AbstractView):
    """
    Vue du menu de la lecture des playlists
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Lecture des Playlists\n" + "-" * 50 + "\n")

        playlist_service = PlaylistService()

        playlists = playlist_service.afficher_playlist()

        lire_playlist = inquirer.select(
            message="Choisissez une playlist : ",
            choices=playlists,
        ).execute()

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Lancer la playlist depuis le début",
                # "Lancer la playlist depuis un son particulier",
                "Jouer un son",
                "Jouer en boucle un son",
                "Jouer un autre son en simultané",
                "Revenir au menu précédent",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_view import AccueilView

                return AccueilView()

            case "Revenir au menu précédent":
                from view.playlist_view import PlaylistView

                return PlaylistView()

            case "Lancer la playlist depuis le début":
                playlist_service.jouer_playlist(lire_playlist)
                return JouerPlaylistView()

            case "Jouer un son":
                lire_son = inquirer.select(
                    message="Choisissez un son : ",
                    choices=lire_playlist,
                ).execute()

                son_service = SonService()
                son_service.play(lire_son)
                return JouerPlaylistView

            case "Jouer un son en boucle":
                lire_son = inquirer.select(
                    message="Choisissez un son : ",
                    choices=lire_playlist,
                ).execute()

                son_service = SonService()
                son_service.jouer_en_boucle(lire_son)
                return JouerPlaylistView

            case "Jouer un autre son en simultané":
                lire_son_en_plus = inquirer.select(
                    message="Choisissez une son : ",
                    choices=lire_playlist,
                ).execute()

                son_service = SonService()
                son_service.play_multiple_sounds(lire_son_en_plus)
                return JouerPlaylistView
