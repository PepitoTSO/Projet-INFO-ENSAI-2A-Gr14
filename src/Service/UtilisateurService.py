from src.Object.utilisateur import Utilisateur
from src.DAO.utilisateur_DAO import Utilisateur_DAO


class UtilisateurService:
    def __init__(self, utilisateur: Utilisateur):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")

        self.utilisateur = utilisateur

    def creer_compte(self, id, mdp):
        mdp_hache = Utilisateur.hacher_mot_de_passe(mdp)

        print(f"Compte créé pour l'utilisateur {id}.")
        return Utilisateur(id=id, mdp_hache=mdp_hache)

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

    def creer_utilisateur(self, id: str, mdp: str):

        if not isinstance(id, str):
            raise TypeError("L'identifiant doit être un str")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être un str")

        nouvel_utilisateur = Utilisateur(id, mdp)
        Utilisateur.utilisateurs.append(nouvel_utilisateur)
        return nouvel_utilisateur

    def supprimer_utilisateur(self, id: str):

        if not isinstance(id, str):
            raise TypeError("L'identifiant doit être un str")

        Utilisateur_DAO.supprimer_utilisateur(self.utilisateur.id)

    def modifier_utilisateur(self, utilisateur: Utilisateur, id: str):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id, str):
            raise TypeError("L'identifiant' doit être un str")

        Utilisateur_DAO.modifier_utilisateur(self.utilisateur)

    def obtenir_utilisateur(self, utlisateur: Utilisateur, id: str):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id, str):
            raise TypeError("L'identifiant' doit être un str")

        Utilisateur_DAO.get_utilisateur(self.utilisateur)
