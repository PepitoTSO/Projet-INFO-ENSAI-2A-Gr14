from Object.utilisateur import Utilisateur
from DAO.utilisateur_DAO import Utilisateur_DAO
from view.session import Session
import hashlib


class UtilisateurService:

    def se_connecter(self, mdp_nh: str, pseudo_utilisateur: str):
        mdp_hache = self.hacher_mot_de_passe(mdp_nh)
        user = Utilisateur(pseudo=pseudo_utilisateur, mdp_hache=mdp_hache)
        reponse = Utilisateur_DAO.se_connecter(user)
        if reponse:
            Session.utilisateur = user
        return reponse

    def hacher_mot_de_passe(self, mdp_nh: str):
        sel = "matae_projet"
        mot_de_passe_sale = sel + mdp_nh
        mdp_hache = hashlib.sha256(mot_de_passe_sale.encode()).hexdigest()
        return mdp_hache

    def creer_utilisateur(self, mdp_nh, pseudo_utilisateur):
        mdp_hache = self.hacher_mot_de_passe(mdp_nh=mdp_nh)
        new_user = Utilisateur(mdp_hache=mdp_hache, pseudo=pseudo_utilisateur)

        return Utilisateur_DAO.creer_utilisateur(new_user)

    def deconnecter_utilisateur(self):

        Session.utilisateur = None

    def modifier_utilisateur(self, pseudo_utilisateur: str, nouveau_mdp_nh: str):
        """Modifie les détails de l'utilisateur courant."""
        if Session.utilisateur is not None:
            ancien_utilisateur = Utilisateur(
                pseudo=Session.utilisateur.pseudo,
                mdp_hache=Session.utilisateur.mdp_hache,
            )
            mdp_hache = self.hacher_mot_de_passe(nouveau_mdp_nh)
            Session.utilisateur.mot_de_passe_hache = mdp_hache
            Session.utilisateur.pseudo = pseudo_utilisateur

            user_modif = Utilisateur(pseudo=pseudo_utilisateur, mdp_hache=mdp_hache)
            reponse = Utilisateur_DAO.modifier_utilisateur(ancien_utilisateur, user_modif)
        return reponse
