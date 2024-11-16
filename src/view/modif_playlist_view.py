from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Service.PlaylistService import PlaylistService


class ModifPlaylistView(AbstractView):
    """
    Vue du menu de la modification des playlists
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Modif\n" + "-" * 50 + "\n")

        playlist_service = PlaylistService()
        playlists = playlist_service.afficher_playlist()

        modifier_playlist = inquirer.select(
            message="Choisissez une playlist : ",
            choices=playlists,
        ).execute()

        Session().playlist = modifier_playlist
        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Renommer la playlist",
                "Ajouter un son à la playlist",
                "Supprimer un son de la playlist",
                "Changer l'ordre d'un son dans la playlist",
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
                from view.playlist_view import PlaylistView

                return PlaylistView()

            case "Renommer la playlist":
                nouveau_nom_playlist = inquirer.text(
                    message="Quel est le nouveau nom de la playlist ? : "
                ).execute()

                modifier_playlist = playlist_service.modifier_nom_playlist(
                    nouveau_nom_playlist
                )
                Session().playlist = None
                from view.playlist_view import PlaylistView

                return PlaylistView

            case "Ajouter un son à la playlist":
                nouveau_son = inquirer.text(
                    message="Quel est le nouveau son à ajouter ? : "
                ).execute()
                ordre = inquirer.text(
                    message="A quel ordre souhaitez-vous placer le son dans la playlist ? : "
                ).execute()

                modifier_playlist = playlist_service.ajouter_son_a_playlist(
                    nouveau_son, ordre
                )
                Session().playlist = None
                from view.playlist_view import PlaylistView

                return PlaylistView

            case "Supprimer un son à la playlist":
                son_a_supprimer = inquirer.text(
                    message="Quel est le son à supprimer ? : "
                ).execute()

                Session().playlist
                modifier_playlist = playlist_service.retirer_son_playlist(
                    son_a_supprimer
                )
                Session().playlist = None
                from view.playlist_view import PlaylistView

                return PlaylistView

            case "Changer l'ordre d'un son dans la playlist":
                son_a_deplacer = inquirer.text(
                    message="Quel est le son à déplacer ? : "
                ).execute()
                nouvel_ordre = inquirer.text(
                    message="A Quelle place voulez-vous que le son soit situé ? : "
                ).execute()

                modifier_playlist = playlist_service.changer_ordre_son(
                    son_a_deplacer, nouvel_ordre
                )
                Session().playlist = None
                from view.playlist_view import PlaylistView

                return PlaylistView
