import random

def guess(x):
    i=0
    random_num=random.randint(1,x)
    guess=0
    while guess!=random_num:
        guess=int(input(f'Guess the number between 1 and {x}:'))
        if guess<random_num:
            print('Sorry try again. You are too low.')
            print('')
        elif guess>random_num:
            print('Soryy try again. You are too high.')
            print('')
        i=i+1
    print(f'Congratulations you have guessed the correct number i.e. {random_num}')
    print(f'Chances taken by you : {i}')
guess(100)