from src.Object.son import Son
import unittest


class TestSon(unittest.TestCase):

    def test_repr():

    #Given
        son1=Son(999,"pop",("sympa","dance"))
    #When
        repr_son1 = 'id_son=999,nom="pop",caracteristiques=("sympa","dance")'
    #Then
        self.assertEqual(repr_son1,repr(son1))


if __name__ == "__main__":
    unittest.main()