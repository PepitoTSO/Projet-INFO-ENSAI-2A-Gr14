import unittest
from Object.utilisateur import Utilisateur
from Object.son import Son
from Object.playlist import Playlist


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur("user1", "hashed_password")
        self.son1 = Son(
            id_son=1, nom="Son1", tags=["tag1", "tag2"], path_stockage="path1.mp3"
        )
        self.son2 = Son(id_son=2, nom="Son2", tags=["tag3"], path_stockage="path2.mp3")
        self.son3 = Son(id_son=3, nom="Son3", tags=["tag4"], path_stockage="path3.mp3")
        self.playlist = Playlist(
            self.utilisateur, 1, "My Playlist", [[self.son1, 1], [self.son2, 2]]
        )

    def test_ajouter_son_playlist(self):
        self.playlist.ajouter_son_playlist(self.son3, 1)
        self.assertEqual(len(self.playlist.list_son), 3)
        self.assertEqual(self.playlist.list_son[0][0], self.son3)
        self.assertEqual(self.playlist.list_son[0][1], 1)
        self.assertEqual(self.playlist.list_son[1][0], self.son1)
        self.assertEqual(self.playlist.list_son[1][1], 2)
        self.assertEqual(self.playlist.list_son[2][0], self.son2)
        self.assertEqual(self.playlist.list_son[2][1], 3)

    def test_supprimer_son(self):
        # Supprimer un son existant
        self.playlist.supprimer_son(self.son1)
        self.assertEqual(len(self.playlist.list_son), 1)
        self.assertEqual(self.playlist.list_son[0][0], self.son2)
        self.assertEqual(
            self.playlist.list_son[0][1], 1
        )  # After deletion, ordre should adjust

        # Supprimer un son non existant
        result = self.playlist.supprimer_son(self.son3)
        self.assertFalse(result)

    def test_changer_ordre(self):
        # Changer l'ordre d'un son existant
        self.playlist.changer_ordre(self.son1, 2)
        self.assertEqual(self.playlist.list_son[0][0], self.son2)
        self.assertEqual(self.playlist.list_son[0][1], 1)  # son2 should be at ordre 1
        self.assertEqual(self.playlist.list_son[1][0], self.son1)
        self.assertEqual(
            self.playlist.list_son[1][1], 2
        )  # son1 should now be at ordre 2

        # Tester un ordre invalide
        with self.assertRaises(ValueError):
            self.playlist.changer_ordre(
                self.son1, 5
            )  # Invalid ordre, greater than list length
        with self.assertRaises(ValueError):
            self.playlist.changer_ordre(self.son1, 0)  # Invalid ordre, less than 1

    def test_changer_nom_playlist(self):
        # Changer le nom de la playlist
        self.playlist.changer_nom_playlist("New Playlist Name")
        self.assertEqual(self.playlist.nom_playlist, "New Playlist Name")

    def test_initialisation_invalide(self):
        # Tester les erreurs d'initialisation
        with self.assertRaises(TypeError):
            Playlist(
                "not_a_user", 1, "test", []
            )  # utilisateur n'est pas de type Utilisateur
        with self.assertRaises(TypeError):
            Playlist(
                self.utilisateur, "not_an_int", "test", []
            )  # id_playlist n'est pas un int
        with self.assertRaises(TypeError):
            Playlist(self.utilisateur, 1, 12345, [])  # nom_playlist n'est pas un str
        with self.assertRaises(TypeError):
            Playlist(
                self.utilisateur, 1, "test", "not_a_list"
            )  # list_son n'est pas une liste

    def test_ajouter_son_invalid(self):
        # Tester ajout de son avec un ordre invalide
        with self.assertRaises(ValueError):
            self.playlist.ajouter_son_playlist(self.son3, 0)  # ordre invalide, < 1
        with self.assertRaises(ValueError):
            self.playlist.ajouter_son_playlist(
                self.son3, 5
            )  # ordre invalide, > len(list_son) + 1

    def test_repr_str_methods(self):
        # Tester la méthode __str__
        expected_str = (
            "Playlist 'My Playlist' (ID: 1) by Utilisateur: user1:\n"
            "Liste des Sons:\n"
            "  Ordre 1: Son ID: 1, Nom: 'Son1', Tags: [tag1, tag2], Chemin: path1.mp3\n"
            "  Ordre 2: Son ID: 2, Nom: 'Son2', Tags: [tag3], Chemin: path2.mp3\n"
        )
        self.assertEqual(str(self.playlist), expected_str)

    def test_playlist_with_empty_list_son(self):
        # Tester l'initialisation avec une liste de sons vide
        empty_playlist = Playlist(self.utilisateur, 2, "Empty Playlist", [])
        self.assertEqual(empty_playlist.list_son, [])
        self.assertEqual(len(empty_playlist.list_son), 0)

    def test_ajouter_son_playlist_with_duplicate_son(self):
        # Ajouter un son déjà présent dans la playlist
        self.playlist.ajouter_son_playlist(self.son1, 3)
        self.assertEqual(len(self.playlist.list_son), 3)
        self.assertEqual(self.playlist.list_son[2][0], self.son1)
        self.assertEqual(self.playlist.list_son[2][1], 3)

    def test_supprimer_son_present(self):
        # Suppression d'un son présent dans la playlist (son2)
        result = self.playlist.supprimer_son(self.son2)
        self.assertTrue(result)

        # Vérifier que son2 n'est plus dans la playlist
        sons_in_playlist = [item[0] for item in self.playlist.list_son]
        self.assertNotIn(self.son2, sons_in_playlist)

        # Vérifier que les ordres des sons restants sont mis à jour
        expected_list_son = [[self.son1, 1]]
        self.assertEqual(self.playlist.list_son, expected_list_son)

    def test_supprimer_son_absent(self):
        # Tentative de suppression d'un son non présent dans la playlist (son3)
        result = self.playlist.supprimer_son(self.son3)
        self.assertFalse(result)

        # Vérifier que la playlist reste inchangée
        expected_list_son = [[self.son1, 1], [self.son2, 2]]
        self.assertEqual(self.playlist.list_son, expected_list_son)

    def test_supprimer_premier_son(self):
        # Suppression du premier son de la playlist (son1)
        result = self.playlist.supprimer_son(self.son1)
        self.assertTrue(result)

        # Vérifier que son1 n'est plus dans la playlist
        sons_in_playlist = [item[0] for item in self.playlist.list_son]
        self.assertNotIn(self.son1, sons_in_playlist)

        # Vérifier que les ordres sont mis à jour correctement
        expected_list_son = [[self.son2, 1]]
        self.assertEqual(self.playlist.list_son, expected_list_son)

    def test_supprimer_dernier_son(self):
        # Ajouter son3 à la playlist pour pouvoir le supprimer en dernier
        self.playlist.ajouter_son_playlist(self.son3, 3)

        # Suppression du dernier son de la playlist (son3)
        result = self.playlist.supprimer_son(self.son3)
        self.assertTrue(result)

        # Vérifier que son3 n'est plus dans la playlist
        sons_in_playlist = [item[0] for item in self.playlist.list_son]
        self.assertNotIn(self.son3, sons_in_playlist)

        # Vérifier que les ordres sont mis à jour correctement
        expected_list_son = [[self.son1, 1], [self.son2, 2]]
        self.assertEqual(self.playlist.list_son, expected_list_son)

    def test_supprimer_tous_les_sons(self):
        # Suppression de tous les sons de la playlist un par un
        self.playlist.supprimer_son(self.son1)
        self.playlist.supprimer_son(self.son2)

        # Vérifier que la playlist est vide
        self.assertEqual(len(self.playlist.list_son), 0)

    def test_ordres_apres_suppressions_multiples(self):
        # Suppression de son2 puis son1
        self.playlist.supprimer_son(self.son2)
        self.playlist.supprimer_son(self.son1)

        # Vérifier que la playlist est vide après les suppressions
        self.assertEqual(len(self.playlist.list_son), 0)

    def test_repr_str_methods(self):
        # Tester la méthode __str__
        str_attendu = (
            "Playlist 'My Playlist' (ID: 1) by Utilisateur: user1:\n"
            "Liste des Sons:\n"
            "  Ordre 1: Son ID: 1, Nom: 'Son1', Tags: [tag1, tag2], Chemin: path1.mp3\n"
            "  Ordre 2: Son ID: 2, Nom: 'Son2', Tags: [tag3], Chemin: path2.mp3\n"
        )
        self.assertEqual(str(self.playlist), str_attendu)


if __name__ == "__main__":
    unittest.main()
