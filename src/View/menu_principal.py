from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Connection",
                    "Inscription"
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Connection":
            from view.connection_view import ConnectionView

            return ConnectionView()

        elif reponse["choix"] == "Inscription":
            from view.inscription_view import InscriptionView

            return InscriptionView()


class MenuView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
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
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
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

            info = 'texte a faire'   # C'est ici pour le texte des pourquoi et comment
            print(info)

            return MenuView()
