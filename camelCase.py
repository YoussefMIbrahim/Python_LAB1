def validate(word):
    badCharactors = ['=','+','-']
    if word[0].isdigit():
        return False
    if any(c in word for c in badCharactors):
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


