
## init ##

tab_personnes = []  # nom, prénom, sexe, date de naissance
positionnement_personnes = []  # tuple d'entiers d'un numéro identifiant & de la position de la personne dans tab_personnes


def ajout_personne(nom, prenom, sexe, date_de_naissance):
    tab_personnes.append([nom, prenom, sexe, date_de_naissance])
    id_personne = 100 + len(tab_personnes) - 1  # identifiant suivant le dernier dans le tableau
    position_personne = len(tab_personnes) - 1  # position dans tab_personnes
    positionnement_personnes.append((id_personne, position_personne))

def affichage_tableau(tableau: list()):
    for ligne in tableau:
        print(ligne, "\n")

def affichage_personne(numero: int()):
    for position in positionnement_personnes:
        if position[0] == numero:
            position_tableau = position[1]
            return(tab_personnes[position_tableau])


## debug ##

tab_personnes.append(["Déhu", "Alexis", "Homme", "21/12/2004"])
tab_personnes.append(["Jean", "Jean", "Homme", "06/06/1944"])
positionnement_personnes.append((100, 0))
positionnement_personnes.append((101, 1))

# ajout_personne("Déhu", "Justine", "Femme", "06/01/2002")
# ajout_personne("Didier", "Didier", "Homme", "hier")
# print(affichage_tableau(tab_personnes))
#print(affichage_personne(100))

print("\nTableau des personnes : ", tab_personnes, "\n\nTableau des positionnements : ", positionnement_personnes)