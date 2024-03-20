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

print("user chose: ")
print(gane_images[user_hand])

print("Computer chose: ")
print(gane_images[com_hand])

if user_hand == 0 and com_hand == 1:
  print("Computer wins")
elif user_hand == 1 and com_hand == 2:
  print("Computer wins")
elif user_hand == com_hand:
  print("Draw")
else:
  print("User wins")
