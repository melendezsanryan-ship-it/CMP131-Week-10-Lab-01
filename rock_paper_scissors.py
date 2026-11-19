
import random


def main():
  while True:
    pc_result = pc_choice()
    user_result = user_choice()
    win = winner(pc_result, user_result)
    display(win, pc_result, user_result)


def pc_choice():
  choice = random.randint(1, 3)
  if choice == 1:
    return "rock"
  elif choice == 2:
    return "paper"
  else:
    return "scissors"


def user_choice():
  while True:
    try:
      choice = int(input("Press 1 for rock, 2 for paper, 3 for scissors: "))
      if choice == 1:
        return "rock"
      elif choice == 2:
        return "paper"
      elif choice == 3:
        return "scissors"
      else:
        print("Please enter 1, 2, or 3.")
    except ValueError:
      print("Invalid input. Please enter a number (1, 2, or 3).")


def winner(pc_result, user_result):
  if pc_result == user_result:
    return "tie"
  elif (
      (user_result == "rock" and pc_result == "scissors")
      or (user_result == "paper" and pc_result == "rock")
      or (user_result == "scissors" and pc_result == "paper")
  ):
    return "user"
  else:
    return "pc"


def display(win, pc_result, user_result):
  print("\nYou chose:", user_result)
  print("PC chose:", pc_result)
  print("Winner:", win, "\n")


main()

