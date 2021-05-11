import random


def play():
    player = input(f"Let's begin the game!!\n there are three options\nr for ROCK \np for PAPER\ns for SCISSOR\n")
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return 'TIE'
    # p>r ,s>p,r>s
    if (player == 'p' and computer == 'r') or (player == 's' and computer == 'p') or (
            player == 'r' and computer == 's'):
        return f"YOU WON!!!"
    
    return f"YOU LOST"


print(play())
