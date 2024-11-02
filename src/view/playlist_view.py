from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

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
                from view.accueil.accueil_view import AccueilView

                return AccueilView()

            case "Revenir au menu":
                from view.menu_principal_view import MenuView

                return MenuView()

            case "Lancer une playlist":
                #Comment demander à l'utilisateur quelle playlist il veut écouter ?
                #Y'a pas get_playlist_by_user ?
                Utilisateur = Utilisateur()

                playlists = utilisateur(list_playlist)
                playlists.append("Retour au Menu Principal")

                choix = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()

                if choix == "Retour au Menu Joueur":
                    from view.menu_principal_view import MenuView

                    return MenuView()

                from Service.PlaylistService import PlaylistService

                PlaylistService().jouer_playlist()

            case "Créer une playlist":
                nom_playlist = inquirer.text(message="Nommez votre playlist : ").execute()
                from Service.PlaylistService import PlaylistService

                PlaylistService().creer_playlist(nom_playlist)

            case "Modifier une playlist":
                from view.modif_playlist_view import ModifPlaylistView

                return ModifPlaylistView

            case "Supprimer une playlist":
                Utilisateur = Utilisateur()

                playlists = utilisateur(list_playlist)
                playlists.append("Retour au Menu Principal")

                choix = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()

                if choix == "Retour au Menu Joueur":
                    from view.menu_principal_view import MenuView

                    return MenuView()

                from Service.PlaylistService import PlaylistService

                PlaylistService().supprimer_playlist()
                from view.menu_principal_view import MenuView
                
                return MenuView()
