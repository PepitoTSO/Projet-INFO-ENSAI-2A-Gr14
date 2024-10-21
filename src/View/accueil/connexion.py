class identification_utilisateur():
    '''
    Permet connexion et inscription
    '''
    def connexion(message):
        print(message)
        return "Utilisateur connecté"
    
class InscriptionVue:
    
    def __init__(self, message):
        self.message = message
        self.show_message()

    def show_message(self):
        print(self.message)
        return "Vue inscription utilisateur"
    