import random
import time

word = ''
original_word = ''
length = len(word)
count = 0
limit = 5
display = '_' * length
already_guessed = []
game_still_going = True
lose = False
win = False
name = ''
guess = ''

# welcome user
def welcome_user(): 
    global name
    global game_still_going
    game_still_going = True
    print('Welcome to Hangman! \n')
    time.sleep(0.4)
    name = input("What is your name? ")
    print("\nWelcome to the game, " + name + "!\n")
    time.sleep(0.4)

def choose_word():
    global display
    global word
    global original_word
    global length
    wordlist = 'wordlist.txt'
    
    #word = (random.choice(open('wordlist.txt').readline().split()))
    with open(wordlist) as f:
        wordlistdata = f.readlines()
    for w in wordlistdata:
        word = random.choice(w)

    original_word = word
    length = len(word)
    display = '_' * length
    return length, word, original_word

#def find_all(word, guess):
#    return [i for i, letter in enumerate(word) if letter == guess]

def display_board():
    global display
    print(display)

def check_win():
    if word == '_' * length:
        print("YOU WIN! The word was: " + original_word + "! Well done, " + name.title() + "!")
        win = True
        game_still_going = False

def handle_turn():
    global word
    global display
    global count
    global limit
    display_board()
    guess = input('Enter a letter..')
    guess = guess.strip()
    if len(guess) != 1 or guess.isalpha() == False:
        print("Invalid Input, Try again\n")

def check_correct():
    global guess
    global word
    global display
    if guess in word:
        print('correct!')
        while guess in word:
            already_guessed.append(guess)
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]

def check_incorrect():
    if guess in already_guessed:
        print("Already guessed! Try another letter.\n")
    else:
        print('WRONG!')
        count += 1
        hangman()

def hangman():
    global count
    global lose
    if count == 1:
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("WRONG guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 2:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("WRONG guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 3:
        print("   _____ \n"
             "  |     | \n"
             "  |     |\n"
             "  |     | \n"
             "  |      \n"
             "  |      \n"
             "  |      \n"
             "__|__\n")
        print("WRONG guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 4:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("WRONG guess. " + str(limit - count) + " last guess remaining!\n")

    elif count == 5:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
        print("WRONG guess. You are hanged!!!\nThe word was:" + original_word + "!")
        lose = True
        game_still_going = False


def play_game():
    global lose
    already_guessed.clear()
    lose == False
    win == False
    choose_word()
    print(word)
    print('Can you guess the word?')
    while game_still_going:
        display_board()
        handle_turn()
        check_correct()
        check_incorrect()
        check_win()

#loop main program
welcome_user()
while game_still_going:
    play_game()
    if lose or win == True:
        break
    if input("Play again?! (y/n)").strip().upper() != 'Y':
        break

