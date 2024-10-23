from src.Object.utilisateur import Utilisateur
from src.DAO.utilisateur_DAO import Utilisateur_DAO
from src.DAO.playlist_DAO import Playlist_DAO


class UtilisateurService:
    def __init__(self, utilisateur: Utilisateur):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")

        self.utilisateur = utilisateur

    def creer_compte(self, id_utilisateur, pseudo, mdp):
        mdp_hache = Utilisateur.hacher_mot_de_passe(mdp)

        print(f"Compte créé pour l'utilisateur {id}.")
        return Utilisateur(pseudo=pseudo, mdp_hache=mdp_hache)

    def creer_playlist(self, nom_playlist, son):
        if nom_playlist in self.playlists:
            print(f"La playlist '{nom_playlist}' existe déjà.")
        else:
            self.playlists[nom_playlist] = [son]
            print(f"Playlist '{nom_playlist}' créée avec succès")
        return self.playlists[nom_playlist]

    def supprimer_playlist(self, nom_playlist):
        if nom_playlist in self.playlists:
            del self.playlists[nom_playlist]
            print(f"Playlist '{nom_playlist}' supprimée.")
            return True
        else:
            print(f"La playlist '{nom_playlist}' n'existe pas.")
            return False

    def copier_playlist(self, nom_playlist_source, nom_playlist_copie):
        if nom_playlist_source in self.playlists:
            if nom_playlist_copie in self.playlists:
                print(f"La playlist '{nom_playlist_copie}' existe déjà.")
                return False
            else:
                self.playlists[nom_playlist_copie] = list(
                    self.playlists[nom_playlist_source]
                )
                print(
                    f"Playlist '{nom_playlist_copie}' créée à partir de '{nom_playlist_source}'."
                )
                return True
        else:
            print(f"La playlist source '{nom_playlist_source}' n'existe pas.")
            return False

    def creer_utilisateur(self, utilisateur: Utilisateur, pseudo: pseudo, mdp: str):

        if not isinstance(pseudo, int):
            raise TypeError("Le pseudo doit être un str")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être un str")

        Utilisateur_DAO.ajouter_utilisateur(utilisateur)
        nouvel_utilisateur = Utilisateur(pseudo, mdp)
        Utilisateur.utilisateurs.append(nouvel_utilisateur)
        return nouvel_utilisateur

    def supprimer_utilisateur(self, id_utilisateur: str):

        if not isinstance(id_utilisateur, str):
            raise TypeError("L'identifiant doit être un str")

        Utilisateur_DAO.supprimer_utilisateur(self.utilisateur.id_utilisateur)

    def modifier_utilisateur(self, utilisateur: Utilisateur, id_utilisateur: str):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_utilisateur, str):
            raise TypeError("L'identifiant doit être un str")

        Utilisateur_DAO.modifier_utilisateur(self.utilisateur)

    def obtenir_utilisateur(self, utlisateur: Utilisateur, id_utilisateur: str):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_utilisateur, str):
            raise TypeError("L'identifiant doit être un str")

        Utilisateur_DAO.get_utilisateur(self.utilisateur)

    def lister_playlists(self, utilisateur: Utilisateur):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")

        Playlist_DAO.get_playlist(self.utilisateur)

    def connecter_utilisateur(id_utilisateur, mot_de_passe):
        """Méthode pour connecter un utilisateur avec un id et un mot de passe.
        Retourne l'utilisateur si réussi, sinon None.
        """
        for utilisateur in Utilisateur.utilisateurs:
            if (
                utilisateur.id_utilisateur == id_utilisateur
                and utilisateur.mot_de_passe == mot_de_passe
            ):
                utilisateur.est_connecte = True
                print(f"Connexion réussie pour l'utilisateur : {id_utilisateur}")
                return utilisateur
        print("Échec de la connexion : identifiant ou mot de passe incorrect.")
        return None

    @staticmethod
    def deconnecter_utilisateur(id_utilisateur, mot_de_passe):
        """Méthode pour déconnecter un utilisateur avec un id et un mot de passe.
        Retourne True si la déconnexion est réussie, sinon False.
        """
        for utilisateur in Utilisateur.utilisateurs:
            if (
                utilisateur.id_utilisateur == id_utilisateur
                and utilisateur.mot_de_passe == mot_de_passe
            ):
                if utilisateur.est_connecte:
                    utilisateur.est_connecte = False
                    print(f"Déconnexion réussie pour l'utilisateur : {id_utilisateur}")
                    return True
                else:
                    print(f"L'utilisateur {id_utilisateur} n'est pas connecté.")
                    return False
            else:
                print("Échec de la déconnexion : ID ou mot de passe incorrect.")
                return False
