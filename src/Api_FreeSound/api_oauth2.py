import requests
import time
from selenium import webdriver
from dotenv import load_dotenv
import os

class API_OAUTH2():
        '''
        gère l'authentification spécifique OAuth2 pour avoir plus de fonctionnalités
                
        Step 1: Your application redirects users to a Freesound page where they log in and are asked to give permissions to your application.
        Step 2: If users grant access to your application, Freesound redirects users to a url you provide and includes an authorization grant as a GET parameter*.
        Step 3: Your application uses that authorization grant to request an access token that ‘links’ the end user with your application and that you will then need to add to all your API requests.

        Returns
        tokenOauth2 : str
                Le token qui permet d'attester de l'authentification.
        
        Example
        >>>rAPI=API_OAUTH2()
        >>>print(rAPI.tokenOAuth2)
        2WoqneIUA2PeCzrWcB4BPsbxvtPAKg
        '''

        #[orga] Au propre dans un config.py puis import ici?
        load_dotenv()
        CLEAPI = os.getenv("CLEAPI")
        client_id = os.getenv("CLIENTID")

        def __init__(self):
               '''
               Créer le token à l'instanciation de la classe (on verra si c'est plus pratique)
               '''
               
               self.tokenOAuth2 = self.a2ioauth()["access_token"]

        def _step12OAuth2(self):
                '''
                
                Step 1: Your application redirects users to a Freesound page where they log in and are asked to give permissions to your application.
                Step 2: If users grant access to your application, Freesound redirects users to a url you provide and includes an authorization grant as a GET parameter*.

                Ouvre un navigateur, attend le login, demande le token de connection et le retourne

                Params
                navigateur : str
                        [a venir]
                Return
                token : str
                        Le token de connexion présent après la page de login
                '''
                #Step1
                url = 'https://freesound.org/apiv2/oauth2/authorize/'

                getpayload = {'client_id': API_OAUTH2.client_id, 'response_type': 'code'}

                with requests.Session() as session:
                        # pour conserver les cookies etc pas sûr que utile

                        r = session.get(url, params=getpayload)

                        if r.status_code <= 400 :
                                #fait pour chrome, possible autre navigateur, argument defaut dans fonction? // navigateur = Chrome

                                navigateur = webdriver.Chrome()

                                navigateur.get(r.url)

                                time.sleep(15)

                                token = input("le token (ctrl c/v)")
                                if token:
                                    pass
                                else:
                                    #pas sûr que utile
                                    print("il vous reste 15 avant quit")
                                    time.sleep(15)

                                navigateur.quit()
                                        
                        else:
                                print("prblm get Erreur http :", r.status_code)

                return token

        def a2ioauth(self):
                '''
                Step 2: If users grant access to your application, Freesound redirects users to a url you provide and includes an authorization grant as a GET parameter*.
                Step 3: Your application uses that authorization grant to request an access token that ‘links’ the end user with your application and that you will then need to add to all your API requests.

                Params

                Returns
                rep.text : dict
                        Un dict contenant access_token, expires_in, token_type, scope, refresh_token
                        ex : {"access_token": "MelWOOo1WLtdwsRGfPYAsGkyH4FOxd", "expires_in": 86400, "token_type": "Bearer", "scope": "read write", "refresh_token": "tKhALCVjvNK28omQ4TvWJYAWD9NPTS"}
                
                '''

                code_auth = API_OAUTH2._step12OAuth2(self)

                postpayload = {"client_id" : API_OAUTH2.client_id, "client_secret" : API_OAUTH2.CLEAPI, 'grant_type' : 'authorization_code', "code": code_auth}
                
                rep = requests.post("https://freesound.org/apiv2/oauth2/access_token/", postpayload)

                return rep.json()


        def resetauth(self):
                '''
                [A Venir]
                Permet de reset le token avec le reset_token si nécessaire (en fonction de date d'expiration)
                
                access tokens do have a limited lifetime of 24 hours. Notice that access token response from Step 3 includes an expires_in parameter that indicates that lifetime in seconds. After that time, the token will be invalidated and any request to the API using the token will return a 401 (Unauthorized) response showing an ‘Expired token’ error. If that happens, you can obtain a new access token either by starting the whole authentication process again or by requesting a new access token using the refresh token that was also issued to you when you got the access token (refresh_token parameter above).

                idée
                Si l'objet a déjà été instancié alors une clef existe déjà donc il suffit de la reset ssi expiré donc il faut compter l'instanciation à l'initialisation et reset en fonction de la date d'instanciation
                
                Returns
                rep.text : dict
                        Un dict contenant access_token, expires_in, token_type, scope, refresh_token
                        ex : {"access_token": "MelWOOo1WLtdwsRGfPYAsGkyH4FOxd", "expires_in": 86400, "token_type": "Bearer", "scope": "read write", "refresh_token": "tKhALCVjvNK28omQ4TvWJYAWD9NPTS"}
                                
                '''

                refresh_token = self.tokenOAuth2["refresh_token"]

                postpayload = {"client_id": API_OAUTH2.client_id, "client_secret" : API_OAUTH2.CLEAPI, 'grant_type' : 'refresh_token', "refresh_token": refresh_token}

                rep = requests.post("https://freesound.org/apiv2/oauth2/access_token/", postpayload)

                return rep.json()

#a mettre en forme (blake)