from son import Son
import unittest
import pygame

class TestSon(unittest.TestCase):

    def test_str(self):

    #Given
        test = Son(1, 'test', 'oui', 'data/test.mp3')
    #When
        repr_son1 = "self.id_son=1, self.nom='test', self.caracteristiques='oui'"
    #Then
        self.assertEqual(repr_son1,repr(test))

    def test_init_pygame(self):
        test = Son(1, 'test', 'oui', 'data/test.mp3')

        mixer_init=True

        self.assertEqual(mixer_init, pygame.mixer.get_init)

if __name__ == "__main__":
    unittest.main()