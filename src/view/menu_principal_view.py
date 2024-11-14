from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session


class MenuView(AbstractView):
    """Vue du menu principal de l'utilisateur

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Principal\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rechercher un son/playlist",
                "Mes Sons",
                "Mes Playlists",
                "Infos",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().utilisateur = None
                from view.accueil.accueil_view import AccueilView

                return AccueilView()

            case "Rechercher un son/playlist":
                from view.recherche_son_playlist_view import RechSonPlaylistView

                return RechSonPlaylistView()

            case "Mes Sons":
                from view.son_view import SonView

                return SonView()

            case "Mes Playlists":
                from view.playlist_view import PlaylistView

                return PlaylistView()

            case "Infos":
                menu = MenuView()
                menu.messageInfoMenu()

                return MenuView()

    def messageInfoMenu(self):
        print(
            "Bonjour et bienvenu sur notre application ! \n"
            "Vous pouvez vous connecter ou créer un compte pour accéder à nos services. \n"
            "Cette application a été créée dans le but de vous aider à créer une ambiance pour vos parties de jeux de rôles. \n"
            "Vous pouvez ajouter des sons à votre playlist et les jouer en boucle ou les arrêter à tout moment afin de permettre une immersion totale des joueurs. \n"
            "Vous pouvez aussi créer des playlists personnalisées pour chaque partie. \n"
            "N'hésitez pas à nous contacter pour toute question ou suggestion. \n"
            "Merci de votre confiance et bonne partie !"
        )
