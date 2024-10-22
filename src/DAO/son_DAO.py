from typing import List
from utils.singleton import Singleton
from db_connection import DBConnection
from son import Son


class Son_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Son operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def ajouter_son(self, son: Son) -> bool:
        try:
            with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO son (id_attack_type, attack_name,        "
                    " power, accuracy, element, attack_description)             "
                    "VALUES                                                     "
                    "(%(id_attack_type)s, %(name)s, %(power)s, %(accuracy)s,    "
                    " %(element)s, %(description)s)                             "
                    "RETURNING id_attack;",
                    {
                        "id_attack_type": id_attack_type,
                        "name": attack.name,
                        "power": attack.power,
                        "accuracy": attack.accuracy,
                        "element": attack.element,
                        "description": attack.description,
                    },
                )
                res = cursor.fetchone()
        if res:
            attack.id = res["id_attack"]
            created = True

        return created
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error adding son: {e}")
            return False

    def get_son(self, id_son: int) -> Son:
        try:
            cursor = self.db_connection.cursor()
            select_son_query = """
                SELECT name FROM sons WHERE id_son = %s
            """
            cursor.execute(select_son_query, (id_son,))
            row = cursor.fetchone()
            if row:
                name = row["name"]

                # Now get the tags
                select_tags_query = """
                    SELECT tag FROM son_tags
                    WHERE id_son = %s
                """
                cursor.execute(select_tags_query, (id_son,))
                tags = [tag_row["tag"] for tag_row in cursor.fetchall()]

                son = Son(id_son=id_son, name=name, tags=tags)
                cursor.close()
                return son
            else:
                cursor.close()
                return None
        except Exception as e:
            print(f"Error retrieving son: {e}")
            return None

    def get_all_sons(self) -> List[Son]:
        try:
            cursor = self.db_connection.cursor()
            select_all_sons_query = """
                SELECT id_son, name FROM sons
            """
            cursor.execute(select_all_sons_query)
            sons = []
            for row in cursor.fetchall():
                id_son = row["id_son"]
                name = row["name"]

                # Now get the tags for each son
                select_tags_query = """
                    SELECT tag FROM son_tags
                    WHERE id_son = %s
                """
                cursor.execute(select_tags_query, (id_son,))
                tags = [tag_row["tag"] for tag_row in cursor.fetchall()]

                son = Son(id_son=id_son, name=name, tags=tags)
                sons.append(son)
            cursor.close()
            return sons
        except Exception as e:
            print(f"Error retrieving all sons: {e}")
            return []

    def supprimer_son(self, id_son: int) -> bool:
        try:
            cursor = self.db_connection.cursor()
            # Delete tags associated with the son
            delete_tags_query = "DELETE FROM son_tags WHERE id_son = %s"
            cursor.execute(delete_tags_query, (id_son,))
            # Delete the son itself
            delete_son_query = "DELETE FROM sons WHERE id_son = %s"
            cursor.execute(delete_son_query, (id_son,))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            self.db_connection.rollback()
            print(f"Error deleting son: {e}")
            return False


# Le bloc try s'assure que le processus de suppression est tenté de manière sécurisée.
# Si une erreur se produit à n'importe quel moment, le bloc except la gère de manière
# élégante en annulant la transaction (pour éviter des modifications de données incomplètes
# ou incorrectes) et en enregistrant l'erreur, avant de retourner False pour signaler l'échec.
# Sans cela, une exception non interceptée pourrait entraîner le plantage du programme ou un
# comportement imprévisible.
