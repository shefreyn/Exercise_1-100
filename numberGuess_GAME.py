import random
compInput = random.randint(1,10)
life = 3
def uInput():
    
    userInput = input('Guess the number : ')
    userInput = int(userInput)
    print(f'You have chose number {userInput}')
    return userInput


print(f'comp chose : {compInput}')

while life != 0 :
    #Input and random number
    userInput= uInput()
    if userInput == compInput :
        print('You win !')
        break
    else :
        life -= 1
        print(f'lives left : {life}')
        if compInput % 2 == 0 or compInput % 3 == 0 :
            print('Hint : the number is divisible by 2 or 3')
        elif userInput < compInput:
            print('Hint : the number is greater')
        elif userInput > compInput:
            print('Hint : the number is lesser')
        
        
        

        