
from fonctions import *
import csv 

      
#lire le fichier csv
filename = open('Donnees_Projet_Python_DataC5.csv')
f = csv.reader(filename)

lignecompte = 0
dico = {}
donnee_invalides = {}
donnees_valides = {}
donne = {}

#mettre les donnees dans un dictionnaire
for ligne in  f :
    if lignecompte >= 1 :
        dico[ligne[1]] ={'code':ligne[0], 'numero':ligne[1], 'nom':ligne[2], 'prenom':ligne[3], 'date_de_naissance':transformation_date(transformation_des_separateurs_en_tiret(espace_inutile(ligne[4]))), 'classe':changer_format_classe(ligne[5]), 'note': format_notes(ligne[6])       } 
    lignecompte += 1


donnees_valides,donnees_invalides = separation_des_donnees_en_valide_et_invalide(dico)


 

choice = afficher_le_menu()

while choice != '9':
    if choice == '1' :
        print(afficher_information(donnees_valides))
        choice = afficher_le_menu()


    elif choice == '2' :
        print(afficher_information(donnees_invalides))
        choice = afficher_le_menu()
        
        
        
    elif choice == '3' :
        numero_de_recherche = input("Veuillez entrer le numero de l'eleve pour faire la recherche: ")
        if is_valid_numero(numero_de_recherche) == True :
            print("Le numero saisie est correct ")
        else :
            numero_est_correct = False
            while numero_est_correct == False:
                numero = input("Veuillez entrer un bon numero de recherche: ")
                if is_valid_numero(numero) == True :
                    valeurcorrect = True
        eleve_trouver = recherche_information(numero_de_recherche, donnees_valides)
        if eleve_trouver == False :
            eleve_trouver = recherche_information(numero_de_recherche, donnees_invalides)
            if eleve_trouver == False:
                print("Aucun élève trouvé pour le numéro de recherche donné.")
        choice = afficher_le_menu()



    elif choice == '4' :
        print(afficher_information(dico[0:5]))
        print(afficher_information(donnees_valides[0:5]))
        print(afficher_information(donnees_invalides[0:5]))
        choice = afficher_le_menu()
        
        
    elif choice == '5' :
        print(ajouter_information(dico))
        choix = input("voulez vous ajouter un autre eleves? (o/n) ")
        while choix == 'o' :
            print(ajouter_information(dico))
            choix = input("voulez vous ajouter un autre eleves? (o/n) ")
        choice = afficher_le_menu()
        
    
    elif choice == '6' :
        print
    
    
    elif choice == '7' :
        print
        
    
    elif choice == '9' :
        print
        

    else  :
        print("Choisis quelque chose")
        choice = afficher_le_menu()









