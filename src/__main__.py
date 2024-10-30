import dotenv

from view.menu_principalgit pull import StartView

# This script is the entry point of your application

if __name__ == "__main__":
    dotenv.load_dotenv(override=True)

    # run the Start View
    current_view = StartView()

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        with open("src/dessin/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())
        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make.choice()

    with open(
        "src/dessin/bye.txt", "r", encoding="utf-8"
    ) as asset:
        print(asset.read())
