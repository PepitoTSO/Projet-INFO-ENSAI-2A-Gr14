import logging
import dotenv
import asyncio
import nest_asyncio
from view.accueil.accueil_view import AccueilView

nest_asyncio.apply()


async def main():
    # On charge les variables d'environnement
    dotenv.load_dotenv(override=True)

    current_view = AccueilView("Bienvenue")
    nb_erreurs = 0

    while current_view:
        if nb_erreurs > 100:
            print("Le programme recense trop d'erreurs et va s'arrêter")
            break
        try:
            current_view.afficher()

            current_view = await current_view.choisir_menu()
        except Exception as e:
            logging.info(e)
            nb_erreurs += 1
            print(e)

    print("\n" + "-" * 50 + "\nMerci\n" + "-" * 50 + "\n")

    logging.info("Fin de l'application")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
