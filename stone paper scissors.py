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

your_choice=int(input("What do you choose? Type 0 for rock,1 for Paper or 2 for Sissor\n"))

if your_choice >=2:
    print("Oop's invalid number\n")

else:
    if your_choice == 0:
        print(rock)
    elif your_choice == 1:
        print(paper)
    elif your_choice == 2:
        print(scissors)

    print("Computer's choice")

    choice = random.randint(0, 2)
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)

    if (your_choice == 0 and choice == 1) or (your_choice == 1 and choice == 2) or (your_choice == 2 and choice == 0):
        print("You lose")
    elif choice == your_choice:
        print("it's Draw")
    elif (your_choice == 1 and choice == 0) or (your_choice == 2 and choice == 1) or (your_choice == 0 and choice == 2):
        print("you win")
