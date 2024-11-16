import os
import requests
import dotenv
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)


class apifreesound:
    """Gestion des requêtes à l'API"""

    def __init__(self):
        self.url = "https://freesound.org"

        # Vérifie et récupère la clé API dans le .env
        dotenv.load_dotenv()
        try:
            self.cleAPI = os.getenv("CLEAPI")
        except KeyError:
            print("Manque la variable d'environnement CLEAPI")

    def recherche_son(self, recherche: str, params=False):
        """
        Get http avec la clé API selon recherche

        Params:
            recherche : str
            Ce que l'on recherche sur freesound
            params : bool
            Si besoin de filtres

        Returns:
            Affiche les cinq premiers résultats de manière lisible
        """
        payload = {
            "query": recherche,
            "token": self.cleAPI,
            "fields": "id,name,tags,description",
        }

        if params:
            payload["filter"] = [""]

        try:
            reponse = requests.get(
                self.url + "/apiv2/search/text/", params=payload, timeout=1
            )
            reponse.raise_for_status()
            results = reponse.json()["results"][:5]  # Get only the first 5 results

            if not results:
                print("Aucun résultat trouvé.")
                return None

            for idx, son in enumerate(results[:-1], start=1):
                # Extract only the first sentence of the description
                description = son["description"].split(".")[0] + "."

                print(f"{Fore.MAGENTA}Resultat {idx}:{Style.RESET_ALL}")
                print(f"  {Fore.RED}ID: {Style.RESET_ALL}{son['id']}")
                print(f"  {Fore.RED}Nom: {Style.RESET_ALL}{son['name']}")
                print(f"  {Fore.RED}Description: {Style.RESET_ALL}{description}\n")
            return results
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")

    def dl_son(self, id, HQ=False):
        """
        Permet de telecharger un son à partir de son identifiant sur l'API avec verification si le son existe deja"
        """
        if not isinstance(id, int):
            raise TypeError("id n'est pas int")

        fichier = Path(f"./data/son/{id}.mp3")
        repertoire = fichier.parent

        if not repertoire.exists():
            try:
                repertoire.mkdir(parents=True, exist_ok=True)
                print(f"Répertoire {repertoire} créé.")
            except Exception as e:
                print(f"Erreur lors de la création du répertoire : {e}")
                return None

        if not fichier.exists():
            try:
                payload = {"token": self.cleAPI}
                reponse = requests.get(
                    f"{self.url}/apiv2/sounds/{id}/", params=payload, timeout=1
                )

                if HQ:
                    url_dl = reponse.json()["previews"]["preview-hq-mp3"]
                else:
                    url_dl = reponse.json()["previews"]["preview-lq-mp3"]

                reponse = requests.get(url_dl, stream=True)

                # Écriture du fichier dans le répertoire de destination
                with open(fichier, "wb") as f:
                    for chunk in reponse.iter_content(chunk_size=8192):
                        f.write(chunk)

                print(f"Fichier téléchargé avec succès: {fichier}")
            except Exception as e:
                print(f"Erreur lors du téléchargement du son avec ID {id}: {e}")
        else:
            print("Le fichier existe déjà dans data/son")
