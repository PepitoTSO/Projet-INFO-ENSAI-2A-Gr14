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
    def creer_compte(self, id_utilisateur, mdp):
        mdp_hache = Utilisateur.hacher_mot_de_passe(mdp) #il manque la fonction et ca devrait plutôt être self.utilisateur.hacher_mot_de_passe(mdp)

        print(f"Compte créé pour l'utilisateur {id}.")
        return Utilisateur(pseudo=pseudo, mdp_hache=mdp_hache)

        return Utilisateur(id=id_utilisateur, mdp_hache=mdp_hache) #on return rien par contre il faut daire appel à la DAO pour créer l'utilisateur dans la base de données
################Tout ce qui est entre là
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
########### et là est à supprimer
    
        def creer_utilisateur(self, id_utilisateur: str, mdp: str):
        # Placeholder for the function body
            pass

        if not isinstance(pseudo, int):
            raise TypeError("Le pseudo doit être un str")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être un str")

        Utilisateur_DAO.ajouter_utilisateur(utilisateur)
        nouvel_utilisateur = Utilisateur(pseudo, mdp)
        Utilisateur.utilisateurs.append(nouvel_utilisateur)
        return nouvel_utilisateur
#### Il faut faire appel à la DAO, créer des objets ne sert à rien



    def supprimer_utilisateur(self, id_utilisateur: int):

        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant doit être un int")

        Utilisateur_DAO().supprimer_utilisateur(self.utilisateur.id_utilisateur) #carré, juste attention à pas oublier les parenthèses de Utilisateur_DAO()

    def modifier_utilisateur(self, utilisateur: Utilisateur, id_utilisateur: int):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant doit être un int")

        Utilisateur_DAO().modifier_utilisateur(self.utilisateur) #je pense que cette méthode devra communiquer avec la session, parce qu'on va pas
        # lui faire modifier son mdp, son username par contre il faudra que la date de dernière connexion change au fur et à mesure.

    def obtenir_utilisateur(self, utilisateur: Utilisateur, id_utilisateur: str):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")
        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant doit être un int")

        Utilisateur_DAO().get_utilisateur(self.utilisateur) # pourquoi pas, après reflexion en fait utilisateur ne fait que gérer les connexions, on en reparle

    def lister_playlists(self, utilisateur: Utilisateur):

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur n'est pas de la classe utilisateur.")

        Playlist_DAO().get_all_playlists_by_user(self.utilisateur.id)

    def connecter_utilisateur(pseudo: str, mot_de_passe: str):

        """
        Méthode pour connecter un utilisateur avec un pseudo et un mot de passe.
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
        return None ##Non, il faut appeler la DAO puis vérifier que les mdp hachés sont égaux

    @staticmethod
    def deconnecter_utilisateur(pseudo: str, mot_de_passe: str):
        """Méthode pour déconnecter un utilisateur avec un id et un mot de passe.
        Retourne True si la déconnexion est réussie, sinon False.
        """

        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être un str")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être un str")
        
            if utilisateur.pseudo == pseudo and utilisateur.mot_de_passe == mot_de_passe:
                if utilisateur.est_connecte == False:
                    print(f"L'utilisateur {id_utilisateur} n'est pas connecté.")
                    return False
                else:
                    Utilisateur.est_connecte = True
                    print(f"Déconnexion réussie pour l'utilisateur : {id_utilisateur}")
                    return True
                print(f"L'utilisateur {id_utilisateur} n'est pas connecté.")
                return False
        print("Échec de la déconnexion : ID ou mot de passe incorrect.")
        return False #ça sera utile mais j'ai aucune idée de comment faire le code, je suis pas sûr que ça soit bon ici

    def afficher_details(self):
        """Affiche les détails de l'utilisateur."""
        etat_connexion = "connecté" if self.est_connecte else "déconnecté"
        print(f"ID utilisateur : {self.id_utilisateur}")
        print(f"Nombre de playlists : {len(self.playlists)}")
        print(f"État : {etat_connexion}") #inutile c'est la session qui dit qui est connecté et qui l'est pas
