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
        """
        Adds a new 'son' to the database.
        """
        created = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    insert_query = """
                        INSERT INTO son (nom, id_playlist, ordre_son_in_plist, tags, path_stockage)
                        VALUES (%s, %s, %s, %s, %s)
                        RETURNING id_son;
                    """
                    cursor.execute(
                        insert_query,
                        (
                            son.nom_son,
                            son.id_playlist,
                            son.ordre_son_playlist,
                            son.tags,
                            son.path_stockage,
                        ),
                    )
                    # Fetch the generated id_son
                    res = cursor.fetchone()
                    if res:
                        son.id_son = result[0]
                        created = True
            return created
        except Exception as e:
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


# a voir


from typing import List, Optional
from utils.singleton import Singleton
from db_connection import DBConnection
from son import Son


class Son_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Son operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def ajouter_son(self, son: Son) -> bool:
        """
        Adds a new 'son' to the database.
        """
        created = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    insert_query = """
                        INSERT INTO bdd.son (nom, id_playlist, ordre_son_in_plist, tags, path_stockage)
                        VALUES (%(nom)s, %(id_playlist)s, %(ordre_son_in_plist)s, %(tags)s, %(path_stockage)s)
                        RETURNING id_son;
                    """
                    cursor.execute(
                        insert_query,
                        {
                            "nom": son.nom,
                            "id_playlist": son.id_playlist,
                            "ordre_son_in_plist": son.ordre_son_in_plist,
                            "tags": son.tags,
                            "path_stockage": son.path_stockage,
                        },
                    )
                    # Fetch the generated id_son
                    res = cursor.fetchone()
                    if res:
                        son.id_son = res[0]
                        created = True
            return created
        except Exception as e:
            print(f"Error adding son: {e}")
            return False

    def get_son(self, id_son: int) -> Optional[Son]:
        """
        Retrieves a 'son' by its id_son.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    select_son_query = """
                        SELECT nom, id_playlist, ordre_son_in_plist, tags, path_stockage
                        FROM bdd.son WHERE id_son = %s
                    """
                    cursor.execute(select_son_query, (id_son,))
                    row = cursor.fetchone()
                    if row:
                        son = Son(
                            id_son=id_son,
                            nom=row[0],
                            id_playlist=row[1],
                            ordre_son_in_plist=row[2],
                            tags=row[3],
                            path_stockage=row[4],
                        )
                        return son
                    else:
                        return None
        except Exception as e:
            print(f"Error retrieving son: {e}")
            return None

    def get_all_sons(self) -> List[Son]:
        """
        Retrieves all 'sons' from the database.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    select_all_sons_query = """
                        SELECT id_son, nom, id_playlist, ordre_son_in_plist, tags, path_stockage
                        FROM bdd.son
                    """
                    cursor.execute(select_all_sons_query)
                    rows = cursor.fetchall()
                    sons = []
                    for row in rows:
                        son = Son(
                            id_son=row[0],
                            nom=row[1],
                            id_playlist=row[2],
                            ordre_son_in_plist=row[3],
                            tags=row[4],
                            path_stockage=row[5],
                        )
                        sons.append(son)
            return sons
        except Exception as e:
            print(f"Error retrieving all sons: {e}")
            return []

    def supprimer_son(self, id_son: int) -> bool:
        """
        Deletes a 'son' by its id_son.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Delete tags associated with the son, if applicable
                    delete_tags_query = "DELETE FROM bdd.son_tags WHERE id_son = %s"
                    cursor.execute(delete_tags_query, (id_son,))
                    # Delete the son itself
                    delete_son_query = "DELETE FROM bdd.son WHERE id_son = %s"
                    cursor.execute(delete_son_query, (id_son,))
            return True
        except Exception as e:
            print(f"Error deleting son: {e}")
            return False
