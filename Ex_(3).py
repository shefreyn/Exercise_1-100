LP = input("Let's play, yes or no ?")
while LP == 'yes':
    print('__ Welcome to treasure hunt __')
    leftOright = input('Left or Right : ')
    if leftOright == 'left':
        swimOwait = input('Swim or Wait : ')
        if swimOwait == 'wait':
            print('Red / Blue / Yellow')
            door = input('Choose a Door : ')
            if door == 'yellow':
                print('You Win ! :D')
            else:
                print('Game Overr !!')
        else:
            print('Game Over !!')
    else:
        print('Game Overr !!')
    game = input('Want to play again yes or no ? ')
    if game == 'no':
        break