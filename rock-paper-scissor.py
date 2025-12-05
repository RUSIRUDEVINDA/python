import random

# Valid game options
options = ["rock", "paper", "scissors"]

def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(options)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "win"
    else:
        return "lose"

def play_round():
    player = get_player_choice()
    computer = get_computer_choice()
    
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    
    result = determine_winner(player, computer)
    
    if result == "win":
        print("You win this round!\n")
    elif result == "lose":
        print("You lose this round!\n")
    else:
        print("It's a tie!\n")
    
    return result

def play_game():
    wins = 0
    losses = 0
    ties = 0
    
    print("Welcome to Rock-Paper-Scissors!\n")
    
    while True:
        result = play_round()
        
        if result == "win":
            wins += 1
        elif result == "lose":
            losses += 1
        else:
            ties += 1
        
        again = input("Play again? (y/n): ").lower()
        while again not in ["y", "n"]:
            again = input("Invalid input! Please enter 'y' to continue or 'n' to stop: ").lower()
        
        if again == "n":
            break
    
    print("\n--- Final Score ---")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
