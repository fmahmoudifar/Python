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

gane_images = [rock, paper, scissors]

com_hand = random.randint(0, 2)

user_hand = int(input("Enter 0 = Rock, 1 = paper and 2 = scissors:"))

if user_hand >= 3:
  print("You hav etyped an invalid number, you lose!")
else:
  print("You chose: ")
  
  print(gane_images[user_hand])
  
  print("Computer chose: ")
  print(gane_images[com_hand])
  
  if user_hand == 0 and com_hand == 1:
    print("You lose")
  elif user_hand == 1 and com_hand == 2:
    print("You Lose")
  elif user_hand == com_hand:
    print("It is a Draw")
  else:
    print("You win!")
