from unittest.mock import patch, MagicMock
from Object.utilisateur import Utilisateur
from Object.son import Son
from Object.playlist import Playlist
from Service.PlaylistService import PlaylistService
from DAO.playlist_DAO import Playlist_DAO
from view.session import Session


def test_creer_playlist():
    """Test creer la playlist"""

    # GIVEN
    utilisateur = Utilisateur("user1", "hashed_password1")
    son1 = Son(
        id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
    )
    son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
    list_son = [[son1, 1], [son2, 2]]
    playlist_a_creer = Playlist(utilisateur, 11, "Playlist Test", list_son)
    Session().utilisateur = utilisateur
    Playlist_DAO().ajouter_playlist = MagicMock(return_value=playlist_a_creer)

    # WHEN

    PlaylistService().creer_playlist("Ma playlist", list_son)

    # THEN
    assert Session().utilisateur == utilisateur
    assert Session().playlist == playlist_a_creer
    Session().playlist = None
    Session().utilisateur = None


def test_supprimer_playlist():
    """Test supprimer la playlist"""

    # GIVEN
    utilisateur = Utilisateur("user1", "hashed_password1")
    playlist = Playlist(utilisateur, 13, "Playlist Test", [])
    Session().utilisateur = utilisateur
    Session().playlist = playlist
    Playlist_DAO().supprimer_playlist = MagicMock(return_value=True)

    # WHEN
    PlaylistService().supprimer_playlist()

    # THEN
    Playlist_DAO().supprimer_playlist.assert_called_once_with(playlist)
    assert Session().playlist is None
    Session().playlist = None
    Session().utilisateur = None


def test_modifier_nom_playlist():
    """Test modifier le nom de la playlist"""

    # GIVEN
    utilisateur = Utilisateur("user1", "hashed_password1")
    playlist = Playlist(utilisateur, 12, "Old Name", [])
    Session().utilisateur = utilisateur
    Session().playlist = playlist
    Playlist_DAO().modifier_nom_playlist = MagicMock()

    # WHEN
    PlaylistService().modifier_nom_playlist("New Name")

    # THEN
    assert Session().playlist.nom_playlist == "New Name"
    Playlist_DAO().modifier_nom_playlist.assert_called_once_with(playlist, "New Name")
    Session().playlist = None
    Session().utilisateur = None


def test_changer_ordre_son():
    """Test changer l'ordre des sons dans la playlist"""

    # GIVEN
    utilisateur = Utilisateur("user1", "hashed_password1")
    son1 = Son(
        id_son=1, nom="son1", tags=["pas", "de", "tags"], path_stockage="data/test.mp3"
    )
    son2 = Son(id_son=2, nom="son2", tags=["tags"], path_stockage="data/test.mp3")
    list_son = [[son1, 1], [son2, 2]]
    playlist = Playlist(utilisateur, 14, "Playlist Test", list_son)
    Session().utilisateur = utilisateur
    Session().playlist = playlist
    Playlist_DAO().changer_ordre = MagicMock()

    # WHEN
    PlaylistService().changer_ordre_son(son1, 2)
    print(Session().playlist)
    # THEN
    for liste in Session().playlist.list_son:
        if liste[0] == son1:
            assert liste[1] == 2
    Playlist_DAO().changer_ordre.assert_called_once_with(playlist, son1, 2)
    Session().playlist = None
    Session().utilisateur = None


def test_retirer_son_playlist():
    """Test retirer un son de la playlist"""

    # GIVEN
    utilisateur = Utilisateur("user1", "hashed_password1")
    son = Son(id_son=1, nom="son1", tags=["tag"], path_stockage="data/test.mp3")
    playlist = Playlist(utilisateur, 15, "Playlist Test", [[son, 1]])
    Session().utilisateur = utilisateur
    Session().playlist = playlist
    Playlist_DAO().supprimer_son = MagicMock()

    # WHEN
    PlaylistService().retirer_son_playlist(son)

    # THEN
    assert len(playlist.list_son) == 0
    Playlist_DAO().supprimer_son.assert_called_once_with(playlist, son)
    Session().playlist = None
    Session().utilisateur = None


def test_copier_playlist():
    """Test copier une playlist"""

    # GIVEN
    utilisateur = Utilisateur("user1", "hashed_password1")
    son = Son(id_son=1, nom="son1", tags=["tag"], path_stockage="data/test.mp3")
    playlist = Playlist(utilisateur, 12, "Original Playlist", [[son, 1]])
    playlist_copie = Playlist(utilisateur, 16, "Original Playlist", [[son, 1]])
    Session().utilisateur = utilisateur
    Session().playlist = playlist
    with patch.object(
        PlaylistService, "creer_playlist", return_value=playlist_copie
    ) as mock_creer_playlist:
        # WHEN
        PlaylistService().copier_playlist()

        # THEN
        mock_creer_playlist.assert_called_once_with("Original Playlist", [[son, 1]])
        playlist_copie = Session().playlist
        assert playlist_copie.nom_playlist == "Original Playlist"
        assert playlist_copie.list_son == [[son, 1]]
        assert playlist_copie.utilisateur == utilisateur


def test_afficher_playlist():
    """Test afficher les playlists d'un utilisateur"""

    # GIVEN
    utilisateur = Utilisateur("user1", "hashed_password1")
    Session().utilisateur = utilisateur
    playlists = [
        Playlist(utilisateur, 1, "Playlist 1", []),
        Playlist(utilisateur, 2, "Playlist 2", []),
    ]
    Playlist_DAO().get_all_playlists_by_user = MagicMock(return_value=playlists)

    # WHEN
    result = PlaylistService().afficher_playlist()

    # THEN
    assert result == playlists
    Playlist_DAO().get_all_playlists_by_user.assert_called_once_with(utilisateur)


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
