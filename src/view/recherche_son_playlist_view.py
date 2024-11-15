from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.jouer_son_view import JouerSonView
from view.session import Session

from Api_FreeSound.apifreesound import apifreesound


class RechSonPlaylistView(AbstractView):
    """
    Vue du menu de la recherche des sons/playlists
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Recherche Sons/Playlists\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rechercher un son",
                # "Recherche avancée",
                "Revenir au menu principal",
                # "Telecharger son"
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_view import AccueilView

                return AccueilView()

            case "Revenir au menu principal":
                from view.menu_principal_view import MenuView

                return MenuView()

            case "Rechercher un son":
                recherche_son = inquirer.text(
                    message="Quel type de son recherchez-vous ? : "
                ).execute()

                api = apifreesound()
                resultat = api.recherche_son(recherche_son)
                print(resultat)

                souschoix = inquirer.select(
                    message="Faites votre choix : ",
                    choices=[
                        "Telecharger son",
                        "Revenir au menu",
                    ],
                ).execute()
                match souschoix:
                    case "Telecharger son":
                        dl_id = inquirer.text(
                            message="Quel id de son à télécharger ? : "
                        ).execute()
                        api = apifreesound()
                        api.dl_son(int(dl_id))
                        # ajouter son à bdd
                        # jouer le son?
                        #
                        return RechSonPlaylistView()

                    case "Revenir au menu":
                        return RechSonPlaylistView()

                # Faire une interface sur laquelle on peut selectionner le resultat de la liste et le telecharger
                # lire_son = inquirer.select(
                #    message="Choisissez un son : ",
                #    choices=resultat,
                # ).execute()
