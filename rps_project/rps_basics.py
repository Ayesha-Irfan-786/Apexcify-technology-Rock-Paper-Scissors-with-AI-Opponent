# rps_basic.py
import random

CHOICES = ['rock', 'paper', 'scissors']
WIN_MAP = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}  # what each choice beats

def get_user_choice():
    while True:
        u = input("Choose (rock/r, paper/p, scissors/s) or 'q' to quit: ").strip().lower()
        if u in ('q', 'quit', 'exit'):
            return 'q'
        if u in ('r', 'rock'):
            return 'rock'
        if u in ('p', 'paper'):
            return 'paper'
        if u in ('s', 'scissors', 'scissor'):
            return 'scissors'
        print("Invalid choice. Try again.")

def decide_winner(user, comp):
    if user == comp:
        return 'tie'
    elif WIN_MAP[user] == comp:
        return 'user'
    else:
        return 'computer'

def main():
    user_score = comp_score = ties = 0
    rounds = 0
    print("Welcome to Rock-Paper-Scissors! Type 'q' to quit.")
    while True:
        user = get_user_choice()
        if user == 'q':
            break
        comp = random.choice(CHOICES)
        print(f"Computer chose: {comp}")
        result = decide_winner(user, comp)
        rounds += 1
        if result == 'tie':
            print("It's a tie!")
            ties += 1
        elif result == 'user':
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            comp_score += 1
        print(f"Score -> You: {user_score}  Computer: {comp_score}  Ties: {ties}\n")

    print("Thanks for playing!")
    print(f"Final score after {rounds} rounds -> You: {user_score}  Computer: {comp_score}  Ties: {ties}")

if __name__ == "__main__":
    main()
