import random

### Rock beats Scissors, Scissors beats paper, Paper beats rock
##possible update is to verify valid inputs should I so choose.
options = ["Rock", "Paper", "Scissors"]
victory_conditions = {
        "Rock": "Scissors", #Rock beats Scissors,
        "Paper": "Rock", #Paper beats Rock
        "Scissors": "Paper", #scissors beats paper
    }
playerScore = 0
compScore = 0

def computer_play ():
    selection = random.randint(0, len(options) -1)
    return selection

def user_play ():
    while True:
        selection = input("Rock, Paper, Scissors! ").lower()
        opt = [opt.lower() for opt in options]
        try:
            selection in opt
            if selection == 'exit' or selection == 'quit':
                exit()
            index = opt.index(selection)
            return index
        except:
            print("Invalid Selection!")


def determine_winner (userPlay, computerPlay):
    defeats = victory_conditions[options[userPlay]]
    if userPlay != computerPlay:
        if options[computerPlay] in defeats:
            print(f"You Win! {options[userPlay]} beats {options[computerPlay]}!")
        else: print(f"You Lose! {options[computerPlay]} beats {options[userPlay]}!")
    else:
        print("It's a Tie!")

def play_round ():
    global playerScore
    global compScore
    computer = computer_play()
    player = user_play()
    determine_winner(player, computer)


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

