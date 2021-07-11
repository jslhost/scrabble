def scrabble() :


    import json, requests

    #A text file containing over 466k English words.
    r = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json')

    rep = r.json()

    all_words = set(rep)

    import sys
    import math

    # Auto-generated code below aims at helping you parse
    # the standard input according to the problem statement.
    dico = {1: ['a', 'e', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u'],
    2: ['d', 'g'],
    3: ['b', 'c', 'm', 'p'],
    4: ['f', 'h', 'v', 'w', 'y'],
    5: ['k'],
    8: ['j', 'x'],
    10: ['q', 'z']}

    #On récupère les différents mots possibles dans la liste 'mots'
    mots = all_words
    letters = ref = input('Please enter your seven letters : \n')


    #On crée une liste vérifiant les matchs lettres / mots donnés
    liste_match = []
    for mot in mots :
        mot_formé = []
        letters = ref
        for letter in mot :
            if letter in letters :
                mot_formé.append(letter)
                letters = letters.replace(letter, '', 1)

        mot_joint = ''.join(mot_formé)
        liste_match.append(mot_joint)


    #On vérifie quels matchs forment des mots de la liste initiale
    mots_possibles = [mot for mot in liste_match if mot in mots]


    #On compte les points pour chaque mot possible
    score = {}


    for mot in mots_possibles : 
        count = 0
        for letter in mot :
            for point, liste in dico.items() :
                if letter in liste :
                    count += point

        score[mot] = count


    #On cherche le score maximal
    max_score = max(score, key = score.get)

    dernier_mot = sorted(score)[-1]

    score_of_score = sorted(score.items())[-1][0]


    #On affiche la solution
    print(f'\nThis is all the words you can make : \n{score} \n')
    print(f'This is the best word you can make : {max_score} \n')