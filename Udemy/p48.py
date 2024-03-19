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

user_hand_print = ""
com_hand_print =  ""

random_hand = random.randint(0,2)

if random_hand == 0:
  com_hand_print = rock
elif random_hand == 1:
  com_hand_print = paper
elif random_hand == 2:
  com_hand_print = scissors

  

user_hand = int(input("Enter 0 = Rock, 1 = paper and 2 = scissors:"))

if user_hand == 0:
  user_hand_print = rock
elif user_hand == 1:
  user_hand_print = paper
elif user_hand == 2:
  user_hand_print = scissors
else:
  print("Invalid input")
  break

print("Computer chose:", com_hand_print)
print("user chose:", user_hand_print)

if user_hand == 0 and random_hand == 1:
  print("Computer wins")
elif user_hand == 1 and random_hand == 2:
  print("Computer wins")
elif user_hand == random_hand:
  print("Draw")
else:
  print("User wins")