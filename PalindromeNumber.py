# A function is created to check for palindrome number.

def palin(x):
    r=x[::-1] # reverses the number 
    if r==x:
        print('Palindrome number.')
    else:
        print('Not a palindrome number.')

num=input('Enter the number to check for palindrome.') # number is accepted as string
palin(num)