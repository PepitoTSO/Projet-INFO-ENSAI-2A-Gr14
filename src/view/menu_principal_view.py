from InquirerPy import prompt

from view.abstract_view import AbstractView


class MenuView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Menu principal",
                "choices": [
                    "Rechercher son",
                    "Sons",
                    "Playlists",
                    "Infos",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        with open("src/dessin/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Rechercher son":
            from view.recherche_son_view import RechSonView

            return RechSonView()

        elif reponse["choix"] == "Sons":
            from view.son_view import SonView

            return SonView()

        elif reponse["choix"] == "Playlists":
            from view.playlist_view import PlaylistView

            return PlaylistView()

        elif reponse["choix"] == "Infos":

            info = """Bonjour et bienvenu sur notre application ! 
              Vous pouvez vous connecter ou créer un compte pour accéder à nos services. 
              Cette application a été créée dans le but de vous aider à créer une ambiance pour vos parties de jeux de rôles. 
              Vous pouvez ajouter des sons à votre playlist et les jouer en boucle ou les arrêter à tout moment afin de permettre une immersion totale des joueurs. 
              Vous pouvez aussi créer des playlists personnalisées pour chaque partie. 
              N'hésitez pas à nous contacter pour toute question ou suggestion. 
              Merci de votre confiance et bonne partie !"""  # C'est ici pour le texte des pourquoi et comment
            print(info)

            return MenuView()


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

        print("\n" + "-" * 50 + "\nMenu Utilisateur\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rechercher un son",
                "Sons",
                "Playlists",
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

            case "Afficher des pokemons (par appel à un Webservice)":
                from view.pokemon_vue import PokemonVue

                return PokemonVue()

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
