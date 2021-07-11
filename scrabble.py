def scrabble() :


    import urllib

    #A text file containing French words
    liste = []
    url = "http://jph.durand.free.fr/scrabble.txt"
    file = urllib.request.urlopen(url)
    for line in file:
        liste.append(line)
        
    mots_francais = set()
    for elt in liste[1:] :
        mots_francais.add(elt.decode('utf-8').strip())


    #Points by letter
    dico = {1: ['A', 'E', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']}

    #Initialization of dict of words and input letters
    mots = mots_francais
    letters = ref = input('Please enter your seven letters (capitalize) : \n')


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


    #Displaying
    print(f'\nThis is all the words you can make : \n{score} \n')
    print(f'This is the best word you can make : {max_score} \n')
