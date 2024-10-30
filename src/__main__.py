import dotenv

from View.accueil.accueil_view import AccueilView


# This script is the entry point of your application

if __name__ == "__main__":
    dotenv.load_dotenv(override=True)

    # run the Start View
    current_view = AccueilView

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        with open("src/dessin/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())
        # Display the info of the view
        current_view.display_info(self)
        # ask user for a choice
        current_view = current_view.choix

    with open("src/dessin/bye.txt", "r", encoding="utf-8") as asset:
        print(asset.read())
