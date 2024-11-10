from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Service.PlaylistService import PlaylistService


class JouerPlaylistView(AbstractView):
     """
    Vue du menu de la lecture des playlists
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Lecture\n" + "-" * 50 + "\n")

        playlist_service = PlaylistService()

        playlists = playlist_service.afficher_playlist()

        modifier_playlist = inquirer.select(
            message="Choisissez une playlist : ",
            choices=playlists,
        ).execute()

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Changer le nom de la playlist",
                "Ajouter un son à la playlist",
                "Supprimer un son de la playlist" "Changer l'ordre d'un son",
                "Revenir au menu précédent",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_view import AccueilView

                return AccueilView()

            case "Revenir au menu précédent":
                from view.playlist_view import PlaylistView

                return PlaylistView()


"Lancer la playlist depuis le début", playlist_service.jouer_playlist()
#"Lancer la playlist depuis un son particulier",
"Jouer un son",
"Jouer en boucle un son",
"Jouer un autre son en simultané",
"Ajouter un son",
"Supprimer un son",
"Revenir au menu précédent",
"Se déconnecter",