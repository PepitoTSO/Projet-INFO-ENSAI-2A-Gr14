'''
A faire
Pour l'instant c'est juste pour etre coherent avec les diagrammes etc
'''

from InquirerPy import prompt

from view.abstract_view import AbstractView


class ConnectionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "pas encore fait",
                "choices": [
                    "pas le choix"
                ]
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "pas le choix":

            from view.menu_principal import MenuView

            return MenuView()
