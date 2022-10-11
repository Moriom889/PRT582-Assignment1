
import random
def main():
    user_win=0
    comp_win=0
    while True:
        user_action = input("Enter a choice (rock, paper, scissors): ")
        option_list = ["Rock", "Paper", "Scissors"]
        com_action = random.choice(option_list)
        print(f"\nYou chose {user_action}, computer chose {com_action}.\n")

        if user_action.lower() == com_action.lower():
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action.lower() == "rock":
            if com_action.lower() == "scissors":
                user_win=user_win + 1
                print("Rock smashes Scissors. You win!")
            else:
                comp_win = comp_win + 1
                print(" You lose.")
        elif user_action.lower() == "paper":
            if com_action.lower() == "rock":
                user_win=user_win + 1
                print("Paper wraps Rock. You win!")
            else:
                comp_win = comp_win + 1
                print(" You lose.")
        elif user_action.lower() == "scissors":
            if com_action.lower() == "paper":
                user_win=user_win + 1
                print("Scissors cuts paper! You win!")
            else:
                comp_win = comp_win + 1
                print("You lose.")
        else:
            print("Your input is wrong")
        if user_win >= 5 or comp_win >=5:  
           if comp_win < user_win:
                    print("Player won this game")
           else:
                    print("Computer won this game")  
           print("Final Scores:")
           print(f"Player:{user_win}")
           print(f"Comp:{comp_win}")  
           play_again = input("Play again? (yes/no): ")
           if play_again.lower() != "yes":
            break
 

if __name__=="__main__":
    main()