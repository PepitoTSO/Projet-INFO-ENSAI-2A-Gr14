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
            print(f"Utilisateur avec id {utilisateur.id} exist déjà.")  #manque un e à existe, est-ce qu'on veut vraiment print des trucs?
            return created

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                            INSERT INTO bdd.utilisateur (id, mdp, dd, ddc)
                            VALUES (%(id)s, %(mdp)s, %(dd)s, %(ddc)s)
                            """,
                        {
                            "id": utilisateur.id,
                            "mdp": utilisateur.mdp,
                            "dd": utilisateur.dd,
                            "ddc": utilisateur.ddc,
                        },
                    )# si on ajoute un utilisateur, c'est à la création de son compte donc
                    # dd et ddc n'existe pas (encore) il faut que tu prennes la date actuelle pour les deux (lien avec session?)
            created = True

            return created

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def get_utilisateur(self, id: int) -> Utilisateur:
        """
        Retrieves a utilisateur by their id.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    select_user_query = """
                        SELECT id, mdp, dd, ddc FROM utilisateur WHERE id = %s
                    """
                    cursor.execute(select_user_query, (id,))
                    result = cursor.fetchone()
                    if result:
                        return Utilisateur(
                            id=result[0], mdp=result[1], dd=result[2], ddc=result[3]
                        ) # t'es sur que ca marche avec le numero des index, j'ai toujours vu avec le nom des colonnes
                    else:
                        return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_all_utilisateurs(self) -> List[Utilisateur]:
        """
        Retrieves all utilisateurs from the database.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM utilisateurs                     "
                    )

                    # to store raw results
                    res = cursor.fetchall()

            # Create an empty list to store formatted results
            utilisateurs: List[Utilisateur] = []

            # if the SQL query returned results (ie. res not None)
            if res:
                for row in res:
                    # Assuming your Utilisateur class has a constructor that takes these fields
                    utilisateur = Utilisateur(
                        id=row["id"], mdp=row["mdp"], dd=row["dd"], ddc=row["ddc"]
                    )
                    utilisateurs.append(utilisateur)

            return utilisateurs
        except Exception as e:
            print(f"Error retrieving all utilisateurs: {e}")
            return []

    def modifier_utilisateur(self, utilisateur: Utilisateur) -> bool:
        """
        Modifie les informations d'un utilisateur.
        """
        updated = False

        # Vérifier si l'ID de l'utilisateur est présent
        if not utilisateur.id:
            print("L'ID de l'utilisateur (id) est requis pour la modification.")
            return updated

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE bdd.compte                               "
                        "   SET pseudo = %(pseudo)s,                     "
                        "       mdp_hash = %(mdp_hash)s,                 "
                        "       date_creation = %(date_creation)s,       "
                        "       date_derniere_co = %(date_derniere_co)s  "
                        " WHERE id_utilisateur = %(id_utilisateur)s      ",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp_hash": utilisateur.mdp,
                            "date_creation": utilisateur.date_creation,
                            "date_derniere_co": utilisateur.date_derniere_co,
                            "id_utilisateur": utilisateur.id,
                        },
                    )
                    if cursor.rowcount:
                        updated = True
            return updated
        except Exception as e:
            print(f"Error modifying utilisateur: {e}")
            return False

    def supprimer_utilisateur(self, id: int) -> bool:
        """
        Deletes a utilisateur by their id.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Si on s'en fout des injections SQL
                    # delete_user_query = f"DELETE FROM utilisateur WHERE id = {id}"
                    # cursor.execute(delete_user_query)
                    delete_user_query = "DELETE FROM utilisateur WHERE id = %s"
                    cursor.execute(delete_user_query, (id,))
                    connection.commit()
            return True
        except Exception as e:
            if connection:
                connection.rollback()
            print(f"Error deleting utilisateur: {e}")
            return False


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    utilisateurs = Utilisateur_DAO().get_all_utilisateurs()
    print(utilisateurs)
