import unittest
from unittest.mock import patch, MagicMock
from DAO.son_DAO import Son_DAO
from Service.SonService import sonService
from Object.son import Son
from utils.reset_database import ResetDatabase

class TestSonDAO():
    def test_ajout():
        pass


class TestSon():
    def test_def():
        '''
        Verifie que l'objet son a bien la repr associée
        '''
        objet = Son(1,"test",["tag1","tag2"])
        resultat = "Son ID: 1, Nom: test, Tags: [tag1,tag2], Chemin: None"
        self.assertEqual(repr(objet),resultat)

class TestSonService():
    def test_play():
        pass

if __name__ == '__main__':
    unittest.main()