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

        Session().playlist = lire_playlist
        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Lancer la playlist depuis le début",
                "Jouer un son de la playlist",
                "Jouer un son en boucle",
                "Jouer un autre son en simultané",
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
                from view.playlist_view import PlaylistView

                return PlaylistView()

            case "Lancer la playlist depuis le début":
                playlist_service.play_playlist(lire_playlist)
                premier_son = lire_playlist[0]
                son_service = SonService()
                son_service.play(premier_son)
                Session().playlist = None
                from view.jouer_son_view import JouerSonView

                return JouerSonView()

            case "Jouer un son de la playlist":
                lire_son = inquirer.select(
                    message="Choisissez un son : ",
                    choices=lire_playlist,
                ).execute()

                Session().son = lire_son
                son_service = SonService()
                son_service.play(lire_son)
                from view.jouer_son_view import JouerSonView

                return JouerSonView

            case "Jouer un son en boucle":
                lire_son = inquirer.select(
                    message="Choisissez un son : ",
                    choices=lire_playlist,
                ).execute()

                Session().son = lire_son
                son_service = SonService()
                son_service.jouer_en_boucle(lire_son)
                from view.jouer_son_view import JouerSonView

                return JouerSonView

            case "Jouer un autre son en simultané":
                lire_son = inquirer.select(
                    message="Choisissez une son : ",
                    choices=lire_playlist,
                ).execute()

                Session().son = lire_son
                son_service = SonService()
                son_service.play_multiple_sounds(lire_son)
                from view.jouer_son_view import JouerSonView

                return JouerSonView()
