from utils.singleton import Singleton
from DAO.db_connection import DBConnection
from Object.son import Son
from typing import List
import psycopg2
import psycopg2.extras
from utils.log_decorator import log


class Son_DAO(metaclass=Singleton):
    """
    DAO de Son.
    """

    @log
    def ajouter_son(self, son: Son) -> bool:
        """
        Ajoute un son à la bdd
        """
        # la liste de str son.tags devient un seul str
        tags_string = ", ".join(son.tags) if isinstance(son.tags, list) else son.tags

        try:
            with DBConnection().connection as connection:
                with connection.cursor(
                    cursor_factory=psycopg2.extras.RealDictCursor
                ) as cursor:
                    cursor.execute(
                        """
                        INSERT INTO bdd.son (id_son, nom_son, tags, path_stockage)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id_son;
                        """,
                        (
                            son.id_son,
                            son.nom,
                            tags_string,
                            str(son.path_stockage),
                        ),
                    )
                    res = cursor.fetchone()

                    if res is not None:
                        print(f"Son added with id: {res['id_son']}")
                        return res["id_son"]

        except Exception as e:
            print(f"Erreur ajout son: {e.__class__.__name__}: {e}")
            return False

        return False

    def get_son_by_id(self, id_son: int) -> Son:
        """
        Recupere un son par son id.
        """
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
                tags=(
                    [tag.strip() for tag in res["tags"].split(",")]
                    if isinstance(res["tags"], str)
                    else res["tags"]
                ),
                path_stockage=res["path_stockage"],
            )
            return son
        return None

    def get_son_by_name(self, name_son: str) -> Son:
        """
        Recupere un son par son nom
        """
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
                tags=(
                    [tag.strip() for tag in res["tags"].split(",")]
                    if isinstance(res["tags"], str)
                    else res["tags"]
                ),
                path_stockage=res["path_stockage"],
            )
            return son
        return None

    def get_all_son(self) -> list[Son]:
        """
        Récupère tous les sons de la base de données.
        """
        list_son = []
        try:
            with DBConnection().connection as connection:
                with connection.cursor(
                    cursor_factory=psycopg2.extras.RealDictCursor
                ) as cursor:
                    cursor.execute("SELECT * FROM bdd.son;")
                    res = cursor.fetchall()

            for son_data in res:
                son = Son(
                    id_son=son_data["id_son"],
                    nom=son_data["nom_son"],
                    tags=(
                        [tag.strip() for tag in son_data["tags"].split(",")]
                        if isinstance(son_data["tags"], str)
                        else son_data["tags"]
                    ),
                    path_stockage=son_data["path_stockage"],
                )
                list_son.append(son)
            return list_son

        except Exception as e:
            print(f"Erreur get_all_son :{e}")
            return None

    def supprimer_son(self, id_son: int) -> bool:
        """
        Supprime un son de la bdd par son id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor(
                    cursor_factory=psycopg2.extras.RealDictCursor
                ) as cursor:
                    cursor.execute(
                        """
                        SELECT id_playlist FROM bdd.playlist_son_join
                        WHERE id_son = %s;
                        """,
                        (id_son,),
                    )
                    playlists = cursor.fetchall()

                    for playlist_data in playlists:
                        id_playlist = playlist_data["id_playlist"]

                        cursor.execute(
                            """
                            DELETE FROM bdd.playlist_son_join
                            WHERE id_playlist = %s AND id_son = %s;
                            """,
                            (id_playlist, id_son),
                        )

                        cursor.execute(
                            """
                            SELECT id_son FROM bdd.playlist_son_join
                            WHERE id_playlist = %s
                            ORDER BY ordre_son_playlist;
                            """,
                            (id_playlist,),
                        )
                        remaining_songs = cursor.fetchall()

                        for new_order, son_data in enumerate(remaining_songs, start=1):
                            cursor.execute(
                                """
                                UPDATE bdd.playlist_son_join
                                SET ordre_son_playlist = %s
                                WHERE id_playlist = %s AND id_son = %s;
                                """,
                                (new_order, id_playlist, son_data["id_son"]),
                            )

                    cursor.execute(
                        """
                        DELETE FROM bdd.son WHERE id_son = %s;
                        """,
                        (id_son,),
                    )

                    if cursor.rowcount == 0:
                        return False

            return True
        except Exception as e:
            print(f"Erreur suppression son: {e}")
            return False

    def get_all_son_ordre_by_id_playlist(self, id_playlist: int) -> List[List]:
        """
        Recupère tous les sons d'une playlist par son id et les instancie comme tel
        """
        sons = []
        try:
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
                    tags=(
                        [tag.strip() for tag in son_data["tags"].split(",")]
                        if isinstance(son_data["tags"], str)
                        else son_data["tags"]
                    ),
                    path_stockage=son_data["path_stockage"],
                )
                sons.append([son, son_data["ordre_son_playlist"]])
            return sons

        except Exception as e:
            print(f"Erreur get_all_son_ordre_by_id_playlist :{e}")
            return []


son = Son_DAO().get_son_by_id(2)
print(son)
