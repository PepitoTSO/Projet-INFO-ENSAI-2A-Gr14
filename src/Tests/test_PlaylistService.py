import unittest
from unittest.mock import patch, MagicMock
from Object.utilisateur import Utilisateur
from Object.son import Son
from Object.playlist import Playlist
from Service.PlaylistService import PlaylistService
from utils.singleton import Singleton
from DAO.playlist_DAO import Playlist_DAO
from DAO.son_DAO import Son_DAO
from view.session import Session


##### Test Créer une playlist

# utilisateur = Utilisateur("user1", "hashed_password1")
# son1 = Son(
# id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
# )
# son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
# list_son = [[son1, 1], [son2, 2]]
# Session(utilisateur, None, None)
# service = PlaylistService()
# service.creer_playlist("Ma Playlist", list_son)
# print(Session().playlist)



##### Test Supprimer une playlist
#On en ajoute une d'abord, il faut ensuite modifier l'id de la playlist à supprimer
# utilisateur = Utilisateur("user1", "hashed_password1")
# son1 = Son(
# id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
# )
# son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
# list_son = [[son1, 1], [son2, 2]]
# playlist = Playlist(utilisateur, 28, "Ma playlist", list_son)
# Session(utilisateur, playlist, None)
# service = PlaylistService()
# service.supprimer_playlist()
# print(Session().playlist)
# Session().playlist = None
# print(Session().playlist)


### Test  modifier nom playlist
#### Ajout Playlist
# utilisateur = Utilisateur("user1", "hashed_password1")
# son1 = Son(
# id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
# )
# son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
# list_son = [[son1, 1], [son2, 2]]
# Session(utilisateur, None, None)
# service = PlaylistService()
# service.creer_playlist("Ma Playlist", list_son)
# print(Session().playlist)
# ############
# service.modifier_nom_playlist("Quoicoubeh")
# print(Session().playlist)

##### Test changer ordre son
# utilisateur = Utilisateur("user1", "hashed_password1")
# son1 = Son(
# id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
# )
# son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
# list_son = [[son1, 1], [son2, 2]]
# Session(utilisateur, None, None)
# service = PlaylistService()
# service.creer_playlist("Ma Playlist", list_son)
# print(Session().playlist)

# ###Changer l'ordre des sons

# service.changer_ordre_son(son1, 2)
# print(Session().playlist)

##### Test supprimer un son

# utilisateur = Utilisateur("user1", "hashed_password1")
# son1 = Son(
# id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
# )
# son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
# list_son = [[son1, 1], [son2, 2]]
# Session(utilisateur, None, None)
# service = PlaylistService()
# service.creer_playlist("Ma Playlist", list_son)
# print(Session().playlist)
# service.retirer_son_playlist(son1)
# print(Session().playlist)
# service.retirer_son_playlist(son2)
# print(Session().playlist)


##### Test copier playlist

utilisateur = Utilisateur("user1", "hashed_password1")
son1 = Son(
id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
)
son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
list_son = [[son1, 1], [son2, 2]]
Session(utilisateur, None, None)
service = PlaylistService()
service.creer_playlist("Ma Playlist", list_son)
print(Session().playlist)
service.copier_playlist()
print(Session().playlist)

##### Tests ajouter son

Session().playlist = None
utilisateur = Utilisateur("user1", "hashed_password1")
son1 = Son(
id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
)
son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")

son3 = Son(id_son=70, nom="Song 70", tags=["rock"], path_stockage="/music/song2.mp3")
list_son = [[son1, 1], [son2, 2]]
Session(utilisateur, None, None)
service = PlaylistService()
service.creer_playlist("Ma Playlist", list_son)
print(Session().playlist)
service.ajouter_son_a_playlist(son3, 2)
print(Session().playlist)
