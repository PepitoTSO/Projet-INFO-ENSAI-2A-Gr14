from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Service.SonService import SonService


class JouerSonView(AbstractView):
    """
    Vue du menu de la lecture des sons
    """

    async def choisir_menu(self):
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
                "Unpause",
                "Stop",
                "Stop tout sauf playlist",
                "Mute",
                "Volume +",
                "Volume -",
                "Revenir au menu principal",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_view import AccueilView

                return AccueilView("Déconnexion réussie")

            case "Revenir au menu principal":
                from view.menu_principal_view import MenuView

                return MenuView()

            case "Pause":
                # a faire
                son_service.pause_canal(8)
                return JouerSonView()

            case "Unpause":
                # a faire
                son_service.unpause()
                return JouerSonView()

            case "Stop":
                son_service.stop()
                return JouerSonView()

            case "Stop tout sauf playlist":
                son_service.stop_sauf_plist()
                return JouerSonView()

            case "Mute":
                if son_service.volume == 0:
                    son_service.unmute()
                else:
                    son_service.mute()
                return JouerSonView()

            case "Volume +":
                son_service.augmenter_volume()
                return JouerSonView()

            case "Volume -":
                son_service.diminuer_volume()
                return JouerSonView()
