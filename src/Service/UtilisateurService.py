from Object.utilisateur import Utilisateur
from DAO.utilisateur_DAO import Utilisateur_DAO
from view.session import Session
import hashlib


class UtilisateurService:
    """
    Permet de gérer les différents services liés à l'utilisateur.

    Attributes
    ----------
    None
    """

    def se_connecter(self, mdp_nh: str, pseudo_utilisateur: str):
        """
        Permet à un utilisateur de se connecter

        Parameters
        ----------
        mdp_nh : str
            Le mot de passe non haché de l'utilisateur.
        pseudo_utilisateur : str
            Le pseudo de l'utilisateur.

        Returns
        -------
        bool
            `True` si la connexion est réussie, `False` sinon.
        """

        if not isinstance(mdp_nh, str):
            raise TypeError("Le mdp non haché doit être de type str.")
        if not isinstance(pseudo_utilisateur, str):
            raise TypeError("Le pseudo doit être de type str.")
        mdp_hache = self.hacher_mot_de_passe(mdp_nh)
        user = Utilisateur(pseudo=pseudo_utilisateur, mdp_hache=mdp_hache)
        utilisateurDAO = Utilisateur_DAO()
        reponse = utilisateurDAO.se_connecter(user)
        if reponse is True:
            Session().utilisateur = user
            return True
        return False

    def hacher_mot_de_passe(self, mdp_nh: str):
        """
        Hache le mot de passe avec sel.

        Parameters
        ----------
        mdp_nh : str
            Le mot de passe non haché de l'utilisateur.

        Returns
        -------
        str
            Le mot de passe haché.
        """

        if not isinstance(mdp_nh, str):
            raise TypeError("Le mdp non haché doit être de type str.")
        sel = "matae_projet"
        mot_de_passe_sale = sel + mdp_nh
        mdp_hache = hashlib.sha256(mot_de_passe_sale.encode()).hexdigest()
        return mdp_hache

    def creer_utilisateur(self, mdp_nh, pseudo_utilisateur):
        """
        Permet de créer un nouvel utilisateur.

        Parameters
        ----------
        mdp_nh : str
            Le mot de passe non haché de l'utilisateur.
        pseudo_utilisateur : str
            Le pseudo de l'utilisateur.

        Returns
        -------
        bool
            `True` si la création en BDD est réussie, `False` sinon.
        """
        if not isinstance(mdp_nh, str):
            raise TypeError("Le mdp non haché doit être de type str.")
        if not isinstance(pseudo_utilisateur, str):
            raise TypeError("Le pseudo doit être de type str.")

        mdp_hache = self.hacher_mot_de_passe(mdp_nh=mdp_nh)
        new_user = Utilisateur(mdp_hache=mdp_hache, pseudo=pseudo_utilisateur)

        utilisateurDAO = Utilisateur_DAO()
        return utilisateurDAO.creer_utilisateur(new_user)

    def deconnecter_utilisateur(self):
        """
        Permet à un utilisateur de se déconnecter

        Parameters
        ----------

        Returns
        -------
        Modifie l'utilisateur de l'objet Session
        """

        Session.utilisateur = None

    def modifier_utilisateur(self, pseudo_utilisateur: str, nouveau_mdp_nh: str):
        """
        Permet de modifier un utilisateur. Même si c'est plutôt pour le mdp,
        On peut aussi modifier le pseudo.

        Parameters
        ----------
        pseudo_utilisateur : str
            Le (nouveau) pseudo de l'utilisateur

        nouveau_mdp : str
            Le nouveau mot de passe non-haché.

        Returns
        -------
        bool
            `True` si la modification en BDD est réussie, `False` sinon.
        """

        if not isinstance(nouveau_mdp_nh, str):
            raise TypeError("Le mdp non haché doit être de type str.")
        if not isinstance(pseudo_utilisateur, str):
            raise TypeError("Le pseudo doit être de type str.")

        if Session.utilisateur is not None:
            ancien_utilisateur = Utilisateur(
                pseudo=Session.utilisateur.pseudo,
                mdp_hache=Session.utilisateur.mdp_hache,
            )
            mdp_hache = self.hacher_mot_de_passe(nouveau_mdp_nh)

            # Correction : utilisation de 'mdp_hache' au lieu de 'mot_de_passe_hache'
            Session.utilisateur.mdp_hache = mdp_hache
            Session.utilisateur.pseudo = pseudo_utilisateur

            user_modif = Utilisateur(pseudo=pseudo_utilisateur, mdp_hache=mdp_hache)

            # Modification de l'utilisateur dans la BDD
            reponse = Utilisateur_DAO.modifier_utilisateur(
                ancien_utilisateur, user_modif
            )

            return reponse  # Retourner le résultat de la modification
        else:
            return False  # Si aucun utilisateur n'est connecté, retournez False
