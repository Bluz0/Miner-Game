import random


def affiche(grille): 
    #parcours des lignes
    for ligne in grille:
        ligne_a_afficher='|'
        #construction de la ligne à afficher
        for cases in ligne:
            ligne_a_afficher+=cases+'|'
        print(ligne_a_afficher)


def demineur():

    #Grille présentant les emplacements des cases
    presentation_grille = [
        ['A1','A2','A3','A4','A5','A6','A7'],
        ['B1','B2','B3','B4','B5','B6','B7'],
        ['C1','C2','C3','C4','C5','C6','C7'],
        ['D1','D2','D3','D4','D5','D6','D7'],
        ['E1','E2','E3','E4','E5','E6','E7'],
        ['F1','F2','F3','F4','F5','F6','F7'],
        ['G1','G2','G3','G4','G5','G6','G7']
    ]

    #Grille contenant les cases
    grille = [
        [' ',' ',' ',' ',' ',' ',' '],  
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ']
    ]



    #Affichage de la grille pour informer le joueur des caracteres des cases
    print('Vous avez oublié les cases de la grille ? Les voici : ')
    affiche(presentation_grille)



    # Reperage des differents objets

    MINE = '¤'    # Caractère d'une mine
    DRAPEAU = '#'    # Caractère d'un drapeau
    NON_CREUSÉ = ' '  # Case non creusé, donc disponible

demineur()

def bombes(grille): # Fonction qui va permettre de placer des bombes et afficher la grille pour jouer
    """ Cette Fonction va permettre de placer des bombes aléatoirement dans notre grille 
    - Préconditions : La grille est un tableau de tableau contenant 49 cases
    - Post-Conditions : La grille retourner contient 7 bombes réparti aléatoirement dans la grille en ligne et/ou colonne.
    
    Cas attendu de la fonction :
    
    >>> bombes(grille)
        [[' ', ' ', ' ', '¤', ' ', ' ', '¤'],
        [' ', ' ', ' ', ' ', ' ', '¤', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', '¤', '¤', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['¤', ' ', ' ', ' ', ' ', ' ', '¤']]
    
    """
    
    nb_bombes = 0
    while nb_bombes != 7 :
        i = random.randint(0,6) #Choix d'une ligne de la grille 
        j = random.randint(0,6) #Choix d'une colonne de la grille
        if grille[i][j] == ' ':
            grille[i][j] = '¤' #Placement d'une bombe dans une ligne ou une colonne
            nb_bombes = nb_bombes + 1
    return grille


if __name__== '__main__':
    import doctest
    doctest.testmod()

#Si les testes disent que il y a une "failure" c'est normal, le programme propose un placement de bombes differents dans l'argument (grille), on rappelle qu'il utilise la bibliotheque random.


def compteur_case(grille):
    """ Cette fonction va permettre de placer, pour chacune des cases autour, le nombre de bombes, le chiffre exact sera dans la case.
    - Préconditions : La grille est un tableau de tableau contenant 49 cases, 7 bombes sont placés sur les 49 cases aléatoirement.
    - Post-Conditions : Les cases de la grille nous retournera le nombre de bombes, elle contiendera le nombre de bombes converti en string.
    
    Cas attendu de la fonction : 
    
    >>> compteur_case(grille)
        [['0', '0', '1', '¤', '2', '2', '¤'],
        ['0', '0', '1', '1', '2', '¤', '2'], 
        ['0', '0', '0', '0', '1', '1', '1'], 
        ['1', '2', '2', '1', '0', '0', '0'], 
        ['1', '¤', '¤', '1', '0', '0', '0'], 
        ['1', '2', '2', '1', '0', '1', '1'], 
        ['¤', '1', '0', '0', '0', '1', '¤']]
        
        """






    for i in range(1,5+1): #On parcours notre grille
        for j in range(1,5+1):
            if grille[i][j] != '¤':
                nb_bombes = 0
                if grille[i-1][j-1] == '¤': # Pour une case choisi qui ne contient pas de bombes, on verifie autour de cette case combien il y a de bombes.
                    nb_bombes = nb_bombes+1
                if grille[i-1][j] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i-1][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                grille[i][j] = str(nb_bombes)
    for i in range(1,5+1):
        j = 6 # De [1;6] à [5;6]
        if grille[i][j] != '¤':
                nb_bombes = 0
                if grille[i-1][j] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i-1][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j] == '¤':
                    nb_bombes = nb_bombes+1
                grille[i][j] = str(nb_bombes)
    for i in range(1,5+1):
        j = 0
        if grille[i][j] != '¤':
                nb_bombes = 0
                if grille[i-1][j] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i-1][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j] == '¤':
                    nb_bombes = nb_bombes+1
                grille[i][j] = str(nb_bombes)
    for j in range(1,5+1): # De [0;1] à [0;5]
        i = 0
        if grille[i][j] != '¤':
                nb_bombes = 0
                if grille[i][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i+1][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                grille[i][j] = str(nb_bombes)
    for j in range(1,5+1): # De [6;1] à [6;5]
        i = 6
        if grille[i][j] != '¤':
                nb_bombes = 0
                if grille[i][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i-1][j+1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i-1][j] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i-1][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                if grille[i][j-1] == '¤':
                    nb_bombes = nb_bombes+1
                grille[i][j] = str(nb_bombes)
    
    if grille[0][0] != '¤': # Grille [0][0]
        nb_bombes = 0
        if grille[0][0+1] == '¤':
            nb_bombes = nb_bombes+1
        if grille[0+1][0+1] == '¤':
            nb_bombes = nb_bombes+1
        if grille[0+1][0] == '¤':
            nb_bombes = nb_bombes+1
        grille[0][0] = str(nb_bombes)

    if grille[6][0] != '¤': #Grille [6][0]
        nb_bombes = 0
        if grille[6][0+1] == '¤':
            nb_bombes = nb_bombes+1
        if grille[6-1][0+1] == '¤':
            nb_bombes = nb_bombes+1
        if grille[6-1][0] == '¤':
            nb_bombes = nb_bombes+1
        grille[6][0] = str(nb_bombes)

    if grille[0][6] != '¤': #Grille [0][6]
        nb_bombes = 0
        if grille[0+1][6] == '¤':
            nb_bombes = nb_bombes+1
        if grille[0][6-1] == '¤':
            nb_bombes = nb_bombes+1
        if grille[0+1][6-1] == '¤':
            nb_bombes = nb_bombes+1
        grille[0][6] = str(nb_bombes)

    if grille[6][6] != '¤':
        nb_bombes = 0
        if grille[6][6-1] == '¤':
            nb_bombes = nb_bombes+1
        if grille[6-1][6] == '¤':
            nb_bombes = nb_bombes+1
        if grille[6-1][6-1] == '¤':
            nb_bombes = nb_bombes+1
        grille[6][6] = str(nb_bombes)

    return grille

if __name__== '__main__':
    import doctest
    doctest.testmod()



def jeu(grille,grille_cache,nb_drapeau):
    """Cette fonction polyvalente va faire marcher en réalité 2 fonctions, la fonction jeu va en premier temps : 1° géré le nombre de drapeau placé sur une grille "caché",
    2° géré l'apparition des numéros qui indique les bombes aux alentours, elle gere aussi quand on tombe sur une bombe directement.
    
    - Préconditions : La grille contient les bombes et les nombres de bombes sur les cases.
                      La grille caché est contient les memes caracteristiques que la grille mais elles sont masquées.
                      Le nombre de drapeau sont des entiers au nombre de 7 
    
    - Post-Conditions : A chaque reponse de "Quel case choisissez vous ?" on retourne la grille caché avec les modifications.
    Si le mot ou le numero de case est mal referencé le programme repose la question 

    >>> jeu(grille,grille_cache,nb_drapeau)
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |

    """

    affiche(grille_cache)
    while nb_drapeau != 8 : # On veut poser ( si on veut pousser le programme loin ) 7 drapeaux , mais si on met ..!= 7 le programme va s'arreter.
        case1 = input('Voulez vous creusez ou poser un drapeau ?')
        if case1 == "drapeau":
            case2 = input('Quel case choisissez vous ?')
            if case2 == "A1" and grille_cache[0][0] == " " :
                grille_cache[0][0] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "A2" and grille_cache[0][1] == " ":
                grille_cache[0][1] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "A3" and grille_cache[0][2] == " ":
                grille_cache[0][2] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "A4" and grille_cache[0][3] == " ":
                grille_cache[0][3] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "A5" and grille_cache[0][4] == " ":
                grille_cache[0][4] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "A6" and grille_cache[0][5] == " ":
                grille_cache[0][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "A6" and grille_cache[0][5] == " ":
                grille_cache[0][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "A7" and grille_cache[0][6] == " ":
                grille_cache[0][6] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "A6" and grille_cache[0][5] == " ":
                grille_cache[0][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "B1" and grille_cache[1][0] == " ":
                grille_cache[1][0] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "B2" and grille_cache[1][1] == " ":
                grille_cache[1][1] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "B3" and grille_cache[1][2] == " ":
                grille_cache[1][2] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "B4" and grille_cache[1][3] == " ":
                grille_cache[1][3] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "B5" and grille_cache[1][4] == " ":
                grille_cache[1][4] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "B6" and grille_cache[1][5] == " ":
                grille_cache[1][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "B7" and grille_cache[1][6] == " ":
                grille_cache[1][6] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "C1" and grille_cache[2][0] == " ":
                grille_cache[2][0] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "C2" and grille_cache[2][1] == " ":
                grille_cache[2][1] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "C3" and grille_cache[2][2] == " ":
                grille_cache[2][2] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "C4" and grille_cache[2][3] == " ":
                grille_cache[2][3] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "C5" and grille_cache[2][4] == " ":
                grille_cache[2][4] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "C6" and grille_cache[2][5] == " ":
                grille_cache[2][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "C7" and grille_cache[2][6] == " ":
                grille_cache[2][6] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "D1" and grille_cache[3][0] == " ":
                grille_cache[3][0] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "D2" and grille_cache[3][1] == " ":
                grille_cache[3][1] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "D3" and grille_cache[3][2] == " ":
                grille_cache[3][2] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "D4" and grille_cache[3][3] == " ":
                grille_cache[3][3] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "D5" and grille_cache[3][4] == " ":
                grille_cache[3][4] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "D6" and grille_cache[3][5] == " ":
                grille_cache[3][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "D7" and grille_cache[3][6] == " ":
                grille_cache[3][6] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "E1" and grille_cache[4][0] == " ":
                grille_cache[4][0] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "E2" and grille_cache[4][1] == " ":
                grille_cache[4][1] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "E3" and grille_cache[4][2] == " ":
                grille_cache[4][2] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "E4" and grille_cache[4][3] == " ":
                grille_cache[4][3] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "E5" and grille_cache[4][4] == " ":
                grille_cache[4][4] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "E6" and grille_cache[4][5] == " ":
                grille_cache[4][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "E7" and grille_cache[4][6] == " ":
                grille_cache[4][6] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "F1" and grille_cache[5][0] == " ":
                grille_cache[5][0] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "F2" and grille_cache[5][1] == " ":
                grille_cache[5][1] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "F3" and grille_cache[5][2] == " ":
                grille_cache[5][2] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "F4" and grille_cache[5][3] == " ":
                grille_cache[5][3] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "F5" and grille_cache[5][4] == " ":
                grille_cache[5][4] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "F6" and grille_cache[5][5] == " ":
                grille_cache[5][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "F7" and grille_cache[5][6] == " ":
                grille_cache[5][6] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "G1" and grille_cache[6][0] == " ":
                grille_cache[6][0] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "G2" and grille_cache[6][1] == " ":
                grille_cache[6][1] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "G3" and grille_cache[6][2] == " ":
                grille_cache[6][2] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "G4" and grille_cache[6][3] == " ":
                grille_cache[6][3] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "G5" and grille_cache[6][4] == " ":
                grille_cache[6][4] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "G6" and grille_cache[6][5] == " ":
                grille_cache[6][5] = '#'
                nb_drapeau = nb_drapeau+1
            elif case2 == "G7" and grille_cache[6][6] == " ":
                grille_cache[6][6] = '#'
                nb_drapeau = nb_drapeau+1


        if case1 == "creuser":
            case2 = input('Quel case choisissez vous ?')
            if case2 == "A1" and grille_cache[0][0] == " ":
                if grille[0][0] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                    
                
                if grille[0][0] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[0][0] = grille[0][0]
                
                if grille[0][0] == '0':
                    grille_cache[0][0] = '0'


            if case2 == "A2" and grille_cache[0][1] == " ":
                if grille[0][1] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[0][1] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[0][1] = grille[0][1]
                
                if grille[0][1] == '0':
                    grille_cache[0][1] = '0'


            if case2 == "A3" and grille_cache[0][2] == " ":
                if grille[0][2] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[0][2] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[0][2] = grille[0][2]
                
                if grille[0][2] == '0':
                    grille_cache[0][2] = '0'


            if case2 == "A4" and grille_cache[0][3] == " ":
                if grille[0][3] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[0][3] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[0][3] = grille[0][3]
                
                if grille[0][3] == '0':
                    grille_cache[0][3] = '0'


            if case2 == "A5" and grille_cache[0][4] == " ":
                if grille[0][4] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[0][4] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[0][4] = grille[0][4]
                
                if grille[0][4] == '0':
                    grille_cache[0][4] = '0'
            

            if case2 == "A6" and grille_cache[0][5] == " ":
                if grille[0][5] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[0][5] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[0][5] = grille[0][5]
                
                if grille[0][5] == '0':
                    grille_cache[0][5] = '0'
            
            if case2 == "A7" and grille_cache[0][6] == " ":
                if grille[0][6] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[0][6] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[0][6] = grille[0][6]
                
                if grille[0][6] == '0':
                    grille_cache[0][6] = '0'

            if case2 == "B1" and grille_cache[1][0] == " ":
                if grille[1][0] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[1][0] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[1][0] = grille[1][0]
                
                if grille[1][0] == '0':
                    grille_cache[1][0] = '0'
            
            if case2 == "B2" and grille_cache[1][1] == " ":
                if grille[1][1] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[1][1] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[1][1] = grille[1][1]
                
                if grille[1][1] == '0':
                    grille_cache[1][1] = '0'
            
            if case2 == "B3" and grille_cache[1][2] == " ":
                if grille[1][2] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[1][2] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[1][2] = grille[1][2]
                
                if grille[1][2] == '0':
                    grille_cache[1][2] = '0'
            
            if case2 == "B4" and grille_cache[1][3] == " ":
                if grille[1][3] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[1][3] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[1][3] = grille[1][3]
                
                if grille[1][3] == '0':
                    grille_cache[1][3] = '0'
            
            if case2 == "B5" and grille_cache[1][4] == " ":
                if grille[1][4] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[1][4] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[1][4] = grille[1][4]
                
                if grille[1][4] == '0':
                    grille_cache[1][4] = '0'

            if case2 == "B6" and grille_cache[1][5] == " ":
                if grille[1][5] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[1][5] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[1][5] = grille[1][5]
                
                if grille[1][5] == '0':
                    grille_cache[1][5] = '0'
            
            if case2 == "B7" and grille_cache[1][6] == " ":
                if grille[1][6] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[1][6] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[1][6] = grille[1][6]
                
                if grille[1][6] == '0':
                    grille_cache[1][6] = '0'

            if case2 == "C1" and grille_cache[2][0] == " ":
                if grille[2][0] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[2][0] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[2][0] = grille[2][0]
                
                if grille[2][0] == '0':
                    grille_cache[2][0] = '0'
            
            if case2 == "C2" and grille_cache[2][1] == " ":
                if grille[2][1] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[2][1] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[2][1] = grille[2][1]
                
                if grille[2][1] == '0':
                    grille_cache[2][1] = '0'
            
            if case2 == "C3" and grille_cache[2][2] == " ":
                if grille[2][2] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[2][2] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[2][2] = grille[2][2]
                
                if grille[2][2] == '0':
                    grille_cache[2][2] = '0'
            
            if case2 == "C4" and grille_cache[2][3] == " ":
                if grille[2][3] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[2][3] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[2][3] = grille[2][3]
                
                if grille[2][3] == '0':
                    grille_cache[2][3] = '0'
            
            if case2 == "C5" and grille_cache[2][4] == " ":
                if grille[2][4] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[2][4] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[2][4] = grille[2][4]
                
                if grille[2][4] == '0':
                    grille_cache[2][4] = '0'

            if case2 == "C6" and grille_cache[2][5] == " ":
                if grille[2][5] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[2][5] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[2][5] = grille[2][5]
                
                if grille[2][5] == '0':
                    grille_cache[2][5] = '0'
            
            if case2 == "C7" and grille_cache[2][6] == " ":
                if grille[2][6] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[2][6] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[2][6] = grille[2][6]
                
                if grille[2][6] == '0':
                    grille_cache[2][6] = '0'

            if case2 == "D1" and grille_cache[3][0] == " ":
                if grille[3][0] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[3][0] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[3][0] = grille[3][0]
                
                if grille[3][0] == '0':
                    grille_cache[3][0] = '0'
            
            if case2 == "D2" and grille_cache[3][1] == " ":
                if grille[3][1] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[3][1] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[3][1] = grille[3][1]
                
                if grille[3][1] == '0':
                    grille_cache[3][1] = '0'
            
            if case2 == "D3" and grille_cache[3][2] == " ":
                if grille[3][2] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[3][2] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[3][2] = grille[3][2]
                
                if grille[3][2] == '0':
                    grille_cache[3][2] = '0'
            
            if case2 == "D4" and grille_cache[3][3] == " ":
                if grille[3][3] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[3][3] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[3][3] = grille[3][3]
                
                if grille[3][3] == '0':
                    grille_cache[3][3] = '0'
            
            if case2 == "D5" and grille_cache[3][4] == " ":
                if grille[3][4] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[3][4] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[3][4] = grille[3][4]
                
                if grille[3][4] == '0':
                    grille_cache[3][4] = '0'

            if case2 == "D6" and grille_cache[3][5] == " ":
                if grille[3][5] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[3][5] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[3][5] = grille[3][5]
                
                if grille[3][5] == '0':
                    grille_cache[3][5] = '0'
            
            if case2 == "D7" and grille_cache[3][6] == " ":
                if grille[3][6] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[3][6] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[3][6] = grille[3][6]
                
                if grille[3][6] == '0':
                    grille_cache[3][6] = '0'

            if case2 == "E1" and grille_cache[4][0] == " ":
                if grille[4][0] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[4][0] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[4][0] = grille[4][0]
                
                if grille[4][0] == '0':
                    grille_cache[4][0] = '0'
            
            if case2 == "E2" and grille_cache[4][1] == " ":
                if grille[4][1] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[4][1] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[4][1] = grille[4][1]
                
                if grille[4][1] == '0':
                    grille_cache[4][1] = '0'
            
            if case2 == "E3" and grille_cache[4][2] == " ":
                if grille[4][2] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[4][2] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[4][2] = grille[4][2]
                
                if grille[4][2] == '0':
                    grille_cache[4][2] = '0'
            
            if case2 == "E4" and grille_cache[4][3] == " ":
                if grille[4][3] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[4][3] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[4][3] = grille[4][3]
                
                if grille[4][3] == '0':
                    grille_cache[4][3] = '0'
            
            if case2 == "E5" and grille_cache[4][4] == " ":
                if grille[4][4] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[4][4] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[4][4] = grille[4][4]
                
                if grille[4][4] == '0':
                    grille_cache[4][4] = '0'

            if case2 == "E6" and grille_cache[4][5] == " ":
                if grille[4][5] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[4][5] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[4][5] = grille[4][5]
                
                if grille[4][5] == '0':
                    grille_cache[4][5] = '0'
            
            if case2 == "E7" and grille_cache[4][6] == " ":
                if grille[4][6] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[4][6] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[4][6] = grille[4][6]
                
                if grille[4][6] == '0':
                    grille_cache[4][6] = '0'
            
            if case2 == "F1" and grille_cache[5][0] == " ":
                if grille[5][0] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[5][0] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[5][0] = grille[5][0]
                
                if grille[5][0] == '0':
                    grille_cache[5][0] = '0'
            
            if case2 == "F2" and grille_cache[5][1] == " ":
                if grille[5][1] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[5][1] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[5][1] = grille[5][1]
                
                if grille[5][1] == '0':
                    grille_cache[5][1] = '0'
            
            if case2 == "F3" and grille_cache[5][2] == " ":
                if grille[5][2] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[5][2] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[5][2] = grille[5][2]
                
                if grille[5][2] == '0':
                    grille_cache[5][2] = '0'
            
            if case2 == "F4" and grille_cache[5][3] == " ":
                if grille[5][3] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[5][3] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[5][3] = grille[5][3]
                
                if grille[5][3] == '0':
                    grille_cache[5][3] = '0'
            
            if case2 == "F5" and grille_cache[5][4] == " ":
                if grille[5][4] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[5][4] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[5][4] = grille[5][4]
                
                if grille[5][4] == '0':
                    grille_cache[5][4] = '0'

            if case2 == "F6" and grille_cache[5][5] == " ":
                if grille[5][5] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[5][5] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[5][5] = grille[5][5]
                
                if grille[5][5] == '0':
                    grille_cache[5][5] = '0'
            
            if case2 == "F7" and grille_cache[5][6] == " ":
                if grille[5][6] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[5][6] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[5][6] = grille[5][6]
                
                if grille[5][6] == '0':
                    grille_cache[5][6] = '0'
            
            if case2 == "G1" and grille_cache[6][0] == " ":
                if grille[6][0] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[6][0] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[6][0] = grille[6][0]
                
                if grille[6][0] == '0':
                    grille_cache[6][0] = '0'
            
            if case2 == "G2" and grille_cache[6][1] == " ":
                if grille[6][1] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[6][1] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[6][1] = grille[6][1]
                
                if grille[6][1] == '0':
                    grille_cache[6][1] = '0'
            
            if case2 == "G3" and grille_cache[6][2] == " ":
                if grille[6][2] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[6][2] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[6][2] = grille[6][2]
                
                if grille[6][2] == '0':
                    grille_cache[6][2] = '0'
            
            if case2 == "G4" and grille_cache[6][3] == " ":
                if grille[6][3] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[6][3] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[6][3] = grille[6][3]
                
                if grille[6][3] == '0':
                    grille_cache[6][3] = '0'
            
            if case2 == "G5" and grille_cache[6][4] == " ":
                if grille[6][4] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[6][4] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[6][4] = grille[6][4]
                
                if grille[6][4] == '0':
                    grille_cache[6][4] = '0'

            if case2 == "G6" and grille_cache[6][5] == " ":
                if grille[6][5] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[6][5] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[6][5] = grille[6][5]
                
                if grille[6][5] == '0':
                    grille_cache[6][5] = '0'
            
            if case2 == "G7" and grille_cache[6][6] == " ":
                if grille[6][6] == '¤':
                    print("Mince , vous avez fini en purée, Dommage !")
                    return 'Erreur'
                
                if grille[6][6] in ["1","2","3","4","5","6","7","8"]:
                    grille_cache[6][6] = grille[6][6]
                
                if grille[6][6] == '0':
                    grille_cache[6][6] = '0'


        
          
        return grille_cache,nb_drapeau

if __name__== '__main__':
    import doctest
    doctest.testmod()
        


grille =[
    [' ',' ',' ',' ',' ',' ',' '],  
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ']
]

grille = bombes(grille)
print(grille)
grille = compteur_case(grille)
affiche(grille)

grille_cache = [
        [' ',' ',' ',' ',' ',' ',' '],  
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ']
    ]

nb_drapeau = 0
while grille_cache != ' ': # Le boucleur
    grille_cache,nb_drapeau=jeu(grille,grille_cache,nb_drapeau)
    if grille_cache == 'Erreur': #Si la grille caché rencontre un "return erreur"
        break # Le programme va s'arreter 



 



