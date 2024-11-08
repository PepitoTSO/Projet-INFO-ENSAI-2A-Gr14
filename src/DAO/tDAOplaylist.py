from Object.playlist import Playlist
from Object.son import Son
from Object.utilisateur import Utilisateur
from DAO.utilisateur_DAO import Utilisateur_DAO
from DAO.playlist_DAO import Playlist_DAO
from DAO.son_DAO import Son_DAO

son1 = Son(
    id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
)
son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
son3 = Son(id_son=3, nom="son3", tags=["pluie"], path_stockage="data/test.mp3")
utilisateur = Utilisateur("a", "b")
playlist = Playlist(
    utilisateur=utilisateur,
    id_playlist=1,
    nom_playlist="test",
    list_son=[[son1, 1], [son2, 2]],
)

playlistDAO = Playlist_DAO()
utilisateurDAO = Utilisateur_DAO()
sonDAO = Son_DAO()

utilisateurDAO.creer_utilisateur(utilisateur)
sonDAO.ajouter_son(son1)
sonDAO.ajouter_son(son2)
playlistDAO.ajouter_playlist(playlist)
