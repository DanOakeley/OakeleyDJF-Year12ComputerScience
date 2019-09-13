#A program to play rock paper scissors.
import random
sHandPlayed = str(input("Please Pick one: R(rock), P(paper), S(scissors)"))
sOptions = ['R', 'S', 'P']
sComputerChoice = random.choice(sOptions)
if sComputerChoice == sHandPlayed
    print("Its a Draw")
if random.choice(sOptions) == 'R' and sHandPlayed == 'S'
    print("Rock Beats Scissors, Computer Wins")
if random.choice(sOptions) == 'R' and sHandPlayed == 'P'
    print("Paper beats Rock, You win!")
if random.choice(sOptions) == 'P' and sHandPlayed == 'R'
    print("Paper Beats Rock, Computer Wins")
if random.choice(sOptions) == 'P' and sHandPlayed == 'S'
    print("Scissors beat Paper, You Win!")
if random.choice(sOptions) == 'S' and sHandPlayed == 'P'
    print("Scissors beat Paper, Computer Wins")
if random.choice(sOptions) == 'S' and sHandPlayed == 'R'
    print("Rock beats Scissors, You Win!")

