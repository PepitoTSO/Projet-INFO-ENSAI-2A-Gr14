"""
A faire
Pour l'instant c'est juste pour etre coherent avec les diagrammes etc
"""

from InquirerPy import prompt

from view.abstract_view import AbstractView


class ConnectionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "pas encore fait",
                "choices": ["pas le choix"],
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "pas le choix":

            from view.menu_principal import MenuView

            return MenuView()


from InquirerPy import inquirer

from View.abstract_view import AbstractView
from Viewiew.session import Session

from Service.UtilisateurService import UtilisateurService


class ConnexionView(AbstractView):
    """Vue de Connexion (saisie de pseudo et mdp)"""

    def choisir_menu(self):
        # Demande à l'utilisateur de saisir pseudo et mot de passe
        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()
        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()

        # Appel du service pour trouver l'utilisateur
        utilisateur = UtilisateurService.se_connecter(
            mdp_nh=mdp, pseudo_utilisateur=pseudo
        )

        # Si l'utilisateur a été trouvé à partir des ses identifiants de connexion
        if utilisateur:
            message = f"Vous êtes connecté sous le pseudo {joueur.pseudo}"
            Session().connexion(utilisateur)

            from View.menu_principal_view import MenuView

            return MenuView(message)

        message = "Erreur de connexion (pseudo ou mot de passe invalide)"
        from View.accueil.accueil_view import AccueilView

        return AccueilView(message)