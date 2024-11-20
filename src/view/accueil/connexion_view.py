from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Service.UtilisateurService import UtilisateurService


class ConnexionView(AbstractView):
    """
    Vue du menu de connexion d'un utilisateur
    """

    async def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Connexion\n" + "-" * 50 + "\n")
        # Demande à l'utilisateur de saisir pseudo et mot de passe
        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()
        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()

        # Appel du service pour trouver l'utilisateur
        utilisateur_service = UtilisateurService()
        utilisateur = utilisateur_service.se_connecter(
            mdp_nh=mdp, pseudo_utilisateur=pseudo
        )

        # Si l'utilisateur a été trouvé à partir des ses identifiants de connexion
        if utilisateur is True:
            message1 = f"Vous êtes connecté sous le pseudo {pseudo}"

            from view.menu_principal_view import MenuView

            return MenuView(message1)

        message2 = "Erreur de connexion (pseudo ou mot de passe invalide)"
        from view.accueil.accueil_view import AccueilView

        return AccueilView(message2)
