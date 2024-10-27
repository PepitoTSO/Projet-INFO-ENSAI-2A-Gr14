from src.Object.utilisateur import Utilisateur
from view.session import Session
import hashlib


class UtilisateurService:

    def se_connecter(self, mdp_nh : str, pseudo_utilisateur : str):
        mdp_hache = self.hacher_mot_de_passe(mdp_nh)
        user = Utilisateur(pseudo = pseudo_utilisateur, mdp_hache = mdp_hache)
        reponse = user.se_connecter()
        if reponse:
            Session.utilisateur = user
        return reponse

    def hacher_mot_de_passe(self, mdp_nh : str):
        sel = "matae_projet"
        mot_de_passe_sale = sel + mdp_nh
        mdp_hache = hashlib.sha256(mot_de_passe_sale.encode()).hexdigest()
        return mdp_hache

    def creer_utilisateur(self, mdp_nh, pseudo_utilisateur):
        mdp_hache = self.hacher_mot_de_passe(mdp_nh = mdp_nh)
        new_user = Utilisateur(mdp_hache = mdp_hache, pseudo = pseudo_utilisateur)

        return new_user.creer_utilisateur()

    def deconnecter_utilisateur(self):

        Session.utilisateur = None

    def modifier_utilisateur(self, pseudo_utilisateur: str, nouveau_mdp_nh: str):
        """Modifie les détails de l'utilisateur courant."""
        if Session.utilisateur is not None:
            mdp_hache = self.hacher_mot_de_passe(nouveau_mdp_nh)
            Session.utilisateur.mot_de_passe_hache = mdp_hache
            Session.utilisateur.pseudo = pseudo_utilisateur

            user_modif = Utilisateur(pseudo= pseudo_utilisateur, mdp_hache= mdp_hache)
            reponse = user_modif.modifier_utilisateur()
        return reponse





    def __init__(self, utilisateur: Utilisateur):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")

        self.utilisateur = utilisateur

    def generer_sel() -> str:
        """Génère un sel aléatoire pour sécuriser le mot de passe."""
        return os.urandom(16).hex()

    def hash_mdp(mdp: str, sel: str) -> str:
        """Hache un mot de passe avec un sel en utilisant SHA-256."""
        mdp_sel = (mdp + sel).encode(
            "utf-8"
        )  # Combine le mot de passe et le sel, puis encode en bytes
        hachage = hashlib.sha256(
            mdp_sel
        ).hexdigest()  # Hache le mot de passe + sel avec SHA-256
        return hachage

    def creer_utilisateur(self, pseudo: str, mdp: str):

        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être un str")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être un str")

        pseudo_input = input("Entrez votre pseudo: ")
        mdp_input = input("Entrez votre mot de passe: ")
        sel = generer_sel()  # Générer un sel aléatoire
        mdp_hash = hash_mdp(mdp, sel)
        utilisateur = Utilisateur(pseudo, mdp_hash)
        Utilisateur_DAO().ajouter_utilisateur(utilisateur)

    def supprimer_utilisateur(self, id_utilisateur: int):

        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant doit être un int")

        Utilisateur_DAO().supprimer_utilisateur(
            self.utilisateur.id_utilisateur
        )  # carré, juste attention à pas oublier les parenthèses de Utilisateur_DAO()

    def modifier_utilisateur(self, utilisateur: Utilisateur, id_utilisateur: int):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant doit être un int")

        Utilisateur_DAO().modifier_utilisateur(
            self.utilisateur
        )  # je pense que cette méthode devra communiquer avec la session, parce qu'on va pas
        # lui faire modifier son mdp, son username par contre il faudra que la date de dernière connexion change au fur et à mesure.

    def obtenir_utilisateur(self, utilisateur: Utilisateur, id_utilisateur: str):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant doit être un int")

        Utilisateur_DAO().get_utilisateur(
            self.utilisateur
        )  # pourquoi pas, après reflexion en fait utilisateur ne fait que gérer les connexions, on en reparle

    def lister_playlists(self, utilisateur: Utilisateur):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")

        Playlist_DAO().get_all_playlists_by_user(self.utilisateur.id)

    def connecter_utilisateur(pseudo: str, mot_de_passe: str):
        """Méthode pour connecter un utilisateur avec un pseudo et un mot de passe.
        Retourne l'utilisateur si réussi, sinon None.
        """

        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être un str")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être un str")

        if utilisateur.pseudo == pseudo and utilisateur.mot_de_passe == mot_de_passe:
            utilisateur.est_connecte = True
            print(f"Connexion réussie pour l'utilisateur : {id_utilisateur}")
            return utilisateur
        print("Échec de la connexion : identifiant ou mot de passe incorrect.")
        return None  ##Non, il faut appeler la DAO puis vérifier que les mdp hachés sont égaux

    def deconnecter_utilisateur(pseudo: str, mot_de_passe: str):
        """Méthode pour déconnecter un utilisateur avec un id et un mot de passe.
        Retourne True si la déconnexion est réussie, sinon False.
        """

        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être un str")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être un str")

            if utilisateur.pseudo == pseudo and utilisateur.mot_de_passe == mot_de_passe:

            if (
                utilisateur.pseudo == pseudo
                and utilisateur.mot_de_passe == mot_de_passe
            ):
                if utilisateur.est_connecte == False:
                    print(f"L'utilisateur {id_utilisateur} n'est pas connecté.")
                    return False
                else:
                    Utilisateur.est_connecte = True  # je pense que c'est pas bon, il faudra que tu fasses un truc du genre utilisateur.est_connecte = False pour transformer l'état de connexion de l'utilisateur en déconnecté.
                    print(f"Déconnexion réussie pour l'utilisateur : {id_utilisateur}")
                    return True
        # j'ai mis en commentaire cette partie parce qu'elle n'est jamais éxécutée. si elle sert à qqch faut modifier le code
        #                else:
        #                    print(f"L'utilisateur {id_utilisateur} n'est pas connecté.")
        #                    return False
        print("Échec de la déconnexion : ID ou mot de passe incorrect.")
        return False  # ça sera utile mais j'ai aucune idée de comment faire le code, je suis pas sûr que ça soit bon ici
