'''
j'ai l'habitude de travailler en anglais mais je me suis abstenu
temps prit: environ 2h

j'ai essayé de créer un maximum de variable au lieu d'utiliser
des paramètres bruts afin de mieux comprendre le programme

je suis disponible pour toute question dessus :)
'''


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


#  q7
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


# q8
def affichage_ordre_alphabétique(tableau_numéro_personnes):
    temp_tab_info_p = []
    # j'estime que les numéros sont linéaires & continus (ex: 1->2->3)
    # j'estime que personnes_famille est le tableau des informations
    num_min = tableau_numéro_personnes[0][0]
    num_max = num_min
    for num in tableau_numéro_personnes:
        for i in range(2):
            if num[i] < num_min:
                num_min = num[i]
            if num[i] > num_max:
                num_max = num[i]
        # on récupère premier & dernier numéro
    for i in range(num_min, num_max):
        temp_tab_info_p.append(personnes_famille[i])
    # toutes les informations des personnes sont stockées
    for i in range(num_min, num_max):
        for j in range(num_min+1, num_max):
            p_observée = personnes_famille[i]
            reste = personnes_famille[j]
            if reste[0] < p_observée[0]:
                temp_tab_info_p[i], temp_tab_info_p[j] = \
                    temp_tab_info_p[j], temp_tab_info_p[i]
            if reste[0] == p_observée[0] and reste[1] < p_observée[1]:
                    temp_tab_info_p[i], temp_tab_info_p[j] = \
                        temp_tab_info_p[j], temp_tab_info_p[i]
            # tri alphabétique par noms puis par prénom si nom similaire
    return(temp_tab_info_p)
                    




















    while len(tableau_numéro_personnes) > 0:
        # pour récupérer tous les numéros, sécurité il n'y en aura plus
        for i in range(num_min, num_max):
            for j in range(i+1, num_max):
                # méthode à la "tri sélection" pour voir si personnes
                # suivantes doivent être mises avant alphabétiquement
                p_observée = personnes_famille[i]
                reste = personnes_famille[j]
                if reste[0] < p_observée[0]:

                 


            




## debug ##

personnes_famille.append(["Déhu", "Laurent", "Homme", "???"])        # parent
personnes_famille.append(["Déhu", "Alexis", "Homme", "21/12/2004"])  # enfant
liens_parentés.append((1, None))
liens_parentés.append((None, 0))

# ajout_personne("Didier", "Didier", "Homme", "hier")
# print(affichage_tableau(personnes_famille))
# print(numéro_personne("Déhu", "Laurent"))

#print("\nTableau des personnes : ", personnes_famille, "\n\nTableau des positionnements : ", liens_parentés)