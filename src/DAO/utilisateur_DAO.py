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
                        "SELECT pseudo, mdp_hache FROM bdd.utilisateurs WHERE pseudo = %s",
                        (pseudo_utilisateur,),
                    )
                    row = cursor.fetchone()
                    if row is not None:
                        return Utilisateur(pseudo=row[0], mdp_hache=row[1])
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
                        "SELECT mdp_hache FROM bdd.utilisateurs WHERE pseudo = %s",
                        (utilisateur.pseudo,),
                    )
                    row = cursor.fetchone()
                    if row is not None:
                        if row[0] == utilisateur.mdp_hache:
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

        try:
            # Vérifie si l'ancien utilisateur existe toujours
            existing_utilisateur = self.get_utilisateur(ancien_utilisateur)
            if existing_utilisateur is None:
                print(
                    f"Utilisateur avec le pseudo {ancien_utilisateur.pseudo} n'existe pas."
                )
                return False

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


#     def ajouter_utilisateur(self, utilisateur: Utilisateur) -> bool:
#         """
#         Adds a new utilisateur to the database.
#         """
#         created = False

#         # Check if the utilisateur already exists
#         existing_utilisateur = self.get_utilisateur(utilisateur.id)
#         if existing_utilisateur is not None:
#             print(f"Utilisateur avec id {utilisateur.id} existe déjà.")
#             return created

#         try:
#             with DBConnection().connection as connection:
#                 with connection.cursor() as cursor:
#                     cursor.execute(
#                         """
#                             INSERT INTO bdd.utilisateur (id, mdp, dd, ddc)
#                             VALUES (%(id)s, %(mdp)s, %(dd)s, %(ddc)s)
#                             """,
#                         {
#                             "id": utilisateur.id,
#                             "mdp": utilisateur.mdp,
# #                            "dd": utilisateur.dd,
# #                            "ddc": utilisateur.ddc,
#                         },
#                     )# si on ajoute un utilisateur, c'est à la création de son compte donc
#                     # dd et ddc n'existe pas (encore) il faut que tu prennes la date actuelle pour les deux (lien avec session?)
#             created = True

#         return created

#     def get_utilisateur(self, id: int) -> Utilisateur:
#         """
#         Retrieves a utilisateur by their id.
#         """
#         try:
#             with DBConnection().connection as connection:
#                 with connection.cursor() as cursor:
#                     select_user_query = """
#                         SELECT id, mdp, dd, ddc FROM utilisateur WHERE id = %s
#                     """
#                     cursor.execute(select_user_query, (id,))
#                     result = cursor.fetchone()
#                     if result:
#                         return Utilisateur(
#                     id=row["id"], mdp=row["mdp"], dd=row["dd"], ddc=row["ddc"]
#                         ) # t'es sur que ca marche avec le numero des index, j'ai toujours vu avec le nom des colonnes
#                     else:
#                         return None
#         except Exception as e:
#             print(f"Error retrieving utilisateur: {e}")
#             return None

#     def get_all_utilisateurs(self) -> List[Utilisateur]:
#         """
#         Retrieves all utilisateurs from the database.
#         """
#         try:
#             cursor = self.db_connection.cursor()
#             select_all_users_query = """
#                 SELECT id, mdp, dd, ddc FROM utilisateurs
#             """
#             cursor.execute(select_all_users_query)
#             utilisateurs = []
#             for row in cursor.fetchall():
#                 utilisateur = Utilisateur(
#                     id=row["id"], mdp=row["mdp"], dd=row["dd"], ddc=row["ddc"]
#                 )
#                 utilisateurs.append(utilisateur)
#             cursor.close()
#             return utilisateurs
#         except Exception as e:
#             print(f"Error retrieving all utilisateurs: {e}")
#             return []

#     def modifier_utilisateur(self, data: Dict[str, Any]) -> bool:
#         """
#         Modifies a utilisateur's information.
#         """
#         try:
#             cursor = self.db_connection.cursor()
#             id = data.get("id")
#             if not id:
#                 print("Utilisateur ID (id) is required for modification.")
#                 return False

#             fields_to_update = data.copy()
#             fields_to_update.pop("id", None)
#             if not fields_to_update:
#                 print("No fields to update.")
#                 return False

#             # Cela crée une chaîne de caractères comme 'mdp = %s, dd = %s, ddc = %s',
#             # en fonction des champs qui sont mis à jour.
#             update_fields = ", ".join(
#                 [f"{key} = %s" for key in fields_to_update.keys()]
#             )
#             update_values = list(fields_to_update.values())
#             update_values.append(id)
#             update_query = f"UPDATE utilisateurs SET {update_fields} WHERE id = %s"

#             cursor.execute(update_query, update_values)
#             self.db_connection.commit()
#             cursor.close()
#             return True
#         except Exception as e:
#             self.db_connection.rollback()
#             print(f"Error modifying utilisateur: {e}")
#             return False

#     def supprimer_utilisateur(self, id: int) -> bool:
#         """
#         Deletes a user by their id.
#         """
#         try:
#             cursor = self.db_connection.cursor()
#             delete_user_query = "DELETE FROM utilisateurs WHERE id = %s"
#             cursor.execute(delete_user_query, (id,))
#             self.db_connection.commit()
#             cursor.close()
#             return True
#         except Exception as e:
#             self.db_connection.rollback()
#             print(f"Error deleting utilisateur: {e}")
#             return False
