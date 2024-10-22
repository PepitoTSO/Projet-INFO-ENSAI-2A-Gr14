from src.Object.son import Son
import unittest
import pygame

class TestSon(unittest.TestCase):

    def test_repr(self):

    #Given
        son1=Son(999,"pop",("sympa","dance"),)
    #When
        repr_son1 = 'id_son=999,nom="pop",caracteristiques=("sympa","dance")'
    #Then
        self.assertEqual(repr_son1,repr(son1))

    def test_init_pygame(self):
        path="../data/son/id999.mp3"
        son1=Son(999,"pop",("sympa","dance"),path)

        mixer_init=True

        self.assertEqual(mixer_init, pygame.mixer.get_init)

    def test_nature_musique(self):
        son1=Son(999,"pop",("sympa","dance"),path)
        self.assertIsInstance(son1.musique, pygame.mixer.Sound)

if __name__ == "__main__":
    unittest.main()