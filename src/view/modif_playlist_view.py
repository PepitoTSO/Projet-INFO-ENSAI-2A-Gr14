from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Service.PlaylistService import PlaylistService
from Service.SonService import SonService


class ModifPlaylistView(AbstractView):
    """
    Vue du menu de la modification des playlists
    """

    async def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Modif\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Renommer une playlist",
                "Ajouter un son à une playlist",
                "Supprimer un son d'une playlist",
                "Changer l'ordre d'un son dans une playlist",
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

            case "Renommer une playlist":
                playlist_service = PlaylistService()
                playlists = playlist_service.afficher_playlist()
                playlists.append("Retour au menu précédent")

                modifier_playlist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()
                if modifier_playlist == "Retour au menu précédent":
                    return ModifPlaylistView()

                Session().playlist = modifier_playlist
                nouveau_nom_playlist = inquirer.text(
                    message="Quel est le nouveau nom de la playlist ? : "
                ).execute()

                playlist_service.modifier_nom_playlist(nouveau_nom_playlist)
                print(
                    f"La playlist {modifier_playlist} a été modifiée en {nouveau_nom_playlist}"
                )
                Session().playlist = None

                return ModifPlaylistView()

            case "Ajouter un son à une playlist":
                playlist_service = PlaylistService()
                playlists = playlist_service.afficher_playlist()
                playlists.append("Retour au menu précédent")

                modifier_playlist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()
                if modifier_playlist == "Retour au menu précédent":
                    return ModifPlaylistView()

                Session().playlist = modifier_playlist
                liste_sons = SonService().lister_son()
                ajout_son = inquirer.select(
                    message="Choisissez un son : ",
                    choices=liste_sons,
                ).execute()

                ordre = inquirer.text(
                    message="A quel ordre souhaitez-vous placer le son dans la playlist ? : "
                ).execute()

                playlist_service.ajouter_son_a_playlist(ajout_son, int(ordre))
                print(f"Le son {ajout_son.nom} a été ajouté avec succès.")
                Session().playlist = None
                Session().son = None
                return ModifPlaylistView()

            case "Supprimer un son d'une playlist":
                playlist_service = PlaylistService()
                playlists = playlist_service.afficher_playlist()
                playlists.append("Retour au menu précédent")

                modifier_playlist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()
                if modifier_playlist == "Retour au menu précédent":
                    return ModifPlaylistView()

                Session().playlist = modifier_playlist
                liste_son_plist = modifier_playlist.list_son
                sons_dans_plist = [liste_sons[0] for liste_sons in liste_son_plist]
                son_a_supprimer = inquirer.select(
                    message="Choisissez un son : ",
                    choices=sons_dans_plist,
                ).execute()

                playlist_service.retirer_son_playlist(son_a_supprimer)
                print(
                    f"Le son {son_a_supprimer.nom} a été supprimé de la playlist {modifier_playlist}"
                )
                Session().playlist = None
                return ModifPlaylistView()

            case "Changer l'ordre d'un son dans une playlist":
                playlist_service = PlaylistService()
                playlists = playlist_service.afficher_playlist()
                playlists.append("Retour au menu précédent")

                modifier_playlist = inquirer.select(
                    message="Choisissez une playlist : ",
                    choices=playlists,
                ).execute()
                if modifier_playlist == "Retour au menu précédent":
                    return ModifPlaylistView()

                Session().playlist = modifier_playlist
                liste_son_plist = modifier_playlist.list_son
                sons_dans_plist = [liste_sons[0] for liste_sons in liste_son_plist]
                son_a_ordonner = inquirer.select(
                    message="Choisissez un son : ",
                    choices=sons_dans_plist,
                ).execute()
                nouvel_ordre = inquirer.text(
                    message="A Quelle place voulez-vous que le son soit situé ? : "
                ).execute()

                res = playlist_service.changer_ordre_son(
                    son_a_ordonner, int(nouvel_ordre)
                )
                if res is True:
                    print(
                        f"Le son {son_a_ordonner.nom} a été déplacé en {nouvel_ordre}"
                    )
                else:
                    print("Erreur lors de la modification")
                Session().playlist = None
                return ModifPlaylistView()
