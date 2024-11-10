#import regex

from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator, EmptyInputValidator

from prompt_toolkit.validation import ValidationError, Validator

from view.abstract_view import AbstractView
from Service.UtilisateurService import UtilisateurService


class InscriptionView(AbstractView):
    def choisir_menu(self):
        # Demande à l'utilisateur de saisir pseudo, mot de passe...
        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()

        # if JoueurService().pseudo_deja_utilise(pseudo):
        #    from view.accueil.accueil_vue import AccueilVue

        #    return AccueilVue(f"Le pseudo {pseudo} est déjà utilisé.")

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
        utilisateur = UtilisateurService.creer_utilisateur(
            mdp_nh=mdp, pseudo_utilisateur=pseudo
        )

        # Si l'utilisateur a été créé
        if utilisateur:
            message = f"Votre compte {pseudo} a été créé. Vous pouvez maintenant vous connecter."
        else:
            message = "Erreur de connexion (pseudo ou mot de passe invalide)"

        from view.accueil.accueil_view import AccueilView

        return AccueilView(message)
