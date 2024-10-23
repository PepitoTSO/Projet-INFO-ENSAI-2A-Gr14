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
        print("Bonjour et bienvenu sur notre application ! \n"
              "Vous pouvez vous connecter ou créer un compte pour accéder à nos services. \n"
              "Cette application a été créée dans le but de vous aider à créer une ambiance pour vos parties de jeux de rôles. \n"
              "Vous pouvez ajouter des sons à votre playlist et les jouer en boucle ou les arrêter à tout moment afin de permettre une immersion totale des joueurs. \n"
              "Vous pouvez aussi créer des playlists personnalisées pour chaque partie. \n"
              "N'hésitez pas à nous contacter pour toute question ou suggestion. \n"
              "Merci de votre confiance et bonne partie !")
        #ou mettre une variable texte dans autre fichier et faire un formater pour unifier tous les textes

