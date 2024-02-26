import random
TRIES = 6
def get_word(file_name: str)->str:
    file_handle = open(file_name, 'r')
    lo_words = []
    for line in file_handle:
        line = line.strip()
        lo_words.append(line)
    word = random.choice(lo_words)
    file_handle.close()
    return word.upper()


def play(word: str): 
    word = word
    blanks = "_" * len(word)+"("+str(len(word))+")"
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = TRIES
   
    print("Let's play!")
    print(blanks)
    print()
    
    while not guessed and tries > 0:
        print("Tries left: " + str(tries))
        print("Letters guessed: " + str(guessed_letters))
        print("Words guessed: " + str(guessed_words))
        guess = input("Guess a letter or word: ").upper()
        print()
        
        if len(guess) == 1 and guess.isalpha(): 
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "is in the word!")
                guessed_letters.append(guess)
                lo_blanks = list(blanks) 
                for index in range(0, len(word)):
                    if word[index] == guess:
                        lo_blanks[index] = guess
                blanks = ""
                for letter in lo_blanks:
                    blanks+=letter 
                    
                if "_" not in blanks:
                    guessed = True
                    
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Your already guessed", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed = True
                blanks = word
            
        else:
            print("Not a valid guess")
            
        print(blanks)
        print()
        
    if guessed:
        print("Good job, you guessed the word!")
    else:
        print("Sorry, you're out of tries. The word was " + word + ", better \
luck next time!")

def game():
    word = get_word("words.txt")
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word("words.txt")
        play(word)
        
    print("Thanks for playing:)")