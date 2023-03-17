
## init ##

personnes_famille = []  # nom, prénom, sexe, date de naissance
liens_parentés = []     # tuple numéro enfant & parent


def ajout_personne(nom, prénom, sexe, date_de_naissance):
    informations = [nom, prénom, sexe, date_de_naissance]
    personnes_famille.append(informations)


def affichage_tableau(tableau: list()):
    for personne in tableau:
        print(personne, "\n")


def numéro_personne(nom, prénom):
    cpt = 0
    for personne in personnes_famille:
        cpt += 1
        if personne[0] == nom and personne[1] == prénom:
            return(cpt - 1)

def construction_famille(parent, enfant):
    liens_parentés.append(parent, enfant)






## debug ##

personnes_famille.append(["Déhu", "Laurent", "Homme", "???"])        # parent
personnes_famille.append(["Déhu", "Alexis", "Homme", "21/12/2004"])  # enfant
liens_parentés.append((1, None))
liens_parentés.append((None, 0))

# ajout_personne("Didier", "Didier", "Homme", "hier")
# print(affichage_tableau(personnes_famille))
# print(numéro_personne("Déhu", "Laurent"))

#print("\nTableau des personnes : ", personnes_famille, "\n\nTableau des positionnements : ", liens_parentés)