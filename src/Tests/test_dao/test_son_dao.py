import unittest
from unittest.mock import patch, MagicMock
from Object.son import Son
from DAO.son_DAO import Son_DAO


class TestSonDAO(unittest.TestCase):
    @patch("DAO.son_DAO.DBConnection")
    def test_ajouter_son(self, MockDBConnection):
        """
        Test adding a new son to the database.
        """
        # Create a mock cursor with context manager behavior
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {"id_son": 1}
        mock_cursor.__enter__.return_value = mock_cursor

        # Create a mock connection with context manager behavior
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connection.__enter__.return_value = mock_connection

        # Mock the DBConnection to return our mock connection
        MockDBConnection.return_value.connection.__enter__.return_value = (
            mock_connection
        )

        # Create a Son object
        son = Son(
            id_son=1,
            nom="Test Son",
            tags=["rock", "pop"],
            path_stockage="/music/test.mp3",
        )

        # Call ajouter_son
        dao = Son_DAO()
        result = dao.ajouter_son(son)

        # Assert that it returned True
        self.assertTrue(result)

        # Assert that execute was called with the correct SQL and parameters
        mock_cursor.execute.assert_called_with(
            """
                            INSERT INTO bdd.son (nom_son, tags, path_stockage)
                            VALUES (%s, %s, %s)
                            RETURNING id_son;
                            """,
            ("Test Son", "rock, pop", "/music/test.mp3"),
        )

    @patch("DAO.son_DAO.DBConnection")
    def test_get_son_by_id(self, MockDBConnection):
        """
        Test getting a son by id.
        """
        # Create a mock cursor with context manager behavior
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {
            "id_son": 1,
            "nom_son": "Test Son",
            "tags": "rock, pop",
            "path_stockage": "/music/test.mp3",
        }
        mock_cursor.__enter__.return_value = mock_cursor

        # Create a mock connection with context manager behavior
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connection.__enter__.return_value = mock_connection

        # Mock the DBConnection to return our mock connection
        MockDBConnection.return_value.connection.__enter__.return_value = (
            mock_connection
        )

        # Call get_son_by_id
        dao = Son_DAO()
        son = dao.get_son_by_id(1)

        # Assert that a Son object is returned and its properties match
        self.assertIsNotNone(son)
        self.assertEqual(son.id_son, 1)
        self.assertEqual(son.nom, "Test Son")
        self.assertEqual(son.tags, ["rock", "pop"])
        self.assertEqual(str(son.path_stockage), "/music/test.mp3")

    @patch("DAO.son_DAO.DBConnection")
    def test_get_all_son(self, MockDBConnection):
        """
        Test getting all sons from the database.
        """
        # Create a mock cursor with context manager behavior
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {
                "id_son": 1,
                "nom_son": "Test Son 1",
                "tags": "rock, pop",
                "path_stockage": "/music/test1.mp3",
            },
            {
                "id_son": 2,
                "nom_son": "Test Son 2",
                "tags": "jazz",
                "path_stockage": "/music/test2.mp3",
            },
        ]
        mock_cursor.__enter__.return_value = mock_cursor

        # Create a mock connection with context manager behavior
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connection.__enter__.return_value = mock_connection

        # Mock the DBConnection to return our mock connection
        MockDBConnection.return_value.connection.__enter__.return_value = (
            mock_connection
        )

        # Call get_all_son
        dao = Son_DAO()
        sons = dao.get_all_son()

        # Assert that the correct number of Son objects are returned
        self.assertEqual(len(sons), 2)
        self.assertEqual(sons[0].nom, "Test Son 1")
        self.assertEqual(sons[1].tags, ["jazz"])

    @patch("DAO.son_DAO.DBConnection")
    def test_supprimer_son(self, MockDBConnection):
        """
        Test deleting a son by id.
        """
        # Create a mock cursor with context manager behavior
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1  # Simulate one row deleted
        mock_cursor.__enter__.return_value = mock_cursor

        # Create a mock connection with context manager behavior
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connection.__enter__.return_value = mock_connection

        # Mock the DBConnection to return our mock connection
        MockDBConnection.return_value.connection.__enter__.return_value = (
            mock_connection
        )

        # Call supprimer_son
        dao = Son_DAO()
        result = dao.supprimer_son(1)

        # Assert that it returned True
        self.assertTrue(result)

        # Assert that execute was called with the correct SQL and parameters
        mock_cursor.execute.assert_called_with(
            "DELETE FROM bdd.son WHERE id_son = %s",
            (1,),
        )

    @patch("DAO.son_DAO.DBConnection")
    def test_get_all_son_ordre_by_id_playlist(self, MockDBConnection):
        """
        Test getting all sons from a specified playlist along with their order.
        """
        # Create a mock cursor with context manager behavior
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {
                "id_son": 1,
                "nom_son": "Test Son 1",
                "tags": "rock, pop",
                "path_stockage": "/music/test1.mp3",
                "ordre_son_playlist": 1,
            },
            {
                "id_son": 2,
                "nom_son": "Test Son 2",
                "tags": "jazz",
                "path_stockage": "/music/test2.mp3",
                "ordre_son_playlist": 2,
            },
        ]
        mock_cursor.__enter__.return_value = mock_cursor

        # Create a mock connection with context manager behavior
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connection.__enter__.return_value = mock_connection

        # Mock the DBConnection to return our mock connection
        MockDBConnection.return_value.connection.__enter__.return_value = (
            mock_connection
        )

        # Call get_all_son_ordre_by_id_playlist
        dao = Son_DAO()
        sons = dao.get_all_son_ordre_by_id_playlist(1)

        # Assert that the correct number of sons are returned
        self.assertEqual(len(sons), 2)
        self.assertEqual(sons[0][0].nom, "Test Son 1")
        self.assertEqual(sons[0][1], 1)
        self.assertEqual(sons[1][0].nom, "Test Son 2")
        self.assertEqual(sons[1][1], 2)


if __name__ == "__main__":
    unittest.main()
