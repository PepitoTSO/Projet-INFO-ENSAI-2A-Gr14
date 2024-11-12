import os
import pytest

from unittest.mock import patch

from DAO.son_DAO import Son_DAO
from Object.son import Son

from utils.reset_database import ResetDatabase


def test_trouver_par_id_existant():
    """Recherche par id d'un son existant"""

    # GIVEN
    id_son = 1

    # WHEN
    son = Son_DAO().get_son_by_id(id_son)

    # THEN
    assert son == Son(
        1, nom="Song 1", tags=["chill", "relax"], path_stockage="/path/to/song1"
    )


'''
def test_trouver_par_id_non_existant():
    """Recherche par id d'un son n'existant pas"""

    # GIVEN
    id_son = 9999999999999

    # WHEN
    son = Son_DAO().get_son_by_id(id_son)

    # THEN
    assert son is None
'''
'''
def test_lister_tous():
    """Vérifie que la méthode renvoie une liste de Son"""

    # GIVEN

    # WHEN
    sons = Son_DAO().get_all_son()

    # THEN
    assert isinstance(joueurs, list)
    for j in joueurs:
        assert isinstance(j, Joueur)
    assert len(joueurs) >= 2
'''

'''
def test_creer_ok():
    """Création de Joueur réussie"""

    # GIVEN
    joueur = Joueur(pseudo="gg", age=44, mail="test@test.io")

    # WHEN
    creation_ok = JoueurDao().creer(joueur)

    # THEN
    assert creation_ok
    assert joueur.id_joueur


def test_creer_ko():
    """Création de Joueur échouée (age et mail incorrects)"""

    # GIVEN
    joueur = Joueur(pseudo="gg", age="chaine de caractere", mail=12)

    # WHEN
    creation_ok = JoueurDao().creer(joueur)

    # THEN
    assert not creation_ok


def test_modifier_ok():
    """Modification de Joueur réussie"""

    # GIVEN
    new_mail = "maurice@mail.com"
    joueur = Joueur(id_joueur=997, pseudo="maurice", age=20, mail=new_mail)

    # WHEN
    modification_ok = JoueurDao().modifier(joueur)

    # THEN
    assert modification_ok


def test_modifier_ko():
    """Modification de Joueur échouée (id inconnu)"""

    # GIVEN
    joueur = Joueur(id_joueur=8888, pseudo="id inconnu", age=1, mail="no@mail.com")

    # WHEN
    modification_ok = JoueurDao().modifier(joueur)

    # THEN
    assert not modification_ok


def test_supprimer_ok():
    """Suppression de Joueur réussie"""

    # GIVEN
    joueur = Joueur(id_joueur=995, pseudo="miguel", age=1, mail="miguel@projet.fr")

    # WHEN
    suppression_ok = JoueurDao().supprimer(joueur)

    # THEN
    assert suppression_ok


def test_supprimer_ko():
    """Suppression de Joueur échouée (id inconnu)"""

    # GIVEN
    joueur = Joueur(id_joueur=8888, pseudo="id inconnu", age=1, mail="no@z.fr")

    # WHEN
    suppression_ok = JoueurDao().supprimer(joueur)

    # THEN
    assert not suppression_ok


def test_se_connecter_ok():
    """Connexion de Joueur réussie"""

    # GIVEN
    pseudo = "batricia"
    mdp = "9876"

    # WHEN
    joueur = JoueurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    # THEN
    assert isinstance(joueur, Joueur)


def test_se_connecter_ko():
    """Connexion de Joueur échouée (pseudo ou mdp incorrect)"""

    # GIVEN
    pseudo = "toto"
    mdp = "poiuytreza"

    # WHEN
    joueur = JoueurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    # THEN
    assert not joueur
'''

if __name__ == "__main__":
    pytest.main([__file__])
