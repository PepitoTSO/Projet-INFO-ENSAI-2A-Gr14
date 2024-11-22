from InquirerPy import inquirer
import asyncio
from view.abstract_view import AbstractView
from view.session import Session
from Service.SonService import SonService


class SonView(AbstractView):
    async def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Sons\n" + "-" * 50 + "\n")
        son_service = SonService()
        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Afficher tous mes sons",
                "Jouer un son",
                "Jouer un son aléatoirement",
                "Jouer un son pendant x secondes",
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
                from view.menu_principal_view import MenuView

                return MenuView()

            case "Afficher tous mes sons":
                liste_sons = son_service.lister_son()
                for son in liste_sons:
                    print(son)
                    print("\n" + "-" * 50 + "\n")
                return SonView()

            case "Jouer un son":
                son_choisi = self.choisir_son()

                asyncio.create_task(son_service.play_canal(son_choisi))

                from view.jouer_son_view import JouerSonView

                return JouerSonView()

            case "Jouer un son aléatoirement":
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

            case "Jouer un son pendant x secondes":
                son_choisi = self.choisir_son()
                t = self.choisir_temps()
                asyncio.create_task(son_service.play_canal(son_choisi, int(t)))

                from view.jouer_son_view import JouerSonView

                return JouerSonView()

    def choisir_son(self):
        son_service = SonService()
        liste_sons = son_service.lister_son()
        son_choisi = inquirer.select(
            message="Choisissez un son : ",
            choices=liste_sons,
        ).execute()
        return son_choisi

    def choisir_temps(self):
        t = inquirer.text(
            message="Entrez le temps de lecture:",
            validate=lambda x: x.isdigit(),
            transformer=lambda x: int(x),
        ).execute()
        return t
