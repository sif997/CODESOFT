import random

def compare_choices(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "tie"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "user wins"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "user wins"
  elif user_choice == "paper" and computer_choice == "rock":
    return "user wins"
  else:
    return "computer wins"


def main():
  
  user_choice = input("Enter your choice (rock, paper, or scissors): ")

  
  computer_choice = random.choice(["rock", "paper", "scissors"])

  result = compare_choices(user_choice, computer_choice)

  
  print(f"You chose {user_choice} and the computer chose {computer_choice}.")
  print(result)

  
  again = input("Do you want to play another round? (y/n): ")

  if again.lower() == "y":
    main()


if __name__ == "__main__":
  main()
