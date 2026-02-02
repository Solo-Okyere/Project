# import pygame, math, sys, time
# pygame.init();pygame.mixer.init()
# W,H = 800,600; S = pygame.display.set_mode((W,H))

# def tone(f):
#     sr = 22050 ; n = int(sr * 0.2); b = bytearray(n*2)
#     for i in range(n):
#         s = int(30000*math.sin(2*math.pi*f*i/sr))
#         b[2*i]=s&255;b[2*i+1]=(s>>8)&255
#     return pygame.mixer.Sound(buffer=bytes(b))

# freq ={'C' : 261,'D':293,'E':329,'F':349,'G':392, 'A':440, 'B':400}

# import random

# players = ['kiriku', 'barnes', 'max', 'ken','kobby','hasnoend', 'dr.johnson']

# randomPlayer = random.choice(players)
# print(randomPlayer)

# match = 0
# while True:
#     player2 = input("Enter your name: ")
#     if player2 not in players:
#         players.append(player2)
#         print(f'{randomPlayer} VS {player2}')
#         match +=1
#     elif randomPlayer == player2:
#         print('Try again')

#     else:
#         print(f'{player2} VS {randomPlayer}')

#     if match == 3:
#         break


import random

userScore = 0

computerScore = 0

choice = ['rock', 'paper', 'scissors']

computer_choice = random.choice(choice)

ready = input("Would you like to play this game? Yes/No: ").lower()
while True:
    userChoice = input("Type rock, paper, or scissors: ").lower()

    if userChoice not in choice:
        print('Invalid choice')

    elif userChoice == computer_choice:
        print(f'You chose {userChoice} and computer chose {computer_choice}')
        print('It is a tie')

    elif userChoice == "rock" and computer_choice == "scissors":
        print(f"You chose {userChoice}, computer chose {computer_choice}")
        print("You win!")
        userScore +=1

    elif userChoice == "paper" and computer_choice == "rock":
            print(f"You chose {userChoice}, computer chose {computer_choice}")
            print("You win!")
            userScore +=1

    elif userChoice == "scissors" and computer_choice == "paper":
        print(f"You chose {userChoice}, computer chose {computer_choice}")
        print("You win!")
        userScore +=1

    else:
        print(f"You chose {userChoice}, computer chose {computer_choice}")
        print("Computer wins!")
        computerScore +=1
    
