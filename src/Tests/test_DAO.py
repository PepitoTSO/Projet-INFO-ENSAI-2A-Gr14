import unittest
from unittest.mock import patch, MagicMock
from DAO.utilisateur_DAO import Utilisateur_DAO
from Object.utilisateur import Utilisateur
from utils.reset_database import ResetDatabase
from Object.playlist import Playlist
from DAO.playlist_DAO import Playlist_DAO

utilisateur = Utilisateur("user1", "hashed_password1")
playlist = Playlist(utilisateur, "Playlist test none", None, [[]])

Playlist_DAO().ajouter_playlist(playlist)
