from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Api_FreeSound.apifreesound import apifreesound
from Service.SonService import SonService
from Object.son import Son

from Api_FreeSound.recherche_avancee import recherche_avancee


class RechSonPlaylistView(AbstractView):
    """
    Vue du menu de la recherche des sons. Permet de telecharger et d'exploiter la recommendation
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
                "Revenir au menu précédent",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().utilisateur = None

                from view.accueil.accueil_view import AccueilView

                return AccueilView("Déconnexion réussie")

            case "Revenir au menu précédent":

                from view.menu_principal_view import MenuView

                return MenuView()

            case "Rechercher un son":
                recherche_son = inquirer.text(
                    message="Quel son recherchez-vous ? : "
                ).execute()

                resultat = apifreesound().recherche_son(recherche_son)

                souschoix = inquirer.select(
                    message="Faites votre choix : ",
                    choices=[
                        "Telecharger son",
                        "Recommandations",
                        "Revenir au menu",
                    ],
                ).execute()
                match souschoix:

                    case "Telecharger son":

                        liste_choix_nom = [i["name"] for i in resultat]

                        choix_dl_inq = inquirer.select(
                            message="Quel son voulez-vous télécharger?",
                            choices=liste_choix_nom,
                        ).execute()

                        # retourne le premier resultat associé au nom choisi l'objet pour le telecharger
                        obj_son = next(i for i in resultat if i["name"] == choix_dl_inq)

                        apifreesound().dl_son(int(obj_son["id"]))

                        # Initialise un son et l'ajoute a la bdd
                        son = Son(
                            id_son=obj_son["id"],
                            nom=obj_son["name"],
                            tags=obj_son["tags"],
                        )
                        SonService().ajouter_son(son)

                        ecouter = inquirer.confirm(
                            message="Voulez-vous ecouter (10s)?", default=True
                        ).execute()
                        if ecouter is True:
                            SonService().play(son, 10)

                        return RechSonPlaylistView()

                    case "Recommandations":
                        # La partie recommendation
                        recom = recherche_avancee().n_mots_similaires(recherche_son)
                        liste_recom = [i[0] for i in recom]
                        liste_choix_recom = [recherche_son] + liste_recom
                        choix_recom_inq = inquirer.select(
                            message="Nous vous conseillons d'essayer avec:",
                            choices=liste_choix_recom,
                        ).execute()
                        resultat = apifreesound().recherche_son(choix_recom_inq)

                        telecharger = inquirer.confirm(
                            message="Voulez-vous telecharger?", default=True
                        ).execute()
                        if telecharger is False:
                            return RechSonPlaylistView()

                        # La partie telecharger
                        liste_choix_nom = [i["name"] for i in resultat]

                        choix_dl_inq = inquirer.select(
                            message="Quel son voulez-vous télécharger?",
                            choices=liste_choix_nom,
                        ).execute()

                        # Retourne le premier resultat associé au nom choisi l'objet pour le telecharger
                        obj_son = next(i for i in resultat if i["name"] == choix_dl_inq)

                        apifreesound().dl_son(int(obj_son["id"]))

                        # Initialise un son et l'ajoute a la bdd
                        son = Son(
                            id_son=obj_son["id"],
                            nom=obj_son["name"],
                            tags=obj_son["tags"],
                        )
                        SonService().ajouter_son(son)
                        ecouter = inquirer.confirm(
                            message="Voulez-vous ecouter (10s)?", default=True
                        ).execute()
                        if ecouter is True:
                            SonService().play(son, 10)
                        return RechSonPlaylistView()

                    case "Revenir au menu":
                        return RechSonPlaylistView()
