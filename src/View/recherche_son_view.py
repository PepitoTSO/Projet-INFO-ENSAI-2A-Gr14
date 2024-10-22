
from InquirerPy import prompt
from InquirerPy import Text

from view.abstract_view import AbstractView
from view.session import Session


class RechSonView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Recherche classique",
                    "Recherche avancée",
                    "Télécharger",
                    "Revenir au menu",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Revenir au menu":
            from view.menu_principal import MenuView
            
            return MenuView()

        elif reponse["choix"] == "Recherche classique":

            inquirer_recherche = [Text('Recherche', message="Quel est l'objet de votre recherche")]
            recherche = prompt(inquirer_recherche)
            
            from Api_FreeSound.apifreesound import apifreesound

            resultat = apifreesound.recherche_son(recherche)
            print(resultat)

            return RechSonView()

            

        elif reponse["choix"] == "Recherche avancée":
            from view.son_view import SonView

            return SonView()

        elif reponse["choix"] == "Télécharger":
            inquirer_dl = [Text('Recherche', message="Quel est l'id du son à télécharger")]
            id_dl = prompt(inquirer_dl)
            
            from Api_FreeSound.apifreesound import apifreesound

            resultat = apifreesound.dl_son(int(id_dl))
            print(resultat)

            return RechSonView()