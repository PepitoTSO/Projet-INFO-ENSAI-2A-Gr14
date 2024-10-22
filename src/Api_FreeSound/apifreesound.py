import os
import requests
import dotenv
import json
from pathlib import Path

class apifreesound():
    '''Gestion des requetes à l'API'''
    def __init__(self):

        self.url = 'https://freesound.org'

        # Verifie et recupere la cle API dans le .env       mettre dans un config.py
        dotenv.load_dotenv()
        try:
            self.cleAPI = os.getenv('CLEAPI')
        except KeyError:
            print("Manque la variable d'environnement CLEAPI")

    def recherche_son(self, recherche: str, params=False) -> json:
        '''
        Get http avec la clef API selon recherche

        Params:
            recherche : str
            Ce que l'on recherche sur freesound
            params : bool
            Si besoin de filtres

        Returns:
            reponse : json
            ce que renvoie l'api en json
        '''

        payload = {'query': recherche, 'token': self.cleAPI, 'fields': 'id,name,description'}

        if params:
            payload['filter']=[''] # construire de quoi faire le payload

        # faire de la gestion d'erreur si code erreur http avec try et except
        reponse = requests.get(
            self.url + '/apiv2/search/text/',
            params=payload,
            timeout=1
            )

        reponse.raise_for_status()  # il faut en faire qqc de cette ligne d'exception

        return reponse.json()['results']

    def dl_son(self, id, HQ=False):
        if not isinstance(id, int):
            raise TypeError("id n'est pas int")

        fichier = Path(f"../data/son/{id}.mp3")

        if not fichier.exists():
            try:     
                payload = {'token': self.cleAPI}
                reponse = requests.get(
                    f'{self.url}/apiv2/sounds/{id}/',
                    params=payload,
                    timeout=1
                    )

                if HQ:
                    url_dl = reponse.json()['previews']['preview-hq-mp3']
                else:
                    url_dl = reponse.json()['previews']['preview-lq-mp3']

                reponse = requests.get(url_dl, stream=True)

                # Écriture du fichier dans le répertoire de destination
                with open(f'../data/son/{id}.mp3', 'wb') as f:
                    for chunk in reponse.iter_content(chunk_size=8192):
                        f.write(chunk)

                print(f"Fichier téléchargé avec succès dans {dl_path}")
            except Exception as e:
                print(f"Erreur lors du téléchargement du son avec ID {sound_id}: {e}")
        else:
            print("Le fichier existe dans data/son")

###la classe a deplacé

