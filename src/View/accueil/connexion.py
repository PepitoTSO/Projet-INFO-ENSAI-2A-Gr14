class identification_utilisateur():
    '''
    Permet connexion et inscription
    '''
    def connexion(message):
        print(message)
        return "Utilisateur connecté"


class connexion_Vue:
     def display(self):
        utilisateur = inqugirer.text(message="Nom d'utilisateur : ").execute()
        password = inquirer.secret(message="Mot de passe : ").execute()
        return username, password


class inscription_Vue:
    def display(self):
        utilisateur = inquirer.text(message="Nom d'utilisateur : ").execute()
        password = inquirer.secret(message="Mot de passe : ").execute()
        return username, password
