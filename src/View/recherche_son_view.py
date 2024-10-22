
from InquirerPy import prompt
from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Api_FreeSound.apifreesound import apifreesound


class RechSonView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Menu Recherche Son",
                "choices": [
                    "Recherche classique",
                    "Recherche avancée",
                    "Télécharger",
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

        elif reponse["choix"] == "Recherche classique":
            inquirer_recherche = {
                "type": "input",
                "message": "Quel est l'objet de votre recherche ?",
                "name": "Recherche"
            }

            recherche = prompt([inquirer_recherche])

            api=apifreesound()
            resultat = api.recherche_son(recherche['Recherche'])
            print(resultat)

            return RechSonView()

        elif reponse["choix"] == "Recherche avancée":  # A implementer
            return RechSonView()

        elif reponse["choix"] == "Télécharger":
            inquirer_id = {
                "type": "input",
                "message": "Quel est l'id du son?",
                "name": "id"
            }

            inq_id = prompt([inquirer_id])
            api=apifreesound()
            api.dl_son(int(inq_id['id']))

            return RechSonView()
