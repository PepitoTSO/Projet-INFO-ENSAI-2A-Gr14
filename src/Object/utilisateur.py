from src.Object.playlist import Playlist


class Utilisateur:
    def __init__(self, id_utilisateur: int, pseudo: str, dd, ddc, playlist: list, utilisateurs:list, est_connecte: False):
        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant n'est pas de la classe int.")
        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo n'est pas de la classe str.")
        if not isinstance(playlist, list):
            raise TypeError("playlist n'est pas une liste.")
            if not isinstance(utilisateurs, list):
            raise TypeError("utilisateurs n'est pas une liste.")
        if not isinstance(est_connecte, bool):
            raise TypeError("est_connecte n'est pas un booleen.")

        self.id_utilisateur = id_utilisateur
        self.pseudo = pseudo
        self.dd = dd
        self.ddc = ddc
        self.playlist = []
        self.utilisateurs = []
        self.est_connecte = False  # Indique si l'utilisateur est connecté ou non


    def creer_compte(self, id_utilisateur, pseudo, mdp):
        mdp_hache = Utilisateur.hacher_mot_de_passe(mdp)

        print(f"Compte créé pour l'utilisateur {id_utilisateur}.")
        return Utilisateur(pseudo=pseudo, mdp=mdp_hache)

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