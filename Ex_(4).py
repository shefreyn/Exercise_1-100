import random
print('__ RPS - Rock Paper Scissor__ ')                                                                 #1:rock 2.Paper 3.scissors
userInput = input('Choose your input : ')
compInput = 2
compInput = random.randint(1,3)
print(f"Computer chose {compInput}")
if userInput == '1':
    if compInput == 2:
                print("Computer Wins !! :P")
    elif compInput == 3:
        print('You Win ! :D')
    else:
        print("It's a Tie - cond 1")
elif userInput == '2':
    if compInput == 1:
        print("You Win ! :D")
    elif compInput == 3:
        print("Computer Wins !! :P")
    else:
        print("It's a Tie - cond 2")
elif userInput == '3':
    if compInput == 1:
        print("Computer Win's !! :P")
    elif compInput == 2:
        print("You Win !! :D")
    else:
        print("It's a Tie - cond 3")
else:
    print("Invalid Choice ! ")
