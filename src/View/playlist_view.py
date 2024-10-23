'''
A relier aux fonctions de playlistservice
'''


from InquirerPy import prompt

from view.abstract_view import AbstractView

from Service.PlaylistService import PlaylistService


class PlaylistView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Menu playlist",  # lister les playlist dispo pour l'utilisateur à l'apparition du menu?
                "choices": [
                    "Ajouter playlist",
                    "Modifier playlist",
                    "Supprimer playlist",
                    "Jouer playlist",
                    "Revenir au menu",
                ],
            }
        ]

    def display_info(self):
        with open("src/dessin/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Revenir au menu":
            from view.menu_principal import MenuView

            return MenuView()

        elif reponse["choix"] == "Modifier playlist":  # A implementer
            return PlaylistView()

        elif reponse["choix"] == "Supprimer playlist":

            return PlaylistView()

        elif reponse["choix"] == "Jouer playlist":

            return PlaylistView()
        elif reponse["choix"] == "Ajouter playlist":

            return PlaylistView()
