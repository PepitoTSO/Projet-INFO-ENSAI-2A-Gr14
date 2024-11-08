from utils.singleton import Singleton
from db_connection import DBConnection
from Object.son import Son
from typing import List
import psycopg2
import psycopg2.extras


class Son_DAO(metaclass=Singleton):
    """
    Data Access Object (DAO) for Son operations.
    Uses the Singleton pattern to ensure a single instance.
    """

    def ajouter_son(self, son: Son) -> bool:
        """
        Adds a new 'son' to the database.
        """
        # Convert tags to a comma-separated string if it is a list
        tags_string = ",".join(son.tags) if isinstance(son.tags, list) else son.tags

        try:
            with DBConnection().connection as connection:
                with connection.cursor(
                    cursor_factory=psycopg2.extras.RealDictCursor
                ) as cursor:
                    # Execute the insert query using %s placeholders
                    cursor.execute(
                        """
                        INSERT INTO bdd.son (nom_son, tags, path_stockage)
                        VALUES (%s, %s, %s)
                        RETURNING id_son;
                        """,
                        (
                            son.nom,
                            tags_string,
                            str(son.path_stockage),
                        ),
                    )
                    # Fetch the generated id_son
                    res = cursor.fetchone()
                    print(res)

                    # Check if the result is valid
                    if res is not None:
                        print(
                            f"Son added with id: {res['id_son']}"
                        )  # Access the result by column name
                        return True

        except Exception as e:
            # Print a detailed error message including the type and the string representation of the error
            print(f"Error adding son: {e.__class__.__name__}: {e}")
            return False

        # Return False if the insertion failed without triggering an exception
        return False

    def get_son_by_id(self, id_son: int) -> Son:
        with DBConnection().connection as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:
                cursor.execute(
                    "SELECT * FROM bdd.son WHERE id_son = %s;",
                    (id_son,),
                )
                res = cursor.fetchone()
        if res:
            son = Son(
                id_son=res["id_son"],
                nom=res["nom_son"],
                tags=[res["tags"]],
                path_stockage=res["path_stockage"],
            )
            return son
        return None

    def get_son_by_name(self, name_son: str) -> Son:
        with DBConnection().connection as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:
                cursor.execute(
                    "SELECT * FROM bdd.son WHERE nom_son = %s;",
                    (name_son,),
                )
                res = cursor.fetchone()
        if res:
            son = Son(
                id_son=res["id_son"],
                nom=res["nom_son"],
                tags=[res["tags"]],
                path_stockage=res["path_stockage"],
            )
            return son
        return None

    def get_all_son(self) -> list[Son]:
        """
        Récupère tous les sons de la base de données.
        """
        try:
            list_son = []
            with DBConnection().connection as connection:
                with connection.cursor(
                    cursor_factory=psycopg2.extras.RealDictCursor
                ) as cursor:
                    cursor.execute("SELECT * FROM bdd.son;")
                    res = cursor.fetchall()
            for son_data in res:

                print(
                    son_data["id_son"],
                    son_data["nom_son"],
                    [son_data["tags"]],
                    son_data["path_stockage"],
                )
                son = Son(
                    id_son=son_data["id_son"],
                    nom=son_data["nom_son"],
                    tags=[son_data["tags"]],
                    path_stockage=son_data["path_stockage"],
                )
                list_son.append(son)
            return list_son
        except Exception as e:
            print(f"Error get_all_son :{e}")
            return None

    def supprimer_son(self, id_son: int) -> bool:
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM bdd.son WHERE id_son = %s",
                        (id_son,),
                    )
            return True
        except Exception as e:
            print(f"Error deleting son: {e}")
            return False

    def get_all_son_ordre_by_id_playlist(self, id_playlist: int) -> List[List]:
        """
        Retrieves all 'sons' from the specified playlist along with their order in the playlist.
        """
        sons = []
        with DBConnection().connection as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:
                cursor.execute(
                    """
                    SELECT s.id_son, s.nom_son, s.tags, s.path_stockage, psj.ordre_son_playlist
                    FROM bdd.son s
                    JOIN bdd.playlist_son_join psj ON s.id_son = psj.id_son
                    WHERE psj.id_playlist = %s
                    """,
                    (id_playlist,),
                )
                res = cursor.fetchall()

        for son_data in res:
            son = Son(
                id_son=son_data["id_son"],
                nom=son_data["nom_son"],
                tags=son_data["tags"],
                path_stockage=son_data["path_stockage"],
            )
            sons.append([son, son_data["ordre_son_playlist"]])
        return sons
