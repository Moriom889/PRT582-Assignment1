
#Requirement Three
selection_list = ("Scissors","Rock", "Paper")

def winner_each_round(user_action, com_action):
    
    if user_action.lower() == com_action.lower():
        print(f"Both players selected {user_action}. It's a tie!")
        return 0
    elif user_action.lower() == "rock":
        if com_action.lower() == "scissors":
            print("Rock smashes Scissors. You win!")
            return 1
        else:
            print("Player lose.")
            return 2
    elif user_action.lower() == "paper":
        if com_action.lower() == "rock":
            print("Paper wraps Rock. You win!")
            return 1
        else:
            print("Player lose.")
            return 2
    elif user_action.lower() == "scissors":
        if com_action.lower() == "paper":
            print("Scissors cuts paper! You win!")
            return 1
        else:
            print("Player lose.")
            return 2
    else:
        print("You entered the wrong input")






