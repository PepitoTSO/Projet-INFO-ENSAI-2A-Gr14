import unittest
from unittest.mock import patch, MagicMock
from DAO.utilisateur_DAO import Utilisateur_DAO
from Object.utilisateur import Utilisateur
from utils.reset_database import ResetDatabase


class TestUtilisateurDAO(unittest.TestCase):

    def setUp(self):
        # Réinitialiser la base de données avant chaque test
        ResetDatabase().lancer()

    # @patch('DAO.db_connection.DBConnection')
    # def test_creer_utilisateur(self, mock_db_connection):
    #     dao = Utilisateur_DAO()
    #     utilisateur = Utilisateur(pseudo='test', mdp_hache='hashed_password')

    #     mock_cursor = MagicMock()
    #     mock_db_connection().connection.__enter__.return_value.cursor.return_value.__enter__.return_value = mock_cursor

    #     # Appel de la méthode pour tester
    #     dao.creer_utilisateur(utilisateur)

    #     utilisateur_modifie = Utilisateur(pseudo='test', mdp_hache='quoicoubeh')
    #     dao.modifier_utilisateur(utilisateur, utilisateur_modifie)
    #     # Vous pouvez vérifier manuellement dans la base de données après l'exécution de ce test

    @patch('DAO.db_connection.DBConnection')
    def test_modifier_utilisateur(self, mock_db_connection):
        dao = Utilisateur_DAO()

        utilisateur = Utilisateur(pseudo='test', mdp_hache='hashed_password')
        utilisateur_modifie = Utilisateur(pseudo='test', mdp_hache='INSTAGRAM')

        # Créer d'abord l'utilisateur
        dao.creer_utilisateur(utilisateur)

        # Modifier ensuite l'utilisateur
        resultat = dao.se_connecter(utilisateur)
        print(resultat)
        # Vous pouvez vérifier manuellement dans la base de données après l'exécution de ce test
if __name__ == '__main__':
    unittest.main()
