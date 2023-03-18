'''
j'ai l'habitude de travailler en anglais mais je me suis abstenu
temps prit: environ 2h

j'ai essayé de créer un maximum de variable au lieu d'utiliser
des paramètres bruts pour une meilleure lecture & compréhension

exercice effectué sans aucune recherche ou aide extérieure

abréviations : num == numéro(s)
               p == personne(s)

je suis disponible pour toute question :)
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
    for info_p in tableau:
        print(info_p, "\n")


# q3
def numéro_personne(nom, prénom):
    cpt = 0
    for info_p in personnes_famille:
        cpt += 1
        if info_p[0] == nom and info_p[1] == prénom:
            return(cpt - 1)


# q4
def construction_lien_parenté(num_parent, num_enfant):
    liens_parentés.append(num_parent, num_enfant)


# q5, non testée
temp_tab_ascendants = []
def découvrir_ascendants(num_personne):
    for lien in liens_parentés:
        if lien[0] == num_personne:
            # si numéro de la personne est trouvée en enfant
            num_parent = lien[1]
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
            temp_tab_descendants.append(num_enfant)
            # ajout du numéro de son enfant au tableau temporaire
    for num_enfant in temp_tab_descendants:
        découvrir_descendants(num_enfant)
        # récursivité pour ajouter petits-[...] enfants
    return(temp_tab_descendants)


# q7
def découvrir_fraterie(num_personne):
    tab_parents = []
    tab_info_fraterie = []
    for lien in liens_parentés:
        if lien[1] == num_personne:
            tab_parents.append(lien[0])
            # récupération des numéros des parents de la personne
    for lien2 in liens_parentés:
        for parent in tab_parents:
            if lien2[0] == parent and lien2[1] != num_personne:
                # pour tout enfant avec le même numéro de parent
                num_fraterie = lien2[1]
                info_fraterie = personnes_famille[num_fraterie]
                tab_info_fraterie.append(info_fraterie)
                # récupération de ses informations pour l'ajouter au tableau
    return(tab_info_fraterie)


# q8
def affichage_ordre_alphabétique(tableau_numéro_personnes):
    temp_tab_info_p = []
    # j'estime évolution des num linéaire & continu (ex: 1->2->3)
    # j'estime que personnes_famille est le tableau des informations
    num_min = tableau_numéro_personnes[0][0]
    num_max = num_min
    for num in tableau_numéro_personnes:
        for i in range(2):
            if num[i] < num_min:
                num_min = num[i]
            if num[i] > num_max:
                num_max = num[i]
            # récupération premier & dernier numéro
    for i in range(num_min, num_max):
        temp_tab_info_p.append(personnes_famille[i])
    # stockage informations des personnes
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


# q9
def affichage_par_age(tableau_num_p):
    temp_tab_info_p = []
    num_min = tableau_num_p[0][0]
    num_max = num_min
    for num in tableau_num_p:
        for i in range(2):
            if num[i] < num_min:
                num_min = num[i]
            if num[i] > num_max:
                num_max = num[i]
    for i in range(num_min, num_max):
        temp_tab_info_p.append(personnes_famille[i])
    for i in range(num_min, num_max):
        for j in range(num_min+1, num_max):
            p_observée = personnes_famille[i]
            reste = personnes_famille[j]
            if reste[3] < p_observée[3]:
                temp_tab_info_p[i], temp_tab_info_p[j] = \
                    temp_tab_info_p[j], temp_tab_info_p[i]
    return(temp_tab_info_p)


# q10
def main():
    choix = input("\n===== sujet_2 : liens de parentés =====\n\n 1: ajouter une personne\n 2: afficher les informations de toute la famille\n 3: rechercher le numéro d'identifiant d'une personne\n 4: ajouter un lien de parenté\n 5: afficher les ascendants d'une personne\n 6: afficher la descendance d'une personne\n 7: afficher la fraterie d'une personne\n 8: afficher des informations des personnes de la famille par ordre alphabétique\n 9: afficher les informations des personnes de la famille du plus jeune au plus âgé\n 10: quitter\n\nchoix: ")
     


## debug ##

personnes_famille.append(["Jean", "Stéphane", "Homme", "06/06/1944"])        # parent
personnes_famille.append(["Déhu", "Alexis", "Homme", "21/12/2004"])  # enfant
liens_parentés.append((1, None))
liens_parentés.append((None, 0))

print(main())

# ajout_personne("Didier", "Didier", "Homme", "hier")
# print(affichage_tableau(personnes_famille))
# print(numéro_personne("Déhu", "Laurent"))

#print("\nTableau des personnes : ", personnes_famille, "\n\nTableau des positionnements : ", liens_parentés)