import unittest
from unittest.mock import MagicMock, patch
from Object.son import Son
from Service.SonService import SonService
import pygame


class TestSonService(unittest.TestCase):

    def test_init_pygame(self):
        fr = 44100
        form = -16  # c'est la définition en bits, si neg alors celle du son
        ch = 2
        list_fr_format_channels = (fr, form, ch)
        list_test = pygame.mixer.get_init()
        self.assertEqual(list_fr_format_channels, list_test)

    def test_init_channel_pygame(self):
        n = 8
        n_channels = pygame.mixer.get_num_channels()
        self.assertEqual(n, n_channels)

    def setUp(self):
        self.son_service = SonService()
        self.son = Son(
            id_son=1, nom="Test Son", tags=["tag1"], path_stockage="data/test.mp3"
        )

    @patch("DAO.son_DAO.Son_DAO.supprimer_son")
    def test_supprimer_son(self, mock_supprimer_son):

        mock_supprimer_son.return_value = True

        self.son_service.supprimer_son(self.son)

        mock_supprimer_son.assert_called_once_with(self.son.id_son)

    @patch("DAO.son_DAO.Son_DAO.ajouter_son")
    def test_ajouter_son(self, mock_ajouter_son):

        mock_ajouter_son.return_value = True

        result = self.son_service.ajouter_son(self.son)

        mock_ajouter_son.assert_called_once_with(self.son)
        self.assertTrue(result)

    @patch("pygame.mixer.fadeout")
    def test_stop(self, mock_fadeout):

        # Act
        self.son_service.stop()

        # Assert
        mock_fadeout.assert_called_once_with(3)

    @patch("pygame.mixer.Channel")
    def test_stop_channel(self, mock_channel):
        """Probleme"""
        # Arrange
        mock_channel_instance = MagicMock()
        mock_channel.return_value = mock_channel_instance
        canal = 2

        # Act
        SonService().stop_channel(canal)

        # Assert
        mock_channel.assert_called_once_with(canal)
        mock_channel_instance.stop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
