import random

from Udemy.p7sub import logo, stages, word_list

print(logo)

chosen_word = random.choice(word_list)

word_len = len(chosen_word)
display = []
for x in range(word_len):
  display += "_"

#print(display)
print(f"{' '.join(display)}")

end_of_game = False

lives = 6
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    print(stages[lives])
    if lives == 0:
      end_of_game = True
      print("You lose.")
      print(f"The word was {chosen_word}")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")
