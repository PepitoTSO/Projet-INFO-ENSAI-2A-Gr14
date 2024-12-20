from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator
from view.abstract_view import AbstractView
from Service.UtilisateurService import UtilisateurService


class InscriptionView(AbstractView):
    """
    Vue du menu d'inscription d'un utilisateur
    """

    async def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Inscription\n" + "-" * 50 + "\n")

        # Demande à l'utilisateur de saisir pseudo, mot de passe...
        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()

        mdp = inquirer.secret(
            message="Entrez votre mot de passe : ",
            validate=PasswordValidator(
                length=8,
                cap=True,
                number=True,
                message="Au moins 8 caractères, incluant une majuscule et un chiffre",
            ),
        ).execute()

        # Appel du service pour créer l'utilisateur
        utilisateur_service = UtilisateurService()
        utilisateur = utilisateur_service.creer_utilisateur(
            mdp_nh=mdp, pseudo_utilisateur=pseudo
        )

        # Si l'utilisateur a été créé
        if utilisateur:
            message = f"Votre compte {pseudo} a été créé. Vous pouvez maintenant vous connecter."
        else:
            message = "Erreur d'inscription (pseudo ou mot de passe invalide)"

        from view.accueil.accueil_view import AccueilView

        return AccueilView(message)
