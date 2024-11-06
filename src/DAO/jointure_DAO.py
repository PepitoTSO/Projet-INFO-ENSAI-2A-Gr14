class Jointure_DAO:
    def get_all_id_son_by_id_playlist(self, id_playlist) -> list[Son]:
        sons = []
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Son WHERE id_playlist = %(id_playlist)s;",
                    {"id_playlist": id_playlist},
                )
                res = cursor.fetchall()

        for son_data in res:
            son = Son(
                id_son=son_data["id_son"],
                nom=son_data["nom"],
                caracteristiques=son_data["tags"],
                path=son_data["path_stockage"],
            )
            sons.append(son)
        return sons
