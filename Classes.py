classes = []



while True:
    course = input('Enter the name of the course that you are taking(leave blank to stop)')
    classes.append(course)

    if not course:
        break

print('Here are your courses')
for c in classes:
    print(c)