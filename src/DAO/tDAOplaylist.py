from Object.playlist import Playlist
from Object.son import Son
from Object.utilisateur import Utilisateur
from DAO.utilisateur_DAO import Utilisateur_DAO
from DAO.playlist_DAO import Playlist_DAO
from DAO.son_DAO import Son_DAO


son1 = Son(
    id_son=56,
    nom="Tom's Song",
    tags=["pas", "de", "tags"],
    path_stockage="data/test.mp3",
)
son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
son3 = Son(id_son=3, nom="son3", tags=["pluie"], path_stockage="data/test.mp3")
utilisateur = Utilisateur("user1", "b")

playlist = Playlist(
    utilisateur=utilisateur,
    id_playlist=1,
    nom_playlist="CA marche connard5",
    list_son=[[son1, 1], [son2, 2]],
)

playlistDAO = Playlist_DAO()
utilisateurDAO = Utilisateur_DAO()

sonDAO = Son_DAO()
sonDAO.supprimer_son(6)
# playlistDAO.ajouter_playlist(playlist)
# utilisateurDAO.creer_utilisateur(utilisateur)
# sonDAO.ajouter_son(son1)
# print(sonDAO.get_son_by_id(14))
# sonDAO.ajouter_son(son2)
# print(sonDAO.get_all_son()[12])
# sonDAO.supprimer_son(13)
# for k in range(0, 3):
#    son = sonDAO.get_all_son_ordre_by_id_playlist(1)[k][0]
#    print(son)
# print(sonDAO.get_son_by_id(13))
# print(sonDAO.get_son_by_name("Song 1"))
# playlistDAO.ajouter_playlist(playlist)
# print(playlistDAO.get_sons_by_playlist(playlist))
# print(playlistDAO.get_playlist(playlist))
# print(playlistDAO.get_sons_by_playlist(playlist))
