'''
A relier aux fonctions de playlistservice
'''


from InquirerPy import prompt

from view.abstract_view import AbstractView

from Service.PlaylistService import PlaylistService


class PlaylistView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Menu playlist",  # lister les playlist dispo pour l'utilisateur à l'apparition du menu?
                "choices": [
                    "Ajouter playlist",
                    "Modifier playlist",
                    "Supprimer playlist",
                    "Jouer playlist",
                    "Revenir au menu",
                ],
            }
        ]

    def display_info(self):
        with open("src/dessin/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Revenir au menu":
            from view.menu_principal import MenuView

            return MenuView()

        elif reponse["choix"] == "Modifier playlist":  # A implementer
            return PlaylistView()

        elif reponse["choix"] == "Supprimer playlist":

            return PlaylistView()

        elif reponse["choix"] == "Jouer playlist":

            return PlaylistView()
        elif reponse["choix"] == "Ajouter playlist":

            return PlaylistView()





from InquirerPy import inquirer

from View.abstract_view import AbstractView
from View.session import Session

from Object.utilisateur import Utilisateur
from Object.playlist import Playlist
from Service.PlaylistService import PlaylistService

class PlaylistView(AbstractView):
    """
    Vue du menu de la gestion des playlists
    """

 def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Playlist\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Lancer une playlist",
                "Créer une playlist",
                "Modifier une playlist",
                "Supprimer une playlist",
                "Revenir au menu",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from View.accueil.accueil_view import AccueilView

                return AccueilView()

            case "Revenir au menu":
                from View.menu_principal_view import MenuView

                return MenuView()

            case "Lancer une playlist":
                #Comment demander à l'utilisateur quelle playlist il veur écouter ?
                #Y'a pas get_playlist_by_user ?
                Utilisateur = Utilisateur()

                playlists = utilisateur(list_playlist)
                playlists.append("Retour au Menu Principal")

                choix = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()

                if choix == "Retour au Menu Joueur":
                    from View.menu_principal_view import MenuView

                    return MenuView()

                from Service.PlaylistService import PlaylistService

                PlaylistService().jouer_playlist()

            case "Créer une playlist":
                nom_playlist = inquirer.text(message="Nommez votre playlist : ").execute()
                from Service.PlaylistService import PlaylistService

                PlaylistService().creer_playlist(nom_playlist)

            case "Modifier une playlist":
                

