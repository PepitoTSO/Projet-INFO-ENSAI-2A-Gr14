
'''
template pour la DAO
'''


def nom_fn(self) -> bool:
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "REQUETE SQL %(id_playlist)s",
                        {"id_playlist": id_playlist, "id_son": id_son}
                    )
                connection.commit() # ou fetch_all etc
            return True
        except Exception as e:
            print(f"Error deleting son: {e}")
            return False