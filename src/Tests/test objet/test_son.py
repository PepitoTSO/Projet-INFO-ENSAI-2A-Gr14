import unittest
from Object.son import Son


class TestSon(unittest.TestCase):
    def test_str(self):
        '''
        Verifie que l'objet son a bien la repr associée
        '''
        objet = Son(1, "test", ["tag1", "tag2"])
        resultat = "Son ID: 1, Nom: 'test', Tags: [tag1, tag2], Chemin: data\\son\\1.mp3"
        self.assertEqual(str(objet), resultat)

    def test_initialisation_invalide_id_son(self):
        '''
        Test de la création d'un son avec un id_son invalide
        '''
        with self.assertRaises(TypeError):
            Son('1', "test", ["tag1", "tag2"])

    def test_initialisation_invalide_nom_son(self):
        '''
        Test de la création d'un son avec un nom_son invalide
        '''
        with self.assertRaises(TypeError):
            Son(1, 2, ["tag1", "tag2"])

    def test_initialisation_invalide_tags(self):
        '''
        Test de la création d'un son avec un tag invalide
        '''
        with self.assertRaises(TypeError):
            Son(1, "test", {1, "tag2"})
    
    def test_eq(self):
        pass


if __name__ == '__main__':
    unittest.main()
