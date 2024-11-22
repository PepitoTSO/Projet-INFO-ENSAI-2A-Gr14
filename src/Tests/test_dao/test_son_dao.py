import pytest
from DAO.son_DAO import Son_DAO
from Object.son import Son


def test_trouver_par_id_existant():
    """Recherche par id d'un son existant"""

    # GIVEN
    son = Son(1, nom="Song 1", tags=["chill", "relax"], path_stockage="/path/to/song1")
    Son_DAO().ajouter_son(son)
    id_son1 = 1

    # WHEN
    son = Son_DAO().get_son_by_id(id_son1)

    # THEN
    expected_son = Son(
        1, nom="Song 1", tags=["chill", "relax"], path_stockage="/path/to/song1"
    )

    assert son.id_son == expected_son.id_son
    assert son.nom == expected_son.nom
    assert son.tags == expected_son.tags
    assert son.path_stockage == expected_son.path_stockage


def test_trouver_par_id_non_existant():
    """Recherche par id d'un son n'existant pas"""

    # GIVEN
    id_son = 9999999999999

    # WHEN
    son = Son_DAO().get_son_by_id(id_son)

    # THEN
    assert son is None


def test_lister_tous():
    """Vérifie que la méthode renvoie une liste de Son"""

    # GIVEN

    # WHEN
    sons = Son_DAO().get_all_son()

    # THEN
    assert isinstance(sons, list)
    for s in sons:
        assert isinstance(s, Son)


def test_supprimer_son_existant():
    """Suppression d'un son existant réussie"""

    # GIVEN
    id_son = 1

    # WHEN
    suppression_ok = Son_DAO().supprimer_son(id_son)

    # THEN
    assert suppression_ok


def test_ajouter_ok():
    """Création de Son réussie"""

    # GIVEN
    son = Son(13, nom="Song 1", tags=["chill", "relax"], path_stockage="/path/to/song1")

    # WHEN
    creation_ok = Son_DAO().ajouter_son(son)

    # THEN
    assert creation_ok


def test_supprimer_son_existant2():
    """Suppression d'un son existant réussie"""

    # GIVEN
    id_son = 13

    # WHEN
    suppression_ok = Son_DAO().supprimer_son(id_son)

    # THEN
    assert suppression_ok


def test_supprimer_son_non_existant():
    """Suppression d'un son échouée (id non existant)"""

    # GIVEN
    id_son = 9999999999999

    # WHEN
    suppression_ok = Son_DAO().supprimer_son(id_son)

    # THEN
    assert not suppression_ok


def test_get_son_by_name_existant():
    """Recherche par nom d'un son existant"""

    # GIVEN
    name_son = "Song 1"

    # WHEN
    son = Son_DAO().get_son_by_name(name_son)

    # THEN
    expected_son = Son(
        1, nom="Song 1", tags=["chill", "relax"], path_stockage="/path/to/song1"
    )

    assert son.id_son == expected_son.id_son
    assert son.nom == expected_son.nom
    assert son.tags == expected_son.tags
    assert son.path_stockage == expected_son.path_stockage


def test_get_son_by_name_non_existant():
    """Recherche par nom d'un son non existant"""

    # GIVEN
    name_son = "Nom qui n'existe pas"

    # WHEN
    son = Son_DAO().get_son_by_name(name_son)

    # THEN
    assert son is None


def test_get_all_son_ordre_by_id_playlist_existant():
    """Récupération des sons par ordre d'une playlist existante"""

    # GIVEN
    id_playlist = 1

    # WHEN
    sons = Son_DAO().get_all_son_ordre_by_id_playlist(id_playlist)

    # THEN
    assert isinstance(sons, list)
    for s in sons:
        assert isinstance(s, list)
        assert isinstance(s[0], Son)
        assert isinstance(s[1], int)  # L'ordre doit être un entier


def test_get_all_son_ordre_by_id_playlist_non_existant():
    """Récupération échouée des sons d'une playlist qui n'existe pas"""

    # GIVEN
    id_playlist = 9999999999

    # WHEN
    sons = Son_DAO().get_all_son_ordre_by_id_playlist(id_playlist)

    # THEN
    assert sons == []


if __name__ == "__main__":
    pytest.main([__file__])
