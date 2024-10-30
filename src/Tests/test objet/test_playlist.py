import unittest
from Object.playlist import (
    Playlist,
)  # Assuming the main class is called Playlist
from Object.son import Son
from Object.utilisateur import Utilisateur


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        # Creating instances required for Playlist
        self.utilisateur = Utilisateur(
            "John Doe", "johndoe@example.com"
        )  # Example Utilisateur instance
        self.playlist = Playlist(self.utilisateur, 1, "My Playlist", {})

        # Creating some Son instances
        self.son1 = Son("Song 1", "Artist 1", 3.5)  # Example Son instance
        self.son2 = Son("Song 2", "Artist 2", 4.0)
        self.son3 = Son("Song 3", "Artist 3", 2.8)
        self.new_son = Son("New Song", "New Artist", 3.7)

    def test_ajouter_son_empty_playlist(self):
        """Test adding a son to an empty playlist."""
        self.playlist.ajouter_son(self.son1, 1)
        self.assertEqual(len(self.playlist.dict_son), 1)
        self.assertIn(1, self.playlist.dict_son)
        self.assertEqual(self.playlist.dict_son[1], self.son1)

    def test_ajouter_son_add_to_existing_order(self):
        """Test adding a son at an existing order and shifting others."""
        # Adding initial songs
        self.playlist.ajouter_son(self.son1, 1)
        self.playlist.ajouter_son(self.son2, 2)

        # Adding a new song at order 1, expecting other songs to shift
        self.playlist.ajouter_son(self.new_son, 1)
        self.assertEqual(len(self.playlist.dict_son), 3)
        self.assertEqual(self.playlist.dict_son[1], self.new_son)
        self.assertEqual(self.playlist.dict_son[2], self.son1)
        self.assertEqual(self.playlist.dict_son[3], self.son2)

    def test_ajouter_son_middle_of_playlist(self):
        """Test adding a son in the middle of an existing playlist."""
        # Adding initial songs
        self.playlist.ajouter_son(self.son1, 1)
        self.playlist.ajouter_son(self.son2, 2)
        self.playlist.ajouter_son(self.son3, 3)

        # Adding a new song at order 2, expecting subsequent songs to shift
        self.playlist.ajouter_son(self.new_son, 2)
        self.assertEqual(len(self.playlist.dict_son), 4)
        self.assertEqual(self.playlist.dict_son[1], self.son1)
        self.assertEqual(self.playlist.dict_son[2], self.new_son)
        self.assertEqual(self.playlist.dict_son[3], self.son2)
        self.assertEqual(self.playlist.dict_son[4], self.son3)

    def test_ajouter_son_order_already_exists(self):
        """Test adding a son at an existing order, ensuring correct behavior and shifting."""
        # Adding initial songs
        self.playlist.ajouter_son(self.son1, 1)
        self.playlist.ajouter_son(self.son2, 2)

        # Adding a new song at order 2, expecting existing song at order 2 to shift to order 3
        self.playlist.ajouter_son(self.new_son, 2)
        self.assertEqual(len(self.playlist.dict_son), 3)
        self.assertEqual(self.playlist.dict_son[1], self.son1)
        self.assertEqual(self.playlist.dict_son[2], self.new_son)
        self.assertEqual(self.playlist.dict_son[3], self.son2)

    def test_type_error_for_invalid_son(self):
        """Test that a TypeError is raised if the provided 'son' is not of type Son."""
        with self.assertRaises(TypeError):
            self.playlist.ajouter_son("Invalid Son", 1)

    def test_type_error_for_invalid_order(self):
        """Test that a TypeError is raised if the provided 'ordre' is not an int."""
        with self.assertRaises(TypeError):
            self.playlist.ajouter_son(self.son1, "Invalid Order")

    def test_value_error_for_duplicate_order(self):
        """Test adding a son at an already existing order when duplicates are not allowed."""
        # Adding initial song
        self.playlist.ajouter_son(self.son1, 1)

        # Adding another song at the same order without shifting should raise ValueError
        with self.assertRaises(ValueError):
            self.playlist.ajouter_son(self.son2, 1)


if __name__ == "__main__":
    unittest.main()
