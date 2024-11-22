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

    @patch("pygame.mixer.music.load")
    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.get_busy", side_effect=[True, False])
    def test_play(self, mock_get_busy, mock_play, mock_load):

        self.son_service.play(self.son)

        mock_load.assert_called_once_with(self.son.path_stockage)
        mock_play.assert_called_once()
        self.assertEqual(mock_get_busy.call_count, 2)

    @patch("pygame.mixer.music.pause")
    def test_pause(self, mock_pause):
        # Act
        self.son_service.pause()

        # Assert
        mock_pause.assert_called_once()

    @patch("pygame.mixer.music.unpause")
    def test_unpause(self, mock_unpause):
        # Act
        self.son_service.unpause()

        # Assert
        mock_unpause.assert_called_once()

    @patch("pygame.mixer.fadeout")
    def test_stop(self, mock_fadeout):

        # Act
        self.son_service.stop()

        # Assert
        mock_fadeout.assert_called_once_with(3)

    @patch("pygame.mixer.Sound")
    @patch("pygame.mixer.Channel")
    def test_play_channel(self, mock_channel, mock_sound):
        # Arrange
        mock_channel_instance = MagicMock()
        mock_channel.return_value = mock_channel_instance

        # Configure mock_sound to return a mock "sound object"
        mock_sound_instance = MagicMock()
        mock_sound.return_value = mock_sound_instance

        # Act
        self.son_service.play_canal(self.son)

        # Assert
        mock_sound.assert_called_once_with(
            self.son.path_stockage
        )  # Sound should be initialized with the path
        mock_channel.assert_called_once()  # Ensure we obtained a channel
        mock_channel_instance.play.assert_called_once_with(
            mock_sound_instance
        )  # play is called with the sound instance

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

    @patch("pygame.mixer.Channel")
    @patch("pygame.mixer.Sound")
    def test_jouer_en_boucle(self, mock_sound, mock_channel):
        # Arrange
        mock_channel_instance = MagicMock()
        mock_channel.return_value = mock_channel_instance

        # Act
        self.son_service.jouer_en_boucle(self.son, canal=2, temps=500)

        # Assert
        mock_sound.assert_called_once_with(self.son.path_stockage)
        mock_channel.assert_called_once_with(2)
        mock_channel_instance.play.assert_called_once_with(
            mock_sound.return_value, -1, 500
        )

    @patch(
        "random.uniform", return_value=1
    )  # Mocking the random.uniform to return 1 second for simplicity
    @patch("time.sleep", return_value=None)  # Mocking sleep to avoid actual waiting
    @patch.object(
        SonService, "play_channel"
    )  # Mock play_channel to prevent real sound playing
    def test_jouer_aleatoire(self, mock_play_channel, mock_sleep, mock_uniform):
        # Act
        self.son_service.jouer_aleatoire(
            self.son, attente_min=1, attente_max=2, duree=3
        )

        # Assert
        mock_play_channel.assert_called()
        mock_uniform.assert_called_with(1, 2)
        self.assertTrue(mock_sleep.called)


if __name__ == "__main__":
    unittest.main()
