import os
import requests
import dotenv
import json
import wget
import utils.dl.py

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

        payload = {'query': recherche, 'token': self.cleAPI, 'fields':['id','name','tags']}

        if params:
            payload['filter']=[''] # construire de quoi faire le payload

        # faire de la gestion d'erreur si code erreur http avec try et except
        reponse = requests.get(
            self.url + '/apiv2/search/text/',
            params=payload,
            timeout=1
            )

        reponse.raise_for_status() # il faut en faire qqc de cette ligne d'exception

        return reponse.json()


    def dl_son(self, id, HQ = False):

        payload = {'token': self.cleAPI, 'fields':['id','name','download']}
        reponse = requests.get(
            f'{self.url}/apiv2/sounds/{id}/',
            params=payload,
            timeout=1
            )
        
        if HQ:
            url_dl=reponse['download']['hq'] #ou qqc du genre
        else :
            url_dl=reponse['download']['lq'] #l'autre

        ##ALTERNATIVE1

        wget.download(url_dl) # bof wget est hyper vieux et dépendance

        ##ALTERNATIVE2

        # Téléchargement du fichier
        dl_path = dl.dossier
        
        reponse = requests.get(url_dl, stream=True)

        # Écriture du fichier dans le répertoire de destination
        with open(self.dl_path, 'wb') as f:
            for chunk in reponse.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Fichier téléchargé avec succès dans {self.dl_path}")





    def parserjson(repjson) -> list:
        '''
        adapte le json retourné par recherche_son à la base de données

        Parameters :

        repjson : json
        {
        "count": 2887, "previous": null, "next": "https://freesound.org/apiv2/search/text/?&query=test&weights=&page=2", "results":
        [
        {"id": 326361, "name": "ebs test3.wav", "tags": ["test", "home", "bass"], "license": "http://creativecommons.org/licenses/by-nc/3.0/", "username": "wazdabaz"},
        {"id": 326360, "name": "ebs test4.wav", "tags": ["test", "home", "bass"], "license": "http://creativecommons.org/licenses/by-nc/3.0/", "username": "wazdabaz"},
        {"id": 326363, "name": "ebs test.wav", "tags": ["test", "home", "bass"], "license": "http://creativecommons.org/licenses/by-nc/3.0/", "username": "wazdabaz"},
        {"id": 709450, "name": "230523 - test - MB otok", "tags": ["msh-6", "flac", "test", "field-recording", "zoomh5", "slovenia", "outdoor", "maribor", "zoom-h5", "msh6"], "license": "https://creativecommons.org/licenses/by/4.0/", "username": "dibko"},
        {"id": 178484, "name": "X-marks the spot (test tones).flac", "tags": ["sci-fi", "bleep", "sweep", "tones", "test", "sine", "logarithmic"], "license": "https://creativecommons.org/licenses/by-nc/4.0/", "username": "Timbre"},
        {"id": 517214, "name": "setting_interference_test_digital_silence_0_bits.wav", "tags": ["Test", "sound", "signal"], "license": "http://creativecommons.org/publicdomain/zero/1.0/", "username": "lartti"},
        {"id": 517216, "name": "left_and_right_channels_test.wav", "tags": ["Test", "sound", "signal"], "license": "http://creativecommons.org/publicdomain/zero/1.0/", "username": "lartti"}, {"id": 517217, "name": "front_channels_polarity_test.wav", "tags": ["Test", "sound", "signal"], "license": "http://creativecommons.org/publicdomain/zero/1.0/", "username": "lartti"},
        {"id": 687385, "name": "1OA 26 Corners Test.wav", "tags": ["1oa", "b-format", "ambisonics", "ambix", "test", "bformat"], "license": "https://creativecommons.org/licenses/by-nc/4.0/", "username": "AudioBrewers"},
        {"id": 64363, "name": "test_elecdict.wav", "tags": ["doodling", "guitar", "test", "usb"], "license": "http://creativecommons.org/licenses/by/3.0/", "username": "NoiseCollector"},
        {"id": 64364, "name": "test_elecdict_vol1.wav", "tags": ["doodling", "guitar", "test", "usb"], "license": "http://creativecommons.org/licenses/by/3.0/", "username": "NoiseCollector"}, {"id": 64365, "name": "test_electure.wav", "tags": ["doodling", "guitar", "test", "usb"], "license": "http://creativecommons.org/licenses/by/3.0/", "username": "NoiseCollector"}, {"id": 64367, "name": "test_guitar2.wav", "tags": ["acoustic", "doodling", "guitar", "microphone", "test", "usb"], "license": "http://creativecommons.org/licenses/by/3.0/", "username": "NoiseCollector"}, {"id": 165277, "name": "Surround Test - Channel Names", "tags": ["multichannel", "name", "calibration", "track", "multi-channel", "surround", "calibrate", "test", "naming"], "license": "https://creativecommons.org/licenses/by/4.0/", "username": "blouhond"}, {"id": 436839, "name": "test.wav", "tags": ["test", "sound", "soundtest"], "license": "http://creativecommons.org/publicdomain/zero/1.0/", "username": "thedumbstudio"}
        ]
        }

        Returns :

        repjson : list
        [
        {
            "id": 326361,
            "name": "ebs test3.wav",
            "tags": [
            "test",
            "home",
            "bass"
            ],
            "license": "http://creativecommons.org/licenses/by-nc/3.0/",
            "username": "wazdabaz"
        },
        {
            "id": 326360,
            "name": "ebs test4.wav",
            "tags": [
            "test",
            "home",
            "bass"
            ],
            "license": "http://creativecommons.org/licenses/by-nc/3.0/",
            "username": "wazdabaz"
        },

        '''

        repjson = repjson['results']

        repjson = json.dumps(repjson, indent=2)

        return repjson