import random

### Rock beats Scissors, Scissors beats paper, Paper beats rock
##possible update is to verify valid inputs should I so choose.
options = ["rock", "paper", "scissors"]
playerScore = 0
compScore = 0

def computer_play ():
    selection = random.randint(0, len(options) -1)
    return selection

def user_play ():
    selection = input("Rock, Paper, Scissors! ").lower()
    if selection == 'exit' or selection == 'quit':
        exit()
    index = options.index(selection)
    return index

def play_round ():
    global playerScore
    global compScore
    computer = computer_play()
    player = user_play()
    ##Player wins
    if player != computer:
        if player == 0 and computer == 2:
            playerScore += 1
            print("You win! Rock beats Scissors!")
        elif player == 1 and computer == 0:
            playerScore += 1
            print("You win! Paper beats Rock!")
        elif player == 2 and computer == 1:
            playerScore += 1
            print("You win! Scissors beats paper!")
    ##Comp wins
        elif player == 0 and computer == 1:
            compScore += 1
            print("You lose! Paper beats Rock!")
        elif player == 1 and computer == 2:
            compScore += 1
            print("You lose! Scissors beats Paper!")
        elif player == 2 and computer == 0:
            compScore += 1
            print("You lose! Rock beats Scissors!")
    else:
        print("It's a Tie!")





def game ():
    global playerScore
    global compScore
    print("Welcome to Rock, Paper, Scissors")
    print("To quit type exit.")
    wannaPlay = input("Do you want to play? [y/n] ").lower()
    while True:
        if wannaPlay == 'n' or wannaPlay == 'no' or wannaPlay == 'exit' or wannaPlay == "quit":
            exit()
        else:
            play_round()
            print(f"Current Score: \n    Player 1: {playerScore} \n    Computer Score: {compScore}")
            wannaPlay = input("Play again? [y/n] ")

game()

