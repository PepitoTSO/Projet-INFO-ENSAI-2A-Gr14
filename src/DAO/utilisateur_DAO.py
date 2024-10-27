from utils.singleton import Singleton
from DAO.db_connection import DBConnection
from Object.utilisateur import Utilisateur


class Utilisateur_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Utilisateur operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def creer_utilisateur(self, utilisateur: Utilisateur) -> bool:
        """Crée un nouvel utilisateur dans la base de données.

        Retourne True si la création est réussie,
        ou False si l'utilisateur existe déjà ou en cas d'erreur.
        """

        # Vérifie si l'utilisateur existe déjà
        existing_utilisateur = self.get_utilisateur(utilisateur)
        if existing_utilisateur is not None:
            print(f"Utilisateur avec le pseudo {utilisateur.pseudo} existe déjà.")
            return False  # Retourne False si l'utilisateur existe déjà

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO bdd.utilisateurs (pseudo, mdp_hache) VALUES (%s, %s)",
                        (utilisateur.pseudo, utilisateur.mdp_hache),
                    )
                    return True  # Retourne True si l'utilisateur a été créé avec succès
        except Exception as e:
            print(f"Erreur lors de la création de l'utilisateur : {str(e)}")
            return False  # Renvoie False en cas d'erreur

    def get_utilisateur(self, utilisateur: Utilisateur) -> Utilisateur:
        """Récupère un utilisateur par son pseudo.

        Retourne l'objet Utilisateur si trouvé,
        ou None si l'utilisateur n'existe pas.
        """
        pseudo_utilisateur = utilisateur.pseudo
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM bdd.utilisateurs WHERE pseudo = %(pseudo)s",
                        {"pseudo": pseudo_utilisateur},
                    )
                    row = cursor.fetchone()
                    if row is not None:
                        return Utilisateur(pseudo=row['pseudo'], mdp_hache=row['mdp_hache'])
                    return None
        except Exception as e:
            print(f"Erreur lors de la récupération de l'utilisateur : {str(e)}")
            return None

    def se_connecter(self, utilisateur: Utilisateur) -> bool:
        """Vérifie les informations d'identification d'un utilisateur pour la connexion.

        Retourne True si les informations sont valides,
        ou False si l'utilisateur n'existe pas ou si le mot de passe est incorrect.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT mdp_hache FROM bdd.utilisateurs WHERE pseudo = %s""",
                        (utilisateur.pseudo,),
                    )
                    row = cursor.fetchone()
                    if row is not None:
                        if row['mdp_hache'] == utilisateur.mdp_hache:
                            return True
                        else:
                            print("Mot de passe incorrect.")
                            return False

                    print("Utilisateur non trouvé.")
                    return False
        except Exception as e:
            print(f"Erreur lors de la connexion de l'utilisateur : {str(e)}")
            return False

    def modifier_utilisateur(
        self, ancien_utilisateur: Utilisateur, nouvel_utilisateur: Utilisateur
    ) -> bool:
        """Modifie les informations d'un utilisateur dans la base de données.

        Retourne True si la modification est réussie,
        ou False si l'utilisateur n'existe pas ou en cas d'erreur.
        """
        existing_utilisateur = self.get_utilisateur(ancien_utilisateur)
        if existing_utilisateur is None:
            print(f"Utilisateur avec le pseudo {ancien_utilisateur.pseudo} n'existe pas déjà.")
            return False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE bdd.utilisateurs SET pseudo = %s, mdp_hache = %s WHERE pseudo = %s",
                        (
                            nouvel_utilisateur.pseudo,
                            nouvel_utilisateur.mdp_hache,
                            ancien_utilisateur.pseudo,
                        ),
                    )
                    return True  # Retourne True si la modification a réussi
        except Exception as e:
            print(f"Erreur lors de la modification de l'utilisateur : {str(e)}")
            return False
