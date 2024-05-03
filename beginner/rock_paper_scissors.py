
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = "r"
    PAPER = "p"
    SCISSORS = "s"

def play_rps():
    """
    This function plays a game of Rock, Paper, Scissors between the user and the computer.

    The function first prompts the user to choose either Rock, Paper, or Scissors.
    It then generates a random choice for the computer.
    The function then determines the winner based on the rules of Rock, Paper, Scissors.
    It prints the result of the game and prompts the user if they want to play again.
    """
    playerchoice = input("Choose either\n1.Rock\n2.Paper\n3.Scissors?  ")
    print(playerchoice)

    if playerchoice not in ["s","p","r"]:
        print("You have entered a wrong input!!")
        return play_rps()

    player = playerchoice

    computerchoice = random.choice("rps")
    computer = computerchoice

    print("\nYou chose "+str(RPS(player)).replace('RPS.','').title() + ".")
    print("\nPython chose "+str(RPS(computer)).replace('RPS.','').title() + ".")

    def decide_winner(player,computer):
        """
        This function determines the winner of a game of Rock, Paper, Scissors.

        It takes two arguments: the player's choice and the computer's choice.
        It returns a string indicating the winner of the game.
        """
        if player == "r" and computer == "s":
            return "🎉 You win!"
        elif player == "p" and computer == "r":
            return  "🎉 You win!"
        elif player == "s" and computer == "p":
            return  "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "Python wins!!"

    game_result = decide_winner(player,computer)  

    print(game_result) 
    print("\n Wanna Play Again ? ")

    while True:
        playagain = input("\nY for Yes or \nQ for Quit  ")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")

play_rps()
