from typing import List, Dict, Any
from utils.singleton import Singleton
from db_connection import DBConnection
from utilisateur import Utilisateur


class Utilisateur_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Utilisateur operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def ajouter_utilisateur(self, utilisateur: Utilisateur) -> bool:
        """
        Adds a new utilisateur to the database.
        """
        created = False

        # Check if the utilisateur already exists
        existing_utilisateur = self.get_utilisateur(utilisateur.id)
        if existing_utilisateur is not None:
            print(f"Utilisateur avec id {utilisateur.id} existe déjà.")
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                        INSERT INTO utilisateur (id, mdp, dd, ddc)
                        VALUES (%(id)s, %(mdp)s, %(dd)s, %(ddc)s)
                        """,
                    {
                        "id": utilisateur.id,
                        "mdp": utilisateur.mdp,
                        "dd": utilisateur.dd,
                        "ddc": utilisateur.ddc,
                    },
                )
        created = True

        return created

    def get_utilisateur(self, id: int) -> Utilisateur:
        """
        Retrieves a utilisateur by their id.
        """
        try:
            cursor = self.db_connection.cursor()
            select_user_query = """
                SELECT id, mdp, dd, ddc FROM utilisateurs WHERE id = %s
            """
            # On pourrait écrire select_user_query = f"SELECT id, mdp, dd, ddc FROM utilisateurs WHERE id = {id}"
            # mais on se prémunit des injections SQL
            cursor.execute(select_user_query, (id,))
            row = cursor.fetchone()
            if row:
                utilisateur = Utilisateur(
                    id=row["id"], mdp=row["mdp"], dd=row["dd"], ddc=row["ddc"]
                )
                cursor.close()
                return utilisateur
            else:
                cursor.close()
                return None
        except Exception as e:
            print(f"Error retrieving utilisateur: {e}")
            return None

    def get_all_utilisateurs(self) -> List[Utilisateur]:
        """
        Retrieves all utilisateurs from the database.
        """
        try:
            cursor = self.db_connection.cursor()
            select_all_users_query = """
                SELECT id, mdp, dd, ddc FROM utilisateurs
            """
            cursor.execute(select_all_users_query)
            utilisateurs = []
            for row in cursor.fetchall():
                utilisateur = Utilisateur(
                    id=row["id"], mdp=row["mdp"], dd=row["dd"], ddc=row["ddc"]
                )
                utilisateurs.append(utilisateur)
            cursor.close()
            return utilisateurs
        except Exception as e:
            print(f"Error retrieving all utilisateurs: {e}")
            return []

    def modifier_utilisateur(self, data: Dict[str, Any]) -> bool:
        """
        Modifies a utilisateur's information.
        """
        try:
            cursor = self.db_connection.cursor()
            id = data.get("id")
            if not id:
                print("Utilisateur ID (id) is required for modification.")
                return False

            fields_to_update = data.copy()
            fields_to_update.pop("id", None)
            if not fields_to_update:
                print("No fields to update.")
                return False

            # Cela crée une chaîne de caractères comme 'mdp = %s, dd = %s, ddc = %s',
            # en fonction des champs qui sont mis à jour.
            update_fields = ", ".join(
                [f"{key} = %s" for key in fields_to_update.keys()]
            )
            update_values = list(fields_to_update.values())
            update_values.append(id)
            update_query = f"UPDATE utilisateurs SET {update_fields} WHERE id = %s"

            cursor.execute(update_query, update_values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error modifying utilisateur: {e}")
            return False

    def supprimer_utilisateur(self, id: int) -> bool:
        """
        Deletes a user by their id.
        """
        try:
            cursor = self.db_connection.cursor()
            delete_user_query = "DELETE FROM utilisateurs WHERE id = %s"
            cursor.execute(delete_user_query, (id,))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error deleting utilisateur: {e}")
            return False
