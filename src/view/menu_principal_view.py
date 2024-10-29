from InquirerPy import inquirer

from View.abstract_view import AbstractView
from View.session import Session

from Service.UtilisateurService import UtilisateurService


class MenuView(AbstractView):
    """Vue du menu de l'utilisateur

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
                "Rechercher un son",
                "Gérer mes Sons",
                "Gérer mes Playlists",
                "Infos",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from View.accueil.accueil_view import AccueilView

                return AccueilView()

            case "Rechercher un son":
                from View.recherche_son_view import RechSonView

                return RechSonView()

            case "Gérer mes Sons":
                from View.son_view import SonView

                return SonView()

            case "Gérer mes Playlists":
                from View.playlist_view import PlaylistView

                return PlaylistView()

            case "Infos":
                MenuView.messageInfoMenu()

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
