from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')

#Construction corpus
with open("corpus.txt", "r", encoding='utf-8') as file:
    data = list(line.strip() for line in file)
corpus = data
corpus_token = [word_tokenize(phrase.lower()) for phrase in corpus]

# Entraînement du modele
model = Word2Vec(sentences=corpus_token,  # Corpus tokenisé
                 vector_size=100,             # Taille des vecteurs d'embedding
                 window=5,                    # Taille de la fenêtre de contexte
                 min_count=1,                 # Ignorer les mots qui apparaissent moins de 1 fois
                 workers=8,                   # Nombre de threads pour l'entraînement
                 sg=1)                        # Utiliser skip-gram (1) ou CBOW (0)

#Sauvegarde
model.save("model_word2vec_restreint.model")
