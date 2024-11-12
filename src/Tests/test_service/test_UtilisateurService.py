import unittest
from unittest.mock import patch
from Object.utilisateur import Utilisateur
from view.session import Session
from Service.UtilisateurService import UtilisateurService


class TestUtilisateurService(unittest.TestCase):

    def setUp(self):
        self.service = UtilisateurService()
        Session.utilisateur = None  # Reset session utilisateur before each test

    @patch("Service.UtilisateurService.Utilisateur_DAO.se_connecter")
    @patch.object(UtilisateurService, "hacher_mot_de_passe")
    def test_se_connecter_success(self, mock_hacher_mot_de_passe, mock_se_connecter):
        mock_hacher_mot_de_passe.return_value = "hashed_password"
        mock_se_connecter.return_value = True

        mdp_nh = "password"
        pseudo_utilisateur = "username"
        result = self.service.se_connecter(mdp_nh, pseudo_utilisateur)

        mock_hacher_mot_de_passe.assert_called_once_with(mdp_nh)
        mock_se_connecter.assert_called_once()

        # Vérifications des attributs
        self.assertEqual(Session.utilisateur.pseudo, pseudo_utilisateur)
        self.assertEqual(Session.utilisateur.mdp_hache, "hashed_password")
        self.assertTrue(result)

    @patch("Service.UtilisateurService.Utilisateur_DAO.se_connecter")
    @patch.object(UtilisateurService, "hacher_mot_de_passe")
    def test_se_connecter_failure(self, mock_hacher_mot_de_passe, mock_se_connecter):
        mock_hacher_mot_de_passe.return_value = "hashed_password"
        mock_se_connecter.return_value = False

        mdp_nh = "password"
        pseudo_utilisateur = "username"
        result = self.service.se_connecter(mdp_nh, pseudo_utilisateur)

        mock_hacher_mot_de_passe.assert_called_once_with(mdp_nh)
        mock_se_connecter.assert_called_once()

        # Vérifications
        self.assertIsNone(Session.utilisateur)
        self.assertFalse(result)

    def test_se_connecter_invalid_password_type(self):
        with self.assertRaises(TypeError):
            self.service.se_connecter(12345, "username")

    def test_se_connecter_invalid_username_type(self):
        with self.assertRaises(TypeError):
            self.service.se_connecter("password", 12345)

    @patch("Service.UtilisateurService.Utilisateur_DAO.creer_utilisateur")
    @patch.object(UtilisateurService, "hacher_mot_de_passe")
    def test_creer_utilisateur_success(
        self, mock_hacher_mot_de_passe, mock_creer_utilisateur
    ):
        mock_hacher_mot_de_passe.return_value = "hashed_password"
        mock_creer_utilisateur.return_value = True

        mdp_nh = "password"
        pseudo_utilisateur = "new_user"
        result = self.service.creer_utilisateur(mdp_nh, pseudo_utilisateur)

        # Vérification des appels
        mock_hacher_mot_de_passe.assert_called_once_with(
            mdp_nh=mdp_nh
        )  # Ici, vous devez passer le nom de l'argument
        mock_creer_utilisateur.assert_called_once()

        # Vérifications de l'objet Utilisateur attendu
        utilisateur_attendu = Utilisateur(
            pseudo=pseudo_utilisateur, mdp_hache="hashed_password"
        )
        args, _ = mock_creer_utilisateur.call_args
        self.assertEqual(args[0].pseudo, utilisateur_attendu.pseudo)
        self.assertEqual(args[0].mdp_hache, utilisateur_attendu.mdp_hache)

        self.assertTrue(result)

    @patch(
        "Service.UtilisateurService.Utilisateur_DAO.creer_utilisateur"
    )  # Patch sur la méthode correcte
    @patch.object(UtilisateurService, "hacher_mot_de_passe")
    def test_creer_utilisateur_failure(
        self, mock_hacher_mot_de_passe, mock_creer_utilisateur
    ):
        # Mock des retours
        mock_hacher_mot_de_passe.return_value = "hashed_password"
        mock_creer_utilisateur.return_value = False  # Faux pour simuler un échec

        mdp_nh = "password"
        pseudo_utilisateur = "new_user"

        # Appel de la méthode avec les bons arguments
        result = self.service.creer_utilisateur(mdp_nh, pseudo_utilisateur)

        # Vérifications
        mock_hacher_mot_de_passe.assert_called_once_with(mdp_nh=mdp_nh)

        # Vérifier que la méthode 'creer_utilisateur' a été appelée avec un objet Utilisateur ayant les bons attributs
        utilisateur_attendu = Utilisateur(
            pseudo=pseudo_utilisateur, mdp_hache="hashed_password"
        )

        # On récupère les arguments passés à mock_creer_utilisateur
        args, _ = (
            mock_creer_utilisateur.call_args
        )  # Obtenir les arguments passés lors de l'appel

        # Comparer les attributs de l'objet Utilisateur passé
        self.assertEqual(args[0].pseudo, utilisateur_attendu.pseudo)
        self.assertEqual(args[0].mdp_hache, utilisateur_attendu.mdp_hache)

        self.assertFalse(result)

    def test_creer_utilisateur_invalid_password_type(self):
        with self.assertRaises(TypeError):
            self.service.creer_utilisateur(12345, "new_user")

    def test_creer_utilisateur_invalid_username_type(self):
        with self.assertRaises(TypeError):
            self.service.creer_utilisateur("password", 12345)

    def test_deconnecter_utilisateur(self):
        Session.utilisateur = Utilisateur(
            pseudo="username", mdp_hache="hashed_password"
        )
        self.service.deconnecter_utilisateur()
        self.assertIsNone(Session.utilisateur)

    @patch("Service.UtilisateurService.Utilisateur_DAO.modifier_utilisateur")
    @patch.object(UtilisateurService, "hacher_mot_de_passe")
    def test_modifier_utilisateur_success(
        self, mock_hacher_mot_de_passe, mock_modifier_utilisateur
    ):
        mock_hacher_mot_de_passe.return_value = "new_hashed_password"
        mock_modifier_utilisateur.return_value = True

        Session.utilisateur = Utilisateur(
            pseudo="old_user", mdp_hache="old_hashed_password"
        )
        pseudo_utilisateur = "new_user"
        nouveau_mdp_nh = "new_password"
        result = self.service.modifier_utilisateur(pseudo_utilisateur, nouveau_mdp_nh)

        mock_hacher_mot_de_passe.assert_called_once_with(nouveau_mdp_nh)
        mock_modifier_utilisateur.assert_called_once()

        # Vérifications des attributs
        self.assertEqual(Session.utilisateur.pseudo, pseudo_utilisateur)
        self.assertEqual(Session.utilisateur.mdp_hache, "new_hashed_password")
        self.assertTrue(result)

    @patch("Service.UtilisateurService.Utilisateur_DAO.modifier_utilisateur")
    @patch.object(UtilisateurService, "hacher_mot_de_passe")
    def test_modifier_utilisateur_failure(
        self, mock_hacher_mot_de_passe, mock_modifier_utilisateur
    ):
        mock_hacher_mot_de_passe.return_value = "new_hashed_password"
        mock_modifier_utilisateur.return_value = False

        Session.utilisateur = Utilisateur(
            pseudo="old_user", mdp_hache="old_hashed_password"
        )
        pseudo_utilisateur = "new_user"
        nouveau_mdp_nh = "new_password"
        result = self.service.modifier_utilisateur(pseudo_utilisateur, nouveau_mdp_nh)

        mock_hacher_mot_de_passe.assert_called_once_with(nouveau_mdp_nh)
        mock_modifier_utilisateur.assert_called_once()

        # Vérifications
        self.assertFalse(result)

    def test_modifier_utilisateur_invalid_password_type(self):
        with self.assertRaises(TypeError):
            self.service.modifier_utilisateur("new_user", 12345)

    def test_modifier_utilisateur_invalid_username_type(self):
        with self.assertRaises(TypeError):
            self.service.modifier_utilisateur(12345, "new_password")


if __name__ == "__main__":
    unittest.main()
