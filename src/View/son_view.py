'''
A relier aux fonctions de sonservice
'''


from InquirerPy import prompt

from view.abstract_view import AbstractView

from Service.SonService import SonService


class SonView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Menu son",  # lister les son dispo pour l'utilisateur à l'apparition du menu?
                "choices": [
                    "Ajouter son",
                    "Modifier son",
                    "Supprimer son",
                    "Jouer son",
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

        elif reponse["choix"] == "Modifier son":  # A implementer
            return SonView()

        elif reponse["choix"] == "Supprimer son":

            return SonView()

        elif reponse["choix"] == "Jouer son":

            return SonView()
        elif reponse["choix"] == "Ajouter son":

            return SonView()
