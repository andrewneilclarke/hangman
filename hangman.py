import random
import time
import json

word = ''
original_word = ''
length = len(word)
count = 0
limit = 5
display = '_' * length
already_guessed = []
game_still_going = True
#play_game = ""
lose = False
name = ''

# welcome user
def welcome_user(): 
    global name
    global game_still_going
    game_still_going = True
    print('Welcome to Hangman! \n')
    time.sleep(0.5)
    name = input("What is your name? ")
    time.sleep(0.5)
    print("\nWelcome to the game, " + name + "!\n")
    time.sleep(1)

def choose_word():
    global display
    global word
    global original_word
    global length
    wordlist = 'words_list.json'
    with open(wordlist) as f:
      wordlistdata = json.load(f)
    for v in wordlistdata.values():
      word = random.choice(v)
      original_word = word
    length = len(word)
    display = '_' * length
    return length, word, original_word

#def find_all(word, guess):
#    return [i for i, letter in enumerate(word) if letter == guess]

def display_board():
  global display
  print(display)

def you_win():
  print("YOU WIN! The word was: " + original_word + "! Well done, " + name.title() + "!")

def handle_turn():
  global word
  global display
  global count
  global limit
  guess = input('Enter a letter..')
  guess = guess.strip()
  if len(guess) != 1 or guess.isalpha() == False:
    print("Invalid Input, Try again\n")
  elif guess in word:
    print('correct!')
    already_guessed.append(guess)
    index = word.find(guess)
    #word.find(guess)
    word = word[:index] + "_" + word[index + 1:]
    display = display[:index] + guess + display[index + 1:]

  elif guess in already_guessed:
    if guess not in word:
      print("Already guessed! Try another letter.\n")

  else:
    print('wrong!')
    count += 1
    hangman()

def hangman():
    global count
    global lose
    if count == 1:
        time.sleep(1)
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 2:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 3:
       time.sleep(1)
       print("   _____ \n"
             "  |     | \n"
             "  |     |\n"
             "  |     | \n"
             "  |      \n"
             "  |      \n"
             "  |      \n"
             "__|__\n")
       print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 4:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

    elif count == 5:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
        print("Wrong guess. You are hanged!!!\n")
        print("The word was:" + original_word + "!")
        lose = True
        game_still_going = False


    elif word == '_' * length:
        you_win()


def play_game():
    display_board()
    handle_turn()

def main():
    choose_word()
    print(word)
    print('Can you guess the word?')
    while game_still_going:
      play_game()
      if original_word == display:
          game_still_going == False
          you_win()
          if input("Continue? (y/n)").strip().upper() != 'Y':
              break
          else:
              main()
      elif lose == True:
          if input("Continue? (y/n)").strip().upper() != 'Y':
              break
          else:
              main()
welcome_user()
main()
