
## init ##

tab_personnes = []  # nom, prénom, sexe, date de naissance
positionnement_personnes = []  # tuple d'entiers des positions de 2 personnes


def ajout_personne(nom, prénom, sexe, date_de_naissance):
    tab_personnes.append([nom, prénom, sexe, date_de_naissance])
    positionnement_personnes.append()


## debug ##

tab_personnes.append(["Déhu", "Alexis", "Homme", "21/12/2004"])
tab_personnes.append(["Jean", "Jean", "Homme", "06/06/1944"])

positionnement_personnes.append((0, 1))