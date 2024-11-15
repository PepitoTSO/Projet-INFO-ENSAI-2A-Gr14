from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

from Api_FreeSound.apifreesound import apifreesound
from Service.SonService import SonService
from Object.son import Son

from .recom.recherche_avancee import n_mots_similaires


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
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().utilisateur = None

                from view.accueil.accueil_view import AccueilView

                return AccueilView("Bienvenue")

            case "Revenir au menu principal":

                from view.menu_principal_view import MenuView

                return MenuView()

            case "Rechercher un son":
                recherche_son = inquirer.text(
                    message="Quel type de son recherchez-vous ? : "
                ).execute()

                resultat = apifreesound().recherche_son(recherche_son)

                souschoix = inquirer.select(
                    message="Faites votre choix : ",
                    choices=[
                        "Telecharger son",
                        "Algo de recommandation",
                        "Revenir au menu",
                    ],
                ).execute()
                match souschoix:
                    case "Algo de recommandation":
                        # La partie recommendation
                        recom = n_mots_similaires(recherche_son)
                        liste_recom = [i[0] for i in recom]
                        liste_choix_recom = [recherche_son] + liste_recom
                        choix_recom_inq = inquirer.select(
                            message="Nous vous conseillons d'essayer avec:",
                            choices=liste_choix_recom,
                        ).execute()
                        resultat = apifreesound().recherche_son(choix_recom_inq)

                        # La partie dl
                        liste_choix_nom = [i["name"] for i in resultat]

                        choix_dl_inq = inquirer.select(
                            message="Quel son voulez-vous télécharger?",
                            choices=liste_choix_nom,
                        ).execute()

                        obj_son = next(
                            i for i in resultat if i["name"] == choix_dl_inq
                        )  # match le nom avec l'objet pour le dl, next permet de stopper des que trouve

                        apifreesound().dl_son(int(obj_son["id"]))

                        son = Son(
                            id_son=obj_son["id"],
                            nom=obj_son["name"],
                            tags=obj_son["tags"],
                        )
                        SonService().ajouter_son(son)

                        return RechSonPlaylistView()

                    case "Telecharger son":

                        liste_choix_nom = [i["name"] for i in resultat]

                        choix_dl_inq = inquirer.select(
                            message="Quel son voulez-vous télécharger?",
                            choices=liste_choix_nom,
                        ).execute()

                        obj_son = next(
                            i for i in resultat if i["name"] == choix_dl_inq
                        )  # match le nom avec l'objet pour le dl, next permet de stopper des que trouve

                        apifreesound().dl_son(int(obj_son["id"]))

                        son = Son(
                            id_son=obj_son["id"],
                            nom=obj_son["name"],
                            tags=obj_son["tags"],
                        )
                        SonService().ajouter_son(son)

                        return RechSonPlaylistView()

                    case "Revenir au menu":
                        return RechSonPlaylistView()
