import random

def input_human_play(input=input):
    play = input("rock, paper, or scissors?")
    while not is_valid_play:
        play = input("rock, paper, or scissors?")

def is_valid_play(play):
    return play in ["rock", "paper", "scissors"]

def generate_computer_play():
    return random.choice(["rock", "paper", "scissors"])


def evaluate_game(human, computer):
    if human == computer:
        return "tie"
    elif human == "rock":
        if computer == "paper":
            return "computer"
        else:
            return "human"
    elif human == "paper":
        if computer == "scissors":
            return "computer"
        else:
            return "human"
    else:
        if computer == "rock":
            return "computer"
        else:
            return "human"


def main(input=input): #muj_input = input

    human = input_human_play(input) #muj_input
    computer = generate_computer_play()


    print(computer)
    game = evaluate_game(human, computer)
    if game == "tie":
        print("It´s a tie!")
    else:
        print(f"{game} won")

if __name__ == "__main__":  #když se spustí hlavní modul
    main()


"""
    if human == computer:
        print("It´s a tie!")

    elif (human == "rock" and computer == "paper") or (human == "paper" and computer == "scissors") or (human == "scissors" and computer == "rock"):
        print("Computer won!")

    elif (computer == "rock" and human == "paper") or (computer == "paper" and human == "scissors") or (computer == "scissors" and human == "rock"):
        print("You won!")

"""
