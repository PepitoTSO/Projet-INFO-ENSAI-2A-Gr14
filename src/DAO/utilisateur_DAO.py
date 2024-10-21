from typing import List, Dict, Any
from utils.singleton import Singleton  # Importing the Singleton metaclass
from db_connection import DBConnection  # Importing your DBConnection class
from utilisateur import Utilisateur  # Importing the Utilisateur class
from datetime import date


class Utilisateur_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Utilisateur operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def __init__(self):
        self.db_connection = DBConnection().connection

    def ajouter_utilisateur(self, uid: int, mdp: str, dd: date, ddc: date) -> bool:
        """
        Adds a new utilisateur to the database.
        """
        try:
            cursor = self.db_connection.cursor()
            insert_user_query = """
                INSERT INTO utilisateurs (uid, mdp, dd, ddc)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_user_query, (uid, mdp, dd, ddc))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error adding utilisateur: {e}")
            return False

    def get_utilisateur(self, uid: int) -> Utilisateur:
        """
        Retrieves a utilisateur by their uid.
        """
        try:
            cursor = self.db_connection.cursor()
            select_user_query = """
                SELECT uid, mdp, dd, ddc FROM utilisateurs WHERE uid = %s
            """
            cursor.execute(select_user_query, (uid,))
            row = cursor.fetchone()
            if row:
                utilisateur = Utilisateur(
                    uid=row["uid"], mdp=row["mdp"], dd=row["dd"], ddc=row["ddc"]
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
                SELECT uid, mdp, dd, ddc FROM utilisateurs
            """
            cursor.execute(select_all_users_query)
            utilisateurs = []
            for row in cursor.fetchall():
                utilisateur = Utilisateur(
                    uid=row["uid"], mdp=row["mdp"], dd=row["dd"], ddc=row["ddc"]
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
            uid = data.get("uid")
            if not uid:
                print("Utilisateur ID (uid) is required for modification.")
                return False

            fields_to_update = data.copy()
            fields_to_update.pop("uid", None)
            if not fields_to_update:
                print("No fields to update.")
                return False

            update_fields = ", ".join(
                [f"{key} = %s" for key in fields_to_update.keys()]
            )
            update_values = list(fields_to_update.values())
            update_values.append(uid)
            update_query = f"UPDATE utilisateurs SET {update_fields} WHERE uid = %s"

            cursor.execute(update_query, update_values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error modifying utilisateur: {e}")
            return False

    def supprimer_utilisateur(self, uid: int) -> bool:
        """
        Deletes a utilisateur by their uid.
        """
        try:
            cursor = self.db_connection.cursor()
            delete_user_query = "DELETE FROM utilisateurs WHERE uid = %s"
            cursor.execute(delete_user_query, (uid,))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error deleting utilisateur: {e}")
            return False
