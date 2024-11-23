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
                "Play",
                "Prochain son",
                "Stop tout sauf la playlist en cours",
                "Aller aux sons",
                "Aller aux playlists",
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

            case "Aller aux sons":
                from view.son_view import SonView

                return SonView()

            case "Aller aux playlists":
                from view.playlist_view import PlaylistView

                return PlaylistView()

            case "Pause":
                son_service.pause(0)
                return JouerSonView()

            case "Play":
                son_service.pause(1)
                return JouerSonView()

            case "Prochain son":
                son_service.stop()
                return JouerSonView()

            case "Stop tout sauf la playlist en cours":
                son_service.stop_sauf_plist()
                return JouerSonView()
