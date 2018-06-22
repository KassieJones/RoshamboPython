from random import randint

def roshambo():
    random_number = randint(0,2)
    if random_number == 1:
        response = 'Rock'
    elif random_number == 2:
        response = 'Paper'
    else:
        response = 'Scissors'
    return response

if __name__ == '__main__':
    cont = 'y'
    cont2 = 'y'
    print('Welcome to Rock, Paper, Scissors!')
    username = input('Enter your name: ')

    while cont.lower() == 'y':
        opponent_name = input('Would you like to play TheJets or TheSharks? J / S ')

        if opponent_name.lower() == 'j' or opponent_name.lower() == 's':
           # while cont2.lower() == 'y':
                user_choice = input('Rock, paper, or scissors?  R / P / S ')

                if user_choice.lower() == 'r':
                    print(username + ': ' + 'Rock')
                    if opponent_name.lower() == 'j':
                        print('TheJets: ' + roshambo())
                    elif opponent_name.lower() == 's':
                        print('TheSharks: ' + roshambo())
                    cont = input('Play again? Y / N ')
                elif user_choice.lower() == 'p':
                    print(username + ': ' + 'Paper')
                    if opponent_name.lower() == 'j':
                        print('TheJets: ' + roshambo())
                    elif opponent_name.lower() == 's':
                        print('TheSharks: ' + roshambo())
                    cont = input('Play again? Y / N ')
                elif user_choice.lower() == 's':
                    print(username + ': ' + 'Scissors')
                    if opponent_name.lower() == 'j':
                        print('TheJets: ' + roshambo())
                    elif opponent_name.lower() == 's':
                        print('TheSharks: ' + roshambo())
                    cont = input('Play again? Y / N ')
                else:
                    print('Please enter a valid selection.')
                    #cont2 = 'y'
        else:
            print('Please enter a valid selection')
            cont = 'y'

    print('Thanks for playing!  See You next time!')