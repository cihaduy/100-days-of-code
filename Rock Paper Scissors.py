import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = input("Rock, Paper or Scissors?\n")

if user_input == 'rock':
    print(rock,"\nYou chose Rock!")
elif user_input == 'paper':
    print(paper,"\nYou chose Paper!")
elif user_input == 'scissors':
    print(scissors,"\nYou chose Scissors!")

computer_input = random.randrange(1, 3)

if computer_input == 1:
    computer_input = "Rock"
    print(rock,"\nComputer chose Rock!")
elif computer_input == 2:
    computer_input = "Paper"
    print(paper, "\nComputer chose Paper!")
elif computer_input == 3:
    computer_input = "Scissors"
    print(scissors,"\nComputer chose Scissors!")

while user_input == "rock":
    if computer_input == "Rock":
        print("\nDraw!")
        break
    elif computer_input == "Paper":
        print("\nYou Lost!")
        break
    elif computer_input == "Scissors":
        print("\nYou Won!")
        break

while user_input == "paper":
    if computer_input == "Rock":
        print("\nYou Won!")
        break
    elif computer_input == "Paper":
        print("\nDraw!")
        break
    elif computer_input == "Scissors":
        print("\nYou Lost!")
        break

while user_input == "scissors":
    if computer_input == "Rock":
        print("\nYou Lost!")
        break
    elif computer_input == "Paper":
        print("\nYou Won!")
        break
    elif computer_input == "Scissors":
        print("\nDraw")
        break

