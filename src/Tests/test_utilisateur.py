import unittest
from Object.utilisateur import Utilisateur


class TestUtilisateur(unittest.TestCase):

    def test_initialisation_valide(self):
        """Test de la création d'un utilisateur avec des valeurs valides"""
        utilisateur = Utilisateur("johndoe", "hashed_password")
        self.assertEqual(utilisateur.pseudo, "johndoe")
        self.assertEqual(utilisateur.mdp_hache, "hashed_password")

    def test_initialisation_invalide_pseudo(self):
        """Test de la création d'un utilisateur avec un pseudo invalide"""
        with self.assertRaises(TypeError):
            Utilisateur(12345, "hashed_password")  # Pseudo doit être une chaîne de caractères

    def test_initialisation_invalide_mdp(self):
        """Test de la création d'un utilisateur avec un mot de passe invalide"""
        with self.assertRaises(TypeError):
            Utilisateur("johndoe", 12345)  # Mot de passe doit être une chaîne de caractères

    def test_initialisation_invalide_pseudo_et_mdp(self):
        """Test de la création d'un utilisateur avec un pseudo et un mot de passe invalides"""
        with self.assertRaises(TypeError):
            Utilisateur(12345, 67890)  # Les deux doivent être des chaînes de caractères

    def test_str(self):
        """Test de la méthode __str__"""
        utilisateur = Utilisateur("johndoe", "hashed_password")
        self.assertEqual(str(utilisateur), "Utilisateur: johndoe")

if __name__ == '__main__':
    unittest.main()
