from InquirerPy import inquirer


class VueAccueil(VueAbstraite):
    """Vue d'accueil de l'application"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "*" * 50 + "\nMenu de connexion\n" + "*" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Se connecter",
                "Créer un compte",
                "Infos sur l'appli",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Quitter":
                pass

            case "Se connecter":
                from interface.accueil.connexion import ConnexionVue

                return ConnexionVue("Connexion à l'application")

            case "Créer un compte":
                from interface.accueil.inscription import InscriptionVue

                return InscriptionVue("Création de compte joueur")

            case "Infos sur l'appli":
                VueAccueil.messageInfo()
    
    def messageInfo(self):
        print("message info a ecrire")
        #ou mettre une variable texte dans autre fichier et faire un formater pour unifier tous les textes

