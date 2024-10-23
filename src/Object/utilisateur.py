class Utilisateur:
    def __init__(self, id: int):
        if not isinstance(id, int):
            raise TypeError("L'id de l'utilisateur n'est pas de la classe int.")
        self.id = id

    def creer_compte(self, id, mdp):
        mdp_hache = Utilisateur.hacher_mot_de_passe(mdp)  ######
        ### c'est quoi Utilisateur.hacher_mot_de_passe, il manque une fonction
        ######

        print(f"Compte créé pour l'utilisateur {id_utilisateur}.")
        return Utilisateur(pseudo=pseudo, mdp=mdp_hache)

        ####On crée un nouvel utilisateur? Creer un compte est à refaire

    ##My bad on a pas besoin de creer une playlist ici, ça se fait dans la classe playlist
    def creer_playlist(self, nom_playlist, son):
        if nom_playlist in self.playlist:
            print(f"La playlist '{nom_playlist}' existe déjà.")
        else:
            self.playlist[nom_playlist] = [son]
            print(f"Playlist '{nom_playlist}' créée avec succès")
        return self.playlist[nom_playlist]

    # Pareil pour supprimer playlist
    def supprimer_playlist(self, nom_playlist):
        if nom_playlist in self.playlists:
            del self.playlists[nom_playlist]
            print(f"Playlist '{nom_playlist}' supprimée.")
            return True
        else:
            print(f"La playlist '{nom_playlist}' n'existe pas.")
            return False

    # Pareil pour copier une playlist
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
