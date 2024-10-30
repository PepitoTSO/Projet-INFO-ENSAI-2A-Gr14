from unittest import TestCase, TextTestRunner, TestLoader
from Object.utilisateur import Utilisateur
from Object.son import Son
from Object.playlist import Playlist


class TestPlaylist(TestCase):

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
