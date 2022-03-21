import random

def play():
    user=input("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer=random.choice(['r','p','s'])

    ## rules-  r>s p>r s>p
    if user==computer:
        return 'Tie'
    
    if win(user,computer):
        print('You Win.Computer\'s choice: {computer}')

    return(f'You Lost.Computer\'s choice: {computer}')
     


def win(player,opponent):
        if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
            return True
    
print(play())

