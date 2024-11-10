import unittest
from Object.son import Son


class TestSon(unittest.TestCase):
    def test_def(self):
        '''
        Verifie que l'objet son a bien la repr associée
        '''
        objet = Son(1, "test", ["tag1", "tag2"])
        resultat = "Son ID: 1, Nom: test, Tags: [tag1,tag2], Chemin: None"
        self.assertEqual(repr(objet), resultat)


if __name__ == '__main__':
    unittest.main()
