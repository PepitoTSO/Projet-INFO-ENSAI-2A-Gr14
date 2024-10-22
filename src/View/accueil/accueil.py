from InquirerPy import inquirer


class VueAccueil(VueAbstraite):
    """Vue d'accueil de l'application"""

    def premier_menu(self):
        """
        Interface du premier menu
        """

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
                from View.accueil.connexion import connexion

                return connexion("Connexion à l'application")

            case "Créer un compte":
                from interface.accueil.inscription import InscriptionVue

                return InscriptionVue("Création de compte joueur")

            case "Infos sur l'appli":
                VueAccueil.messageInfo()
    
    def messageInfo(self):
        print("")
        #ou mettre une variable texte dans autre fichier et faire un formater pour unifier tous les textes

