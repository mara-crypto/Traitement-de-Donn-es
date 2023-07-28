import re
import locale
from datetime import datetime


def is_valid_numero(numero):
    regex = r'^[A-Z0-9]{7}$'
    if re.match(regex, numero):
        return True
    else:
        return False


def est_prenom_valide(prenom):
    """
    Vérifie si un prénom est valide.

    Un prénom est valide s'il commence par une lettre majuscule et contient au moins 3 lettres.

    Args:
        prenom (str): Le prénom à valider.

    Returns:
        bool: True si le prénom est valide, False sinon.
    """
    if prenom == "":  # Si le prénom est vide, on le considère comme invalide
        return False
    else:
        if 'A' <= prenom[0] <= 'Z' and len(prenom) >= 3:  # Si la première lettre est une majuscule et que la longueur est d'au moins 3 caractères
            return True  # Le prénom est valide
        else:
            return False  # Le prénom n'est pas valide


def est_nom_valide(nom):
    """
    Vérifie si le nom est valide selon les règles suivantes :
    - Le nom commence par une lettre majuscule
    - Le nom contient au moins 2 lettres
    """
    if nom == "":
        # Si le nom est vide, il n'est pas valide
        return False
    else:
        # Vérifier que la première lettre est une majuscule et que la longueur du nom est supérieure ou égale à 2
        if 'A' <= nom[0] <= 'Z' and len(nom) >= 2:
            return True
        else:
            return False


def espace_inutile(date):
    """
    Cette fonction prend une date en entrée et renvoie la même date sans espaces inutiles.

    Args:
        date (str): une date sous forme de chaîne de caractères

    Returns:
        str: la même date sans espaces inutiles
    """
    if date == "" :
        return date
    else :
    # Supprime tous les espaces inutiles dans la date
    #date = date.replace(" ", "")
        date1 = ""
        if date[0] != " " :
            date1 = date1 + date[0]
        for i in range(1,len(date)) :
            if date[i-1] == " " and date [i] == " " :
                continue
            else :
                date1 = date1 + date[i] 
        return date1



def transformation_des_separateurs_en_tiret(date):
    """
    Cette fonction prend une date en entrée et remplace les séparateurs par des tirets.

    Args:
        date (str): une date sous forme de chaîne de caractères

    Returns:
        str: la même date avec des tirets en tant que séparateurs
    """
    date1 = ""
    # Parcourt chaque caractère de la date et remplace les séparateurs par des tirets
    for i in range(len(date)):
        if date[i] in [',', ';', ':', ' ', '/', '.', '_']:
            date1 += '-'
        else:
            date1 += date[i]
    return date1





def transformation_date(date_string):
    """
    Cette fonction prend une date en entrée et la transforme en format "jj-mm-aaaa".

    Args:
        date_string (str): une date sous forme de chaîne de caractères

    Returns:
        str: la même date au format "jj-mm-aaaa"
    """
    # Configure la localisation en français
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    try:
        # Tente de transformer la date en utilisant le format "%d-%B-%y"
        date_obj = datetime.strptime(date_string, "%d-%B-%y")
    except ValueError:
        try:
            # Si cela échoue, tente de transformer la date en utilisant le format "%d-%m-%y"
            date_obj = datetime.strptime(date_string, "%d-%m-%y")
        except ValueError:
            return date_string
    # Formate la date pour qu'elle soit au format "jj-mm-aaaa"
    formatted_date = datetime.strftime(date_obj, "%d-%m-%Y")
    return formatted_date




def est_bissextile(annee):
    """
    Vérifie si une année est bissextile.

    Args:
        annee (int): L'année à vérifier.

    Returns:
        bool: True si l'année est bissextile, False sinon.
    """
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False





def date_de_naissance_valide(date):
    # Vérification de la présence de la date
    if date == "" or not (date[6:].isdigit())   :
        return False
    else:
        # Transformation de la date en format standard
        #date = transformation_date(date)
        # Vérification du mois et du jour en fonction du mois
        if date[3:5] in ['01', '03', '05', '07', '08', '10', '12']:
            if '01'<= date[:2] <= '31':
                return True
            else:
                return False
        elif date[3:5] in ['04', '06', '09', '11']:
            if '01'<= date[:2] <= '30':
                return True
            else:
                return False
        elif date[3:5] == '02':
            # Vérification de l'année bissextile
            if est_bissextile(int(date[6:])):
                if '01' <= date[:2] <= '29':
                    return True
                else:
                    return False
            else:
                if '01' <= date[:2] <= '28':
                    return True
                else:
                    return False





def changer_format_classe(classe):
    # initialisation de la variable format_classe
    format_classe = ""
    # parcourir chaque caractère de la chaine classe
    for i in range(len(classe)):
        # Si le caractère est compris entre '3' et '6' ou entre 'A' et 'B', l'ajouter au format de classe
        if '3' <= classe[i] <= '6' or 'A' <= classe[i] <= 'B':
            format_classe += classe[i]
    # renvoyer le nouveau format de la classe
    return format_classe






def is_valid_classe(classe):
    if len(classe) != 2:
        return False
    if not classe[0].isdigit():
        return False
    if classe[1] not in ['A', 'B']:
        return False
    if int(classe[0]) < 3 or int(classe[0]) > 6:
        return False
    return True



def format_notes(notes):
    # Vérifier si la chaine de notes est vide
    if notes == '':
        return notes
    else:
         # Initialiser une liste de notes et un dictionnaire de matières
       
        matiere_dic = {}
         # Supprimer les espaces et les guillemets
        notes = notes.replace("Science_Physique","PC")
        notes = notes.replace("Pc","PC")
        notes = notes.replace("pc","PC")

        notes = notes.replace("MATH", "Math")

        notes = notes.replace("ANGLAIS","Anglais")

        notes = notes.replace("FRANCAIS","Francais")
        notes = notes.replace("Français","Francais")

        notes = notes.replace(" ", '')
        notes = notes.replace('"', '')
         # Diviser les notes en fonction des matières
        notes = notes.split('#')
           # Supprimer les éléments vides de la liste des notes
        for i in notes:
            if i == '':
                notes.remove(i)
        # Traiter chaque matière et ses notes
        for i in range(len(notes)):
            # Initialiser une chaine de caractères pour stocker les notes
            note_dic = ""
             # Diviser les informations de la matière en fonction de la note
            for j in notes[i].split('['):
                # Ajouter la matière au dictionnaire et initialiser une liste de notes pour cette matière
                matiere_dic[j] = []
                  # Ajouter chaque note dans la liste de notes pour cette matière
                for k in notes[i].split('[')[1]:
                     # Vérifier si le caractère est un chiffre, une virgule ou un point
                    if k.isnumeric() or k == ',' or k == '.':
                        note_dic += k.replace(',', '.')
                    else:
                          # Ajouter la note à la liste de notes pour cette matière
                        matiere_dic[j].append(note_dic)
                        note_dic = ""
                break
         # Traiter chaque matière et calculer la moyenne
        for matiere, notes in matiere_dic.items():
            if len(notes) > 0:
                if len(notes) == 5:
                    if notes[0] and notes[1] and notes[2] and notes[3]:
                         # Calculer la moyenne des devoirs
                        moyenne_devoir = (float(notes[0]) + float(notes[1]) + float(notes[2]) + float(notes[3])) / 4
                        # Calculer la moyenne de la matière en fonction des coefficients des devoirs et du contrôle continu
                        moyenne_matiere = round((moyenne_devoir + (2 * float(notes[4]))) / 3, 2)
                        moyenne_matiere = str(moyenne_matiere)
                    else:
                        moyenne_matiere = 0.0
                        moyenne_matiere = str(moyenne_matiere)
                     # Ajouter la moyenne de la matière à la liste de notes pour cette matière
                    matiere_dic[matiere].append(moyenne_matiere)
                elif len(notes) == 4:
                    if notes[0] and notes[1] and notes[2]:
                        moyenne_devoir = (float(notes[0]) + float(notes[1]) + float(notes[2])) / 3
                        moyenne_matiere = round((moyenne_devoir + (2 * float(notes[3]))) / 3, 2)
                        moyenne_matiere = str(moyenne_matiere)
                    else:
                        moyenne_matiere = 0.0
                        moyenne_matiere = str(moyenne_matiere)
                    matiere_dic[matiere].append(moyenne_matiere)
                elif len(notes) == 3:
                    if notes[0] and notes[1]:
                        moyenne_devoir = (float(notes[0]) + float(notes[1])) / 2
                        moyenne_matiere = round((moyenne_devoir + (2 * float(notes[2]))) / 3, 2)
                        moyenne_matiere = str(moyenne_matiere)
                    else:
                        moyenne_matiere = 0.0
                        moyenne_matiere = str(moyenne_matiere)
                    matiere_dic[matiere].append(moyenne_matiere)
                elif len(notes) == 2:
                    if notes[0]:
                        moyenne_devoir = float(notes[0])
                        moyenne_matiere = round((moyenne_devoir + (2 * float(notes[1]))) / 3, 2)
                        moyenne_matiere = str(moyenne_matiere)
                    else: 
                        moyenne_matiere = 0.0
                        moyenne_matiere = str(moyenne_matiere)
                        moyenne_matiere = str(moyenne_matiere)

                    matiere_dic[matiere].append
                
       # matiere_dic = matiere_dic.replace("Science_Physique","PC")
        
        
        return matiere_dic





def validiter_notes(matiere_dic) :

    if matiere_dic == "" :
        return False
    else :
        matiere_valide = 0
        for cle, valeur in matiere_dic.items() :
            
            compteur_note_valide = 0

            if len(valeur) == 0 :
                continue

           
            for i in range(len(valeur)) : 
                

                if isinstance(valeur[i], str) and valeur[i].strip() and 0 <= float(valeur[i]) <= 20:
                #if 0 <=float(valeur[i]) <= 20 :
                    compteur_note_valide += 1
                    #
                    
                else :
                    continue
            

            if compteur_note_valide == len(valeur) :
               
                matiere_valide = matiere_valide + 1

        
        if matiere_valide == len(matiere_dic) :
            return True
        else :
            return False






def afficher_le_menu() :
    print(""" 
          
                                                         MENU
                                                         
    1°  Afficher les informations Valide
    2°  Afficher les informations invalide
    3°  Afficher une information par son numéro
    4°  Afficher les cinq premiers
    5°  Ajouter une information en vérifiant la validité des informations données
    6°  Modifier une information invalide ensuite le transférer dans la structure où se trouve les informations valides
    7°  Affichage par pagination: par 5 lignes 
    8°  Affichage par pagination: A vous de choisir par combien de lignes vous voumez paginez
    9°  Quitter Le programme       
          """)
    choice = input("entrer votre choix ")
    return choice
          
         

def afficher_information(dictionnaire) :
    # print("voici les informations:")
    # print(('\n'))
    #print(dictionnaire)
     for cle, element in  dictionnaire.items() :
         
                
         print("|{:<10}|{:<10}|{:<10}|{:<15}|{:<15}|{:<5}|".format(element["code"], element["numero"], element["nom"], element["prenom"], element["date_de_naissance"], element["classe"]))


def recherche_information(numero_de_recherche, dico) :
    

    #modifier=''
    #numero_de_recherche = input("entrer le numero de l'eleve à rechercher: ")
    eleve_trouver = False
    for cle,valeur in dico.items():
        if numero_de_recherche in cle :
            
            print("|{:<10}|{:<10}|{:<15}|{:<25}|{:<15}|{:<5}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
            print("|{:-<10}|{:-<10}|{:-<15}|{:-<25}|{:-<15}|{:-<5}|".format("", "", "", "", "", ""))
            print("|{:<10}|{:<10}|{:<15}|{:<25}|{:<15}|{:<5}|".format(valeur["code"], valeur["numero"], valeur["nom"], valeur["prenom"], valeur["date_de_naissance"], valeur["classe"]))
            eleve_trouver = True
            break
    return  eleve_trouver



def modifier_info_eleves(dico) :


    eleve.update({eleve["Numero"]:input("entrer le numero")})
    eleve.update({eleve["Prénom"]:input("entrer le prénom")})
    eleve.update({eleve["Nom"]:input("entrer le nom")})
    eleve.update({eleve["Date de naissance"]:input("entrer la date de naissance")})
    eleve.update({eleve["Classe"]:input("Entrer la classe ")})
    if teste_num(eleve['Numero'])==True and teste_nom(eleve['Nom'])==True and teste_pnom(eleve['Prénom'])==True and is_valid_date(eleve['Date de naissance'])==True and teste_note(eleve['Note']) == True and teste_classe(eleve['Classe'])==True:
        valid.append(eleve)
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<15}".format("CODE", "Numero", "Prénom", "Nom", "Date de naissance", "Classe"))
        print("|{:-<15}|{:-<15}|{:-<15}|{:-<10}|{:-<15}|{:-<10}|".format("", "", "", "", "", "", ""))
        print("|{:<15}|{:<15}|{:<15}|{:<10}|{:<15}|{:<10}|".format(eleve["CODE"], eleve["Numero"], eleve["Prénom"],                     eleve["Nom"], eleve["Date de naissance"], eleve["Classe"]))
    else:
        print("des infos semblent rester invalide")

    

def ajouter_information(dico) :
    
    print("vous allez ajouter les informations d'un nouveau eleves")
    code = input("code  ")
    
    numero = input("numero: ")
    if is_valid_numero(numero) == False :
        numero_valide = False
        while numero_valide == False :
            numero = input("numero: ")
            if is_valid_numero(numero) == True :
                numero_valide = True
                
    nom = input("nom: ")
    if est_nom_valide(nom) == False :
        nom_correct = False 
        while nom_correct == False :
            nom = input("le nom saissie ne respect pas les regles: ")
            if est_nom_valide(nom) == True :
                nom_correct = True
            else :
                nom_correct = False
                
    prenom =  input("prenom: ")
    if est_prenom_valide(prenom) == False :
        nom_correct == False 
        while nom_correct == False :
            nom = input("le prenom saissie ne respect pas les regles: ")
            if est_prenom_valide(prenom) == True :
                nom_correct = True
            else :
                nom_correct = False
                
    date_de_naissance = input("date de naissance format=jj-mm-aaaa : ")
    if date_de_naissance_valide(date_de_naissance) == False :
        date_valide = False 
        while date_valide == False :
            date_de_naissance = input("date de naissance incorrect format=jj-mm-aaaa : ")
            if  date_de_naissance_valide(date_de_naissance) == True :
                date_valide = True
                
    classe =  input("format=5A, classe: ")
    if is_valid_classe(classe) == False :
        classe_valide = False 
        while classe_valide == False :
            classe = input("classe incorrect format=4B, classe : ")
            if  is_valid_classe(classe) == True :
                classe_valide = True
            
    note = input("""
les matieres sont separe par #
Les notes des matières sont dans des crochets []
Les notes de devoir sont séparées par la note d'examen par deux point :
Les notes de devoir sont séparées entre eux par une barre verticale |
                 """)
    note = format_notes(note)
    if validiter_notes(note) == False:
        print("vous n'avez pas saisie les note en suivant les regles")
        note_valide = False 
        while note_valide == False :
            note = input("""
        les matieres sont separe par #
        Les notes des matières sont dans des crochets []
        Les notes de devoir sont séparées par la note d'examen par deux point :
        Les notes de devoir sont séparées entre eux par une barre verticale |
                         """)
            note = format_notes(note)
            if  validiter_notes(note) == True :
                classe_valide = True
    donne_eleve = {'code':code, 'numero': numero, 'nom': nom, 'prenom': prenom,'date_de_naissance': date_de_naissance, 'classe': classe, 'note': note }
    dico[numero] = donne_eleve
    print("information ajoutée avec succes")
    
    
    
    
def moyenne_generale(note) :
    moy_g = note['Math'][-1] + note['Francais'][-1] + note['Anglais'][-1] + note['SVT'][-1] + note['HG'][-1] + note['PC'][-1]
    
        



def separation_des_donnees_en_valide_et_invalide(dico) :

    dico_invalides = {}
    dico_valides = {}
    donne = {}

    for cle, valeur in dico.items() : 
        valeur_valide = 0
        val = ""
        for key, value in valeur.items() :
            if key == 'code' :
                if value != "" :
                    valeur_valide += 1
            
            elif key == "numero" :
                if is_valid_numero(value) == True :
                    valeur_valide += 1
                
            elif key == "nom" :
                if est_nom_valide(value) == True :
                    valeur_valide += 1
                
            elif key == "prenom" :
                if est_prenom_valide(value) == True :
                    valeur_valide += 1
                                    
            elif key == "date_de_naissance" :
                if date_de_naissance_valide(value) == True :
                    valeur_valide += 1
                         
            elif key == "classe" :
                if is_valid_classe(value) == True :
                    valeur_valide += 1
                  
            elif key == "note" :
                if validiter_notes(value) == True :
                    valeur_valide += 1



        if len(valeur) != valeur_valide :
                    dico_invalides[cle] = valeur
        else :
                    dico_valides[cle] = valeur
            
    return dico_valides,dico_invalides


