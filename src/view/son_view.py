"""
A relier aux fonctions de son service parce que ça marche mieux
"""

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

        elif reponse["choix"] == "Supprimer son":

            return SonView()

        elif reponse["choix"] == "Jouer son":
            inquirer_id = {
                "type": "input",
                "message": "Quel est l'id du son?",
                "name": "id",
            }
            inq_id = prompt([inquirer_id])
            # DAO recherche par id  avec l'id du son
            # renvoie les infos pour créer un objet son

            from Object.son import Son

            son_a_jouer = Son(id_son=int(inq_id["id"]))
            from Service.SonService import SonService

            SonService_a_jouer = SonService(son_a_jouer)

            SonService_a_jouer.jouer_son()
            return SonView()
        elif reponse["choix"] == "Ajouter son":

            return SonView()
