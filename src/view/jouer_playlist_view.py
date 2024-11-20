from InquirerPy import inquirer
import asyncio
from view.abstract_view import AbstractView
from view.session import Session

from Service.PlaylistService import PlaylistService
from Service.SonService import SonService


class JouerPlaylistView(AbstractView):
    """
    Vue du menu de la lecture des playlists
    """

    async def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Lecture des Playlists\n" + "-" * 50 + "\n")

        playlist_service = PlaylistService()
        son_service = SonService()

        playlists = playlist_service.afficher_playlist()

        lire_playlist = inquirer.select(
            message="Choisissez une playlist : ",
            choices=playlists,
        ).execute()

        Session().playlist = lire_playlist
        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Lancer la playlist depuis le début",
                "Jouer un son de la playlist",
                "Jouer un son en boucle",
                "Jouer un autre son en simultané",
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

            case "Lancer la playlist depuis le début":
                # Le menu est ok, l'objet est ok,
                async def async_main_plist():
                    t1 = asyncio.create_task(playlist_service.play_playlist())
                    await t1

                asyncio.run(async_main_plist())
                print("Fin Lecture playlist")
                Session().playlist = None

                return JouerPlaylistView()

            case "Jouer un son de la playlist":
                lire_son = inquirer.select(
                    message="Choisissez un son : ",
                    choices=lire_playlist,
                ).execute()

                Session().playlist = lire_son
                liste_son_plist = lire_son.list_son
                sons_dans_plist = [liste_sons[0] for liste_sons in liste_son_plist]
                son_a_jouer = inquirer.select(
                    message="Choisissez un son : ",
                    choices=sons_dans_plist,
                ).execute()

                son_service.play(son_a_jouer)

                from view.jouer_son_view import JouerSonView

                return JouerSonView

            case "Jouer un son en boucle":
                lire_son = inquirer.select(
                    message="Choisissez un son : ",
                    choices=lire_playlist,
                ).execute()

                Session().son = lire_son
                son_service = SonService()
                son_service.jouer_en_boucle(lire_son)
                from view.jouer_son_view import JouerSonView

                return JouerSonView

            case "Jouer un autre son en simultané":
                lire_son = inquirer.select(
                    message="Choisissez une son : ",
                    choices=lire_playlist,
                ).execute()

                Session().son = lire_son
                son_service = SonService()
                son_service.play_multiple_sounds(lire_son)
                from view.jouer_son_view import JouerSonView

                return JouerSonView()
