from Service.SonService import SonService
import unittest
from unittest.mock import MagicMock, patch
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


if __name__ == '__main__':
    unittest.main()
