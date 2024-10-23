import pytest
from src.Object.utilisateur import Utilisateur
from src.Object.son import Son
from src.Object.playlist import Playlist


@pytest.fixture
def utilisateur():
    return Utilisateur(1, "2022-01-01", "2022-01-02", [])


@pytest.fixture
def son1():
    return Son(1, "Song 1", "Caracteristiques 1")


@pytest.fixture
def son2():
    return Son(2, "Song 2", "Caracteristiques 2")


@pytest.fixture
def playlist(utilisateur):
    return Playlist(utilisateur, 1, "Playlist 1", [])


def test_ajouter_son(playlist, son1):
    # GIVEN
    son = son1
    ordre = 1

    # WHEN
    playlist.ajouter_son(son, ordre)

    # THEN
    assert len(playlist.list_son) == 1
    assert playlist.list_son[0][0] == son
    assert playlist.list_son[0][1] == ordre


def test_supprimer_son(playlist, son1):
    # GIVEN
    son = son1
    playlist.list_son = [[son, 1]]

    # WHEN
    playlist.supprimer_son(son)

    # THEN
    assert len(playlist.list_son) == 0


def test_changer_ordre(playlist, son1):
    # GIVEN
    son = son1
    ordre = 2
    playlist.list_son = [[son, 1]]

    # WHEN
    playlist.changer_ordre(son, ordre)

    # THEN
    assert len(playlist.list_son) == 1
    assert playlist.list_son[0][0] == son
    assert playlist.list_son[0][1] == ordre


def test_changer_nom_playlist(playlist):
    # GIVEN
    nouveau_nom = "New Playlist Name"

    # WHEN
    playlist.changer_nom_playlist(nouveau_nom)

    # THEN
    assert playlist.nom_playlist == nouveau_nom
