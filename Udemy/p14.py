from p14data import data
import random

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_follower, b_follower):
  if a_follower > b_follower:
    return user_guess == 'a'
  else:
    return user_guess == 'b'

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data) 
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print("VS")
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
      score += 1
      print(f"You are right! Current Score: {score}")
    else:
      print(f"Sorry, that's wrong. Final Score: {score}")
      game_should_continue = False