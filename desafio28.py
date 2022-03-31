import random

insertNumber = int(input('Insert a number from 0 to 5: '))
randomNumber = random.randint(0, 5)  # Real number generator

if insertNumber == randomNumber:
    print('Congratulations! this is the number that the machine generated.')
else:
    print('You missed :( The real number was {}'.format(randomNumber))

