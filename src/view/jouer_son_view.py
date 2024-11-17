from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Service.SonService import SonService


class JouerSonView(AbstractView):
    """
    Vue du menu de la lecture des sons
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Lecture des Sons\n" + "-" * 50 + "\n")

        son_service = SonService()

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Pause",
                "Play",
                "Avancer de 15 secondes",
                "Reculer de 15 secondes",
                # "Jouer le prochain son",
                # "Jouer le précédent son",
                "Revenir au menu précédent",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_view import AccueilView

                return AccueilView("Déconnexion réussie")

            case "Revenir au menu précédent":
                from view.menu_principal_view import MenuView

                return MenuView()

            case "Pause":
                son_service.pause()

            case "Play":
                son_service.unpause()

            case "Avancer de 15 secondes":
                son_service.avancer_xtemps(15)

            case "Reculer de 10 secondes":
                son_service.avancer_xtemps(-15)

            # case "Jouer le prochain son":
            #    playlist_service = PlaylistService()
            #    playlist_service.play_next_son() #La fonction n'est pas implémentée
