# import dotenv

# from view.accueil.accueil_view import AccueilView


## This script is the entry point of your application

# if __name__ == "__main__":
#    dotenv.load_dotenv(override=True)

#    # run Accueil View
#    current_view = AccueilView()
#    current_view.choisir_menu()

#    # while current_view is not none, the application is still running
#    while current_view:
#        # a border between view
#        with open("src/dessin/border.txt", "r", encoding="utf-8") as asset:
#            print(asset.read())
#        # Affichage du menu
#        current_view.afficher()
#        # ask user for a choice
#        current_view = current_view.choisir_menu()

#    with open("src/dessin/bye.txt", "r", encoding="utf-8") as asset:
#        print(asset.read())


import logging
import dotenv

from utils.log_init import initialiser_logs

from view.accueil.accueil_view import AccueilView
from view.menu_principal_view import MenuView


if __name__ == "__main__":
    # On charge les variables d'environnement
    dotenv.load_dotenv(override=True)

    # initialiser_logs("Application")

    current_view = AccueilView("Bienvenue")
    nb_erreurs = 0

    while current_view:
        if nb_erreurs > 100:
            print("Le programme recense trop d'erreurs et va s'arrêter")
            break
        try:
            # Affichage du menu
            current_view.afficher()

            # Affichage des choix possibles
            current_view = current_view.choisir_menu()
        except Exception as e:
            logging.info(e)
            nb_erreurs += 1
            print(e)
            # current_view = MenuView("Une erreur est survenue, retour au menu principal")

    # Lorsque l on quitte l application
    print("----------------------------------")
    print("Au revoir")

    logging.info("Fin de l'application")
