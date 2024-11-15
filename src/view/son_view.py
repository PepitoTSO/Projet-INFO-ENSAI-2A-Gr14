from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session
from Api_FreeSound.apifreesound import apifreesound

from Service.SonService import SonService


class SonView(AbstractView):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Sons\n" + "-" * 50 + "\n")
        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Afficher tous mes sons",  # Manque une playlist avec tous les sons de l'utilisateur
                "Jouer un son",
                "Ajouter un son",
                "Supprimer un son",
                "Jouer en boucle un son",
                "Jouer en simultané un autre son",
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

            case "Jouer un son":
                from view.recherche_son_playlist_view import RechSonPlaylistView

                # rech = RechSonPlaylistView()
                # lire_son = inquirer.select(
                #   message="Choisissez un son : ",
                #    choices=rech.resultat,
                # ).execute()

                id_son = inquirer.text(message="Entrez l'id du son : ").execute()
                # DAO recherche par id  avec l'id du son
                # renvoie les infos pour créer un objet son
                api = apifreesound()
                dl_son_a_jouer = api.dl_son(int(id_son))

                from Object.son import Son

                son_a_jouer = Son(id_son=int(id_son))
                SonService_a_jouer = SonService()
                SonService_a_jouer.play(son_a_jouer)

                from view.jouer_son_view import JouerSonView

                return JouerSonView()

            case "Ajouter un son":
                id_son = inquirer.text(message="Entrez l'id du son : ").execute()
