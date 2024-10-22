


class Utilisateur:
    def __init__(self, id: int, date_debut, date_derniere_co, playlist):
        if not isinstance(utilisateur, int):
            raise TypeError("L'utilisateur n'est pas de la classe int.")

        self.id = id
        self.date_debut = date_debut
        self.date_derniere_co = date_derniere_co
        self.playlist = []

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
