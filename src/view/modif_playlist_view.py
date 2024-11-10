class ModifPlaylistView(AbstractView):
    """
    Vue du menu de la gestion des playlists
    """

 def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Modif\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Changer le nom de la playlist",
                "Ajouter un son",
                "Supprimer un son"
                "Changer l'ordre des sons",
                "Revenir au menu précédent",
                "Se déconnecter",
            ],
        ).execute()