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
        session = Session()

        if not session.playlist:
            self.choisir_playlist()

        print(f"Playlist selectionnée : {session.playlist.nom_playlist}\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Lancer la playlist depuis le début",
                "Jouer un son de la playlist",
                "Jouer un son de la playlist aléatoirement",
                "Jouer un son de la playlist pendant x secondes",
                "Changer de playlist",
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
                playlist = session.playlist.list_son
                if playlist is None:
                    print("Aucune playlist n'est chargée dans la session.")
                    return JouerPlaylistView()

                asyncio.create_task(playlist_service.play_playlist())
                print("Fin Lecture playlist")
                from view.jouer_son_view import JouerSonView

                return JouerSonView()

            case "Jouer un son de la playlist":
                son_choisi = self.choisir_son()

                asyncio.create_task(son_service.play_canal(son_choisi))

                from view.jouer_son_view import JouerSonView

                return JouerSonView()

            case "Jouer un son de la playlist aléatoirement":
                son_choisi = self.choisir_son()

                t = self.choisir_temps()

                t_min = inquirer.text(
                    message="Entrez la valeur de t_min :",
                    validate=lambda x: x.isdigit()
                    or "Veuillez entrer un nombre valide.",
                    transformer=lambda x: int(x),
                ).execute()

                t_max = inquirer.text(
                    message="Entrez la valeur de t_max (doit être supérieur à t_min) :",
                    validate=lambda x: x.isdigit()
                    and int(x) > int(t_min)
                    or "Veuillez entrer un nombre supérieur à t_min.",
                    transformer=lambda x: int(x),
                ).execute()

                asyncio.create_task(
                    son_service.jouer_aleatoire(
                        son_choisi, int(t_min), int(t_max), int(t)
                    )
                )

                from view.jouer_son_view import JouerSonView

                return JouerSonView()

            case "Jouer un son de la playlist pendant x secondes":
                son_choisi = self.choisir_son()
                t = self.choisir_temps()
                asyncio.create_task(son_service.play_canal(son_choisi, int(t)))

                from view.jouer_son_view import JouerSonView

                return JouerSonView()

            case "Changer de playlist":
                self.choisir_playlist()
                return JouerPlaylistView()

    def choisir_playlist(self):
        playlists = PlaylistService().afficher_playlist()
        lire_playlist = inquirer.select(
            message="Choisissez une playlist : ",
            choices=playlists,
        ).execute()
        Session().playlist = lire_playlist

    def choisir_son(self):
        lire_son = Session().playlist.list_son
        sons_dans_plist = [liste_sons[0] for liste_sons in lire_son]
        son = inquirer.select(
            message="Choisissez un son : ",
            choices=sons_dans_plist,
        ).execute()
        return son

    def choisir_temps(self):
        t = inquirer.text(
            message="Entrez le temps de lecture:",
            validate=lambda x: x.isdigit(),
            transformer=lambda x: int(x),
        ).execute()
        return t
