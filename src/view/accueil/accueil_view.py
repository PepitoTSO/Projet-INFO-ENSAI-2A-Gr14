from InquirerPy import inquirer
from view.abstract_view import AbstractView


class AccueilView(AbstractView):
    """
    Vue de l'accueil de l'application
    """

    def __init__(self, message):
        super().__init__(message)

    async def choisir_menu(self):
        with open("src/dessin/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

        print("\n" + "-" * 50 + "\nAccueil\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Se connecter",
                "Créer un compte",
                "Infos sur l'application",
                "Quitter l'application",
            ],
        ).execute()

        match choix:
            case "Quitter l'application":
                pass

            case "Se connecter":
                from view.accueil.connexion_view import ConnexionView

                return ConnexionView("Connexion à l'application")

            case "Créer un compte":
                from view.accueil.inscription_view import InscriptionView

                return InscriptionView("Création de compte joueur")

            case "Infos sur l'application":
                accueil = AccueilView("Bienvenue")
                accueil.messageInfo()

                return accueil

    def messageInfo(self):
        print(
            "Bonjour et bienvenue sur notre application ! \n"
            "Vous pouvez vous connecter ou créer un compte pour accéder à nos services. \n"
            "Cette application a été créée dans le but de vous aider à créer une ambiance pour vos parties de jeux "
            "de rôles. \n"
            "Vous pouvez ajouter des sons à votre playlist et les jouer en boucle ou les arrêter à tout moment afin de "
            "permettre une immersion totale des joueurs. \n"
            "Vous pouvez aussi créer des playlists personnalisées pour chaque partie. \n"
            "N'hésitez pas à nous contacter pour toute question ou suggestion. \n"
            "Merci de votre confiance et bonne partie !"
        )
