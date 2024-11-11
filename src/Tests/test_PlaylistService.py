import unittest
from unittest.mock import MagicMock, patch
from Object.playlist import Playlist
from Object.son import Son
from Service.PlaylistService import PlaylistService
from DAO.playlist_DAO import Playlist_DAO
from view.session import Session
from Object.utilisateur import Utilisateur

class TestPlaylistService(unittest.TestCase):

    @patch('DAO.playlist_DAO.Playlist_DAO')  # Mock de Playlist_DAO
    def test_creer_playlist_success(self, MockPlaylistDAO):

        # Setup utilisateur
        utilisateur = Utilisateur("pseudotest", "pseudotest")
        playlist = Playlist(utilisateur, 10, "Test_playlist", [])

        # Initialiser la session avec l'utilisateur
        Session().utilisateur = utilisateur  # Utilisation de la session réelle

        # Mocker Playlist_DAO et sa méthode ajouter_playlist
        mock_playlist_dao = MagicMock(spec=Playlist_DAO)
        MockPlaylistDAO.return_value = mock_playlist_dao
        mock_playlist_dao.ajouter_playlist.return_value = playlist

        # Appel de la méthode à tester
        PlaylistService().creer_playlist("Test_playlist", [])

        # Debug : Vérifier si la méthode ajouter_playlist a bien été appelée
        print(f"Called: {mock_playlist_dao.ajouter_playlist.call_count}")  # Affiche le nombre d'appels
        mock_playlist_dao.ajouter_playlist.assert_called_once()  # Vérifier que l'appel a été effectué une fois


    @patch('view.session.Session')  # Mock uniquement la session
    def test_creer_playlist_failure(self, MockSession):
        # Création d'un utilisateur réel
        utilisateur = Utilisateur(pseudo="utilisateur_test", mdp_hache="hashed_password")

        # Création d'une instance mockée de la session
        mock_session = MockSession.return_value
        # Assigner l'utilisateur réel à la session (et non un mock)
        mock_session.utilisateur = utilisateur  # L'utilisateur est maintenant un vrai objet Utilisateur

        # Mocker Playlist_DAO pour faire échouer l'insertion
        with patch.object(Playlist_DAO, 'ajouter_playlist', return_value=False):
            # Initialisation du service PlaylistService
            playlist_service = PlaylistService()

            # Appel de la méthode à tester, qui échoue
            result = playlist_service.creer_playlist("Ma Playlist", [])

            # Vérification que la playlist dans la session est toujours None
            self.assertIsNone(mock_session.playlist)

            # Vérification du résultat (échec)
            self.assertFalse(result)

    @patch('DAO.playlist_DAO.Playlist_DAO')
    @patch('view.session.Session')
    def test_creer_playlist_with_default_son(self, MockSession, MockPlaylistDAO):
        # Mocker la session utilisateur
        mock_utilisateur = MagicMock(spec=Utilisateur)
        mock_utilisateur.pseudo = "utilisateur_test"
        MockSession.return_value.utilisateur = mock_utilisateur

        # Mocker Playlist_DAO et sa méthode ajouter_playlist
        mock_playlist_dao = MagicMock(spec=Playlist_DAO)
        MockPlaylistDAO.return_value = mock_playlist_dao
        mock_playlist = MagicMock(spec=Playlist)
        mock_playlist_dao.ajouter_playlist.return_value = mock_playlist

        # Appel de la méthode à tester avec une playlist vide
        playlist_service = PlaylistService()
        playlist_service.creer_playlist("Playlist Vide")

        # Vérifier que la méthode ajouter_playlist a bien été appelée
        mock_playlist_dao.ajouter_playlist.assert_called_once()

        # Vérifier que l'objet playlist est bien assigné à la session
        self.assertEqual(MockSession.return_value.playlist, mock_playlist)


if __name__ == '__main__':
    unittest.main()
