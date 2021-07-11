def scrabble() :


    import json, requests

    #A text file containing over 466k English words
    r = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json')

    rep = r.json()

    all_words = set(rep)


    #Points by letter
    dico = {1: ['a', 'e', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u'],
    2: ['d', 'g'],
    3: ['b', 'c', 'm', 'p'],
    4: ['f', 'h', 'v', 'w', 'y'],
    5: ['k'],
    8: ['j', 'x'],
    10: ['q', 'z']}

    #Initialization of dict of words and input letters
    mots = all_words
    letters = ref = input('Please enter your seven letters : \n')


    #Create a list verifying the match between letters and words
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


    #Verify if the words match the initial list of words
    mots_possibles = [mot for mot in liste_match if mot in mots]


    #We count the points in score
    score = {}


    for mot in mots_possibles : 
        count = 0
        for letter in mot :
            for point, liste in dico.items() :
                if letter in liste :
                    count += point

        score[mot] = count


    #We search the best score
    max_score = max(score, key = score.get)

    dernier_mot = sorted(score)[-1]

    score_of_score = sorted(score.items())[-1][0]


    #Displaying
    print(f'\nThis is all the words you can make : \n{score} \n')
    print(f'This is the best word you can make : {max_score} \n')
