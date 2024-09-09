import os
import requests


class apifreesound():
    '''Gestion API'''

    def requestget(self, recherche: str, params=False, OAuth2=False):
        '''
        Get http avec la clef API selon recherche

        Params:
            recherche : str
            Ce que l'on recherche sur freesound
            params : bool
            Si besoin de filtres
            OAuth2 : bool
            Si authentification en OAuth2
        Returns:
            reponse : json
            ce que renvoie l'api en json
        '''

        # Verifie puis recupere la cle API dans le .env
        try:
            os.environ['CLEAPI']
        except KeyError:
            print("Manque la variable d'environnement CLEAPI")

        cleAPI = os.environ['CLEAPI']
        payload = {'query': recherche, 'token': cleAPI}

        if params:
            payload = apifreesound.filtre(payload)

        if OAuth2:
            apifreesound.apiOAuth2()

        # faire de la gestion d'erreur si code erreur http avec try et except
        reponse = requests.get(
            'https://freesound.org/apiv2/search/text/',
            params=payload,
            timeout=1
            )

        reponse.raise_for_status()

        return reponse.json()

    def parserjson(self, json):
        '''
        adapte le json retourné par requestget à la base de données

        reponse type
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

        '''
        # Peut etre une methode abstraite
        # a adapter pour la DAO, méthode ajout de données
        pass

    def apiOAuth2(self, recherche):
        '''
        gère l'authentification spécifique OAuth2 pour avoir plus de fonctionnalité
        
        Step 1: Your application redirects users to a Freesound page where they log in and are asked to give permissions to your application.
        Step 2: If users grant access to your application, Freesound redirects users to a url you provide and includes an authorization grant as a GET parameter*.
        Step 3: Your application uses that authorization grant to request an access token that ‘links’ the end user with your application and that you will then need to add to all your API requests.

        '''
        # A voir si nécessaire
        pass

    def filtre(self, params):
        '''permet de construire le payload http pour filtrer la requete de requestget'''
        pass
