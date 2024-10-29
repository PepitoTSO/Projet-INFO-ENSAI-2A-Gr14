from InquirerPy import inquirer


class AccueilView(AbstractView):
    """Vue d'accueil de l'application"""

    def premier_menu(self):
        """
        Interface du premier menu
        """

    def display_info(self):
        with open("src/dessin/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

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
                from View.accueil.connexion_view import connexion

                return connexion_view("Connexion à l'application")

            case "Créer un compte":
                from View.accueil.inscription_view import InscriptionView

                return InscriptionView("Création de compte joueur")

            case "Infos sur l'appli":
                VueAccueil.messageInfo()

    def messageInfo(self):
        print(
            "Bonjour et bienvenu sur notre application ! \n"
            "Vous pouvez vous connecter ou créer un compte pour accéder à nos services. \n"
            "Cette application a été créée dans le but de vous aider à créer une ambiance pour vos parties de jeux de rôles. \n"
            "Vous pouvez ajouter des sons à votre playlist et les jouer en boucle ou les arrêter à tout moment afin de permettre une immersion totale des joueurs. \n"
            "Vous pouvez aussi créer des playlists personnalisées pour chaque partie. \n"
            "N'hésitez pas à nous contacter pour toute question ou suggestion. \n"
            "Merci de votre confiance et bonne partie !"
        )
        # ou mettre une variable texte dans autre fichier et faire un formater pour unifier tous les textes
