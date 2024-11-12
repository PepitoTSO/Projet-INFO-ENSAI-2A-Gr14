class Utilisateur:
    """
    Permet de créer l'objet métier Utilisateur.

    Attributes
    ----------
    pseudo : str
        Le pseudo de l'utilisateur.
    mdp_hache : str
        Le mot de passe haché de l'utilisateur.
    """

    def __init__(self, pseudo: str, mdp_hache: str):
        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo n'est pas de type str.")
        if not isinstance(mdp_hache, str):
            raise TypeError("Le mdp n'est pas de type str.")

        self.pseudo = pseudo
        self.mdp_hache = mdp_hache

    def __str__(self):
        return f"Utilisateur: {self.pseudo}"
