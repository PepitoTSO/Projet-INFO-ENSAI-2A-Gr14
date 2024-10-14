from pathlib import Path

class gestion_dl():

    def __init__(self):
        self.dossier = Path("../../data/son")

    def creation_dossier_dl(self):

        self.dossier.mkdir(parents=True, exist_ok=True)

        print(f"Le répertoire '{self.dossier}' a été créé avec succès.")

    def trop_gros(self):
        pass
    
