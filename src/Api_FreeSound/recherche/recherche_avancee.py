from apifreesound import apifreesound
from gensim.models import Word2Vec


def mots_similaires(mot, n):
    '''
    Trouve les n mots les plus proches (dist cosinus) au mot.
    Params:
        mot : str
        n : int
    Return:
        list_mot : list
    '''
    modele = Word2Vec.load("model_word2vec_restreint.model")
    mots_proches = modele.wv.most_similar(mot, topn=n)
    list_mot = []
    for i in range(n):
        list_mot.append(mots_proches[i][0])
    return list_mot

def recherche_avance(mot, n=5):
    '''
    Recherche sur les n mots les plus proches du mot
    Params:
        mot : str
        n : int
    Returns:
        res : list
    '''
    m_simil = mots_similaires(mot, n)
    res = []
    for i in range(n):
        mot_recherche = m_simil[i]
        recherche = apifreesound().recherche_son(mot_recherche)
        res.append(recherche)
    return res

