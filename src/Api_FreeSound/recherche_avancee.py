'''
On veut recuperer la liste des tags possibles de freesound puis calculer une distance à l'objet de la recherche
et prendre les 5 tags les plus proches.
'''
'''On veut prédire uniquement x tags en sortie donc on va entrainer un modèle pour retourner ces tags
la data sera généré par un prompt sur chatgpt : donne moi des phrases pour entrainer... + on ne veut pas oublier le côté dnd donc a préciser dans le prompt
Sinon il existe des moèdles plus généraux mais d'une taille de 1,5go'''