import unittest
from Object.utilisateur import Utilisateur
from Object.son import Son
from Object.playlist import Playlist


def setUpModule():
    print("Setting up module resources...")


def tearDownModule():
    print("Tearing down module resources...")


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        # Common setup for all tests
        self.utilisateur = Utilisateur(1)
        self.son1 = Son(1, "Song 1", "Caracteristiques 1")
        self.son2 = Son(2, "Song 2", "Caracteristiques 2")
        self.playlist = Playlist(self.utilisateur, 1, "Playlist 1", [])

    def tearDown(self):
        # Cleanup (runs after every test)
        self.playlist = None

    def test_ajouter_son(self):
        # GIVEN
        son = self.son1
        ordre = 1

        # WHEN
        self.playlist.ajouter_son(son, ordre)

        # THEN
        self.assertEqual(len(self.playlist.list_son), 1)
        self.assertEqual(self.playlist.list_son[0][0], son)
        self.assertEqual(self.playlist.list_son[0][1], ordre)

    def test_supprimer_son(self):
        # GIVEN
        son = self.son1
        self.playlist.list_son = [[son, 1]]

        # WHEN
        self.playlist.supprimer_son(son)

        # THEN
        self.assertEqual(len(self.playlist.list_son), 0)

    def test_changer_ordre(self):
        # GIVEN
        son = self.son1
        ordre = 2
        self.playlist.list_son = [[son, 1]]

        # WHEN
        self.playlist.changer_ordre(son, ordre)

        # THEN
        self.assertEqual(len(self.playlist.list_son), 1)
        self.assertEqual(self.playlist.list_son[0][0], son)
        self.assertEqual(self.playlist.list_son[0][1], ordre)

    def test_changer_nom_playlist(self):
        # GIVEN
        nouveau_nom = "New Playlist Name"

        # WHEN
        self.playlist.changer_nom_playlist(nouveau_nom)

        # THEN
        self.assertEqual(self.playlist.nom_playlist, nouveau_nom)


if __name__ == "__main__":
    unittest.main()
