import unittest
from Object.utilisateur import Utilisateur
from Object.son import Son
from Object.playlist import Playlist


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.utilisateur = Utilisateur("NomUtilisateur", "mdp_hache")
        self.son1 = Son(1, "Titre 1", ["tag1", "tag2"], "path/to/son1.mp3")
        self.son2 = Son(2, "Titre 2", ["tag3", "tag4"], "path/to/son2.mp3")
        self.son3 = Son(3, "Titre 3", ["tag5"], "path/to/son3.mp3")
        self.son4 = Son(4, "Titre 4", ["tag6"], "path/to/son4.mp3")
        self.playlist = Playlist(
            self.utilisateur, 1, "Ma Playlist", [[self.son1, 1], [self.son2, 2]]
        )

    def test_creation_playlist_valide(self):
        playlist = Playlist(
            self.utilisateur, 1, "Ma Playlist", [[self.son1, 1], [self.son2, 2]]
        )
        self.assertEqual(playlist.utilisateur, self.utilisateur)
        self.assertEqual(playlist.id_playlist, 1)
        self.assertEqual(playlist.nom_playlist, "Ma Playlist")
        self.assertEqual(playlist.list_son, [[self.son1, 1], [self.son2, 2]])

    def test_utilisateur_invalide(self):
        with self.assertRaises(TypeError):
            Playlist(
                "Utilisateur Invalide",
                1,
                "Ma Playlist",
                [[self.son1, 1], [self.son2, 2]],
            )

    def test_id_playlist_invalide(self):
        with self.assertRaises(TypeError):
            Playlist(
                self.utilisateur, "1", "Ma Playlist", [[self.son1, 1], [self.son2, 2]]
            )

    def test_nom_playlist_invalide(self):
        with self.assertRaises(TypeError):
            Playlist(self.utilisateur, 1, 123, [[self.son1, 1], [self.son2, 2]])

    def test_list_son_invalide(self):
        with self.assertRaises(TypeError):
            Playlist(self.utilisateur, 1, "Ma Playlist", "Liste Invalide")

    def test_element_invalide_dans_list_son(self):
        with self.assertRaises(TypeError):
            Playlist(self.utilisateur, 1, "Ma Playlist", [self.son1, 1])

    def test_son_invalide_dans_list_son(self):
        with self.assertRaises(TypeError):
            Playlist(self.utilisateur, 1, "Ma Playlist", [["Son Invalide", 1]])

    def test_ordre_invalide_dans_list_son(self):
        with self.assertRaises(TypeError):
            Playlist(self.utilisateur, 1, "Ma Playlist", [[self.son1, "1"]])

    def test_ajouter_son_playlist_valide(self):
        self.playlist.ajouter_son_playlist(self.son3, 3)
        self.assertEqual(len(self.playlist.list_son), 3)
        self.assertEqual(self.playlist.list_son[2], [self.son3, 3])

    def test_ajouter_son_playlist_ordre_intermediaire(self):
        self.playlist.ajouter_son_playlist(self.son3, 2)
        self.assertEqual(len(self.playlist.list_son), 3)
        self.assertEqual(self.playlist.list_son[1], [self.son3, 2])
        self.assertEqual(
            self.playlist.list_son[2][1], 3
        )

    def test_ajouter_son_playlist_ordre_invalide_trop_petit(self):
        with self.assertRaises(ValueError):
            self.playlist.ajouter_son_playlist(self.son3, 0)

    def test_ajouter_son_playlist_ordre_invalide_trop_grand(self):
        with self.assertRaises(ValueError):
            self.playlist.ajouter_son_playlist(self.son3, 5)

    def test_ajouter_son_playlist_reindexation(self):
        self.playlist.ajouter_son_playlist(self.son3, 2)
        self.playlist.ajouter_son_playlist(self.son4, 1)
        self.assertEqual(self.playlist.list_son[0][1], 1)
        self.assertEqual(self.playlist.list_son[1][1], 2)
        self.assertEqual(self.playlist.list_son[2][1], 3)
        self.assertEqual(self.playlist.list_son[3][1], 4)

    def test_supprimer_son_existant(self):
        self.playlist.supprimer_son(self.son1)
        self.assertEqual(len(self.playlist.list_son), 1)
        self.assertEqual(self.playlist.list_son[0], [self.son2, 1])

    def test_supprimer_son_non_existant(self):
        result = self.playlist.supprimer_son(self.son3)
        self.assertFalse(result)
        self.assertEqual(len(self.playlist.list_son), 2)

    def test_changer_ordre_valide(self):
        self.playlist.changer_ordre(self.son1, 2)
        self.assertEqual(self.playlist.list_son[0], [self.son2, 1])
        self.assertEqual(self.playlist.list_son[1], [self.son1, 2])

    def test_changer_ordre_invalide(self):
        with self.assertRaises(ValueError):
            self.playlist.changer_ordre(self.son1, 0)

        with self.assertRaises(ValueError):
            self.playlist.changer_ordre(self.son1, 4)

    def test_changer_nom_playlist(self):
        self.playlist.changer_nom_playlist("Nouveau Nom")
        self.assertEqual(self.playlist.nom_playlist, "Nouveau Nom")

    def test_changer_nom_playlist_invalide(self):
        with self.assertRaises(TypeError):
            self.playlist.changer_nom_playlist(123)

    def test_str(self):
        expected_output = f"Playlist 'Ma Playlist' (ID: 1) by {self.utilisateur}:\nListe des Sons:\n  Ordre 1: {self.son1}\n  Ordre 2: {self.son2}\n"
        self.assertEqual(str(self.playlist), expected_output)


if __name__ == "__main__":
    unittest.main()
