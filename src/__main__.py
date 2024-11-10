import dotenv

from view.accueil.accueil_view import AccueilView


# This script is the entry point of your application

if __name__ == "__main__":
    dotenv.load_dotenv(override=True)

    # run the Start View
    current_view = AccueilView()
    current_view.choisir_menu()

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        with open("src/dessin/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())
        # Affichage du menu
        current_view.afficher()
        # ask user for a choice
        current_view = current_view.choisir_menu()

    with open("src/dessin/bye.txt", "r", encoding="utf-8") as asset:
        print(asset.read())
