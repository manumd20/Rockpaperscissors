import random
import re
def game():
    while (1<2):
        print("\n")
        print("Rock ,Paper, Scissors")
        userChoice = input("please chosse: [R]ock],[P]aper, or [S]cissors: ")

        #making a condition if the user input other than three given words
        if not re.match("[SsRrPp]" , userChoice):
            print ("please choose a letter:")
            print ("[R]ock, [S]cissors or [P]aper.")
            continue

        print ("you have chosen: " + userChoice)
        choices = ['R', 'P' , 'S']
        opponentChoice = random.choice(choices)
        print ("i have chosen:" + opponentChoice)

        if opponentChoice == str.upper(userChoice):
            print ('Tie!')
        elif opponentChoice == 'R' and userChoice.upper() == 'S':
            print ("Scissor beats rock, I win!")
            continue
        elif opponentChoice == 'S' and userChoice.upper() == 'P':
            print ("Scissor beats paper!, I win!")
            continue
        elif opponentChoice == 'P' and userChoice.upper() == 'R':
            print ("Paper beats rock, I win!")
            continue
        else:
            print ("you win!")

#Calling the game function
game()


