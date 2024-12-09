from src.Api_FreeSound import apifreesound
from src.Service.SonService import SonService
from src.Object.son import Son
#from src.DAO.playlist_DAO import Playlist_DAO
from src.Api_FreeSound.recherche_avancee import recherche_avancee
from src.Service.SonService import SonService
'''
Reset l'appli pour la présentation.
'''
#verif install des requierements

#init gensim et pygame
recherche_avancee().charger_modele()
SonService()

#nettoyer le dossier son

#penser a nettoyer bdd du bazar
bdd.reset() quelque chose comme

liste_son = [
    (1, "Son A", ["tag1", "tag2"]),
    (2, "Son B", ["tag3", "tag4"]),
    (3, "Son C", ["tag5", "tag6"])
]

def ajout_son(iden, nom, tags):
    try:
        son=Son(iden, nom, tags)
        apifreesound().dl_son(int(son.id))
        SonService().ajouter_son(son)
        print(f"ajout son{son}")
    except Exception as e :
        print(f"/!\prblm init son{e}")

def init_son(list_son):
    for a, b, c in list_son:
        ajout_son(a, b ,c)

init_son(liste_son)

# pour les utilisateurs et le playlist on va directement dans le pop_db sql

'''def init_son_plist(iden, nom, tags, playlist):
    try :
        son=Son(iden, nom, tags)
        Playlist_DAO().ajouter_son(playlist: Playlist, son: Son, ordre: int)
        print(f"ajout de la playlist{playlist}")
    except Exception as e:
        print(f"/!\prblm init plist {e}")'''
