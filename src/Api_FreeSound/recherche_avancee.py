import gensim.downloader as api


class recherche_avancee:

    def __init__(self, nom_modele="glove-wiki-gigaword-200"):
        if not isinstance(nom_modele, str):
            raise TypeError("Le nom du modele doit être un str")
        self.nom_modele = nom_modele
        self.modele = None

    def benchmark_modele(self):
        """
        Affiche la liste des modeles, le temps d'inference et le path du modele principal
        """
        # infos sur les modèles
        info = api.info()
        print(info["models"].keys())

        # la config np pour l'info hardware
        import numpy as np

        print(np.__config__.show())
        # le temps de recherche
        import time

        temps = time.time()
        recherche_avancee().n_mots_similaires("dragon")
        print("temps chargement et inférence : ", time.time() - temps)
        print("le modele est ici: ", api.load(self.nom_modele, return_path=True))

    def charger_modele(self):
        """
        Permet de charger le modele si besoin pour ne pas ralentir l'application inutilement
        donc ameliorer l'experience utilisateur
        """
        if self.modele is None:
            print("Chargement du modele. Merci de patienter...")
            self.modele = api.load(self.nom_modele)
        return self.modele

    def n_mots_similaires(self, mot: str, n=5):
        """
        Retourne les n couples mot-distance les plus proches du mot recherche selon le modèle

        Params:
            mot : str
        Un mot sur lequel fait une recherche par similarite
            n : int
        Le nombre de resultat

        Returns:
            res : list(str, int)
        Liste qui les couples mot-distance dans l'ordre décroissant
        """
        if not isinstance(mot, str):
            raise TypeError("La recherche doit être un mot")
        modele = self.charger_modele()
        n_mots_simil = modele.most_similar(mot, topn=n)
        res = []
        for mot, simil in n_mots_simil:
            res.append((mot, simil))
        return res


if __name__ == "__main__":
    recherche_avancee().benchmark_modele()
