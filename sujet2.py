
## init ##

personnes_famille = []  # nom, prénom, sexe, date de naissance
liens_parentés = []     # tuple numéro enfant & parent


# q1
def ajout_personne(nom, prénom, sexe, date_de_naissance):
    informations = [nom, prénom, sexe, date_de_naissance]
    personnes_famille.append(informations)


# q2
def affichage_tableau(tableau: list()):
    for personne in tableau:
        print(personne, "\n")


# q3
def numéro_personne(nom, prénom):
    cpt = 0
    for personne in personnes_famille:
        cpt += 1
        if personne[0] == nom and personne[1] == prénom:
            return(cpt - 1)


# q4
def construction_lien_parenté(num_parent, num_enfant):
    liens_parentés.append(num_parent, num_enfant)


# q5, non testée
temp_tab_ascendants = []
def découvrir_ascendants(num_personne):
    for info in liens_parentés:
        if info[0] == num_personne:
            # si numéro de la personne est trouvée en enfant
            num_parent = info[1]
            temp_tab_ascendants.append(num_parent)
            # ajout de son parent dans le tableau temporaire
    for num_parent in temp_tab_ascendants:
        découvrir_ascendants(num_parent)
        # récursivité pour trouver chaques parents de ses parents
    return(temp_tab_ascendants)


# q6, non testée
temp_tab_descendants = []
def découvrir_descendants(num_personne):
    for info in liens_parentés:
        if info[1] == num_personne:
            num_enfant = info[0]
            # ajout du numéro de son enfant au tableau temporaire
            temp_tab_descendants.append(num_enfant)
    for num_enfant in temp_tab_descendants:
        découvrir_descendants(num_enfant)
        # récursivité pour trouver petits-[...] enfants
    return(temp_tab_descendants)


# q7
def découvrir_fraterie(num_personne):
    tab_parents = []
    tab_info_fraterie = []
    for info in liens_parentés:
        if info[1] == num_personne:
            # récupération des numéros des parents de la personne
            tab_parents.append(info[0])
    for info in liens_parentés:
        for parent in tab_parents:
            if info[0] == parent and info[1] != num_personne:
                # pour tout enfant avec même numéro de parent n'ayant pas lui-même
                num_fraterie = info[1]
                info_fraterie = personnes_famille[num_fraterie]
                tab_info_fraterie.append(info_fraterie)
                # récupération de ses informations pour l'ajouter au tableau
    return(tab_info_fraterie)



## debug ##

personnes_famille.append(["Déhu", "Laurent", "Homme", "???"])        # parent
personnes_famille.append(["Déhu", "Alexis", "Homme", "21/12/2004"])  # enfant
liens_parentés.append((1, None))
liens_parentés.append((None, 0))

# ajout_personne("Didier", "Didier", "Homme", "hier")
# print(affichage_tableau(personnes_famille))
# print(numéro_personne("Déhu", "Laurent"))

#print("\nTableau des personnes : ", personnes_famille, "\n\nTableau des positionnements : ", liens_parentés)