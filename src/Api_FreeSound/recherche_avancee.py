from gensim.models import Word2Vec


def n_mots_similaires(mot, n):
    """
    Trouve les n mots les plus proches (dist cosinus) au mot.
    Params:
        mot : str
        n : int
    Return:
        list_mot : list
    """
    modele = Word2Vec.load("model_word2vec_restreint.model")
    mots_proches = modele.wv.most_similar(mot, topn=n)
    list_mot = []
    for i in range(n):
        list_mot.append(mots_proches[i][0])
    return list_mot
