from datetime import datetime

name = input('What is your name?')
print('Greetings ' + name)
print(f'your name has {len(name)} letters')
birthDay = int(input('What month is your birthday on?(enter number)'))


if birthDay == datetime.now().month:
        print('sweet')
