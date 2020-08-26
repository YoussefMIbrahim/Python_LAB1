def validate(word):
    badCharactors = ['=','+','-'] # list of bad characters 
    if word[0].isdigit(): # checking if the first character is a digit
        return False
    if any(c in word for c in badCharactors): # checking if any of the bad characters in the list are in the word
        return False
    return True

word = input('Write some words ')

if validate(word):

    wordList = word.split()

    newWord = ''
    for w in wordList:
        newWord = newWord + w.capitalize()

    print(newWord)
else:
    print('String contains charcters that will prevent proper conversion.')


