from InquirerPy import inquirer

from view.abstract_view import AbstractView
from view.session import Session

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
                "Afficher tous mes sons",
                "Jouer un son",
                "Ajouter un son",
                "Supprimer un son",
                "Jouer en boucle un son",
                "Jouer en simulatané un autre son",
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
                id_son = inquirer.text(message="Entrez l'id du son : ").execute()
                # DAO recherche par id  avec l'id du son
                # renvoie les infos pour créer un objet son

                from Object.son import Son

                son_a_jouer = Son(id_son=int(id_son))
                SonService_a_jouer = SonService(son_a_jouer)
                SonService_a_jouer.jouer_son()

                return SonView()

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Revenir au menu":
            from view.menu_principal import MenuView

            return MenuView()

        elif reponse["choix"] == "Supprimer son":

            return SonView()

        elif reponse["choix"] == "Jouer son":
            inquirer_id = {
                "type": "input",
                "message": "Quel est l'id du son?",
                "name": "id",
            }

        elif reponse["choix"] == "Ajouter son":

            return SonView()
