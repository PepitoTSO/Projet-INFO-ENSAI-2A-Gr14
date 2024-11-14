from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Service.PlaylistService import PlaylistService
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

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Pause",
                "Unpause",
                "Avancer de 10 secondes",
                "Reculer de 10 secondes",
                "Jouer le prochain son",
                "Jouer le précédent son",
                "Revenir au menu précédent",
                "Se déconnecter",
            ],
        ).execute()
