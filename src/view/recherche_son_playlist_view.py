from InquirerPy import prompt
from InquirerPy import inquirer

from view.abstract_view import AbstractView
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
                "Rechercher une playlist",
                # "Recherche avancée",
                # "Télécharger",
                "Revenir au menu principal",
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

            # elif reponse["choix"] == "Recherche classique":
            # inquirer_recherche = {
            # "type": "input",
            # "message": "Que recherchez-vous ?",
            # "name": "Recherche",
            # }

            # recherche = prompt([inquirer_recherche])

            case "Rechercher une playlist":
                recherche_playlist = inquirer.text(
                    message="Quel type de playlist recherchez-vous ? : "
                ).execute()

                api = apifreesound()
                resultat = api.recherche_son(
                    recherche_playlist
                )  # Remplacer recherche_son par un vrai recherche_playlist
                print(resultat)

                return RechSonPlaylistView()

        # elif reponse["choix"] == "Recherche avancée":  # A implementer
        # return RechSonView()

        # elif reponse["choix"] == "Télécharger":
        # inquirer_id = {
        # "type": "input",
        # "message": "Quel est l'id du son?",
        # "name": "id",
        # }

        # inq_id = prompt([inquirer_id])
        # api = apifreesound()
        # api.dl_son(int(inq_id["id"]))

        # et ajouter à la bdd

        # return RechSonView()
