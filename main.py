import random  # Used to select a random word
import os  # Used to clear the terminal

# List of words to choose from for the game
words = ['computer', 'python', 'rainbow', 'book', 'koala', 'pizza', 'water', 'condition', 'programming', 'random']

# Function to start a new game
def newgame():
    word = random.choice(words)  # Selects a random word
    charused = ""  # Tracks characters used so far
    numleft = level("placeholder")  # Sets the number of tries based on difficulty level
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal
    dword = ["_"] * len(word)  # Creates a display list with underscores for each letter in the word
    win = False  # Tracks if the player has won

    # Main game loop
    while numleft > 0 and not win:
        print("You have %s number of tries left!" % numleft)  # Shows remaining tries
        print(dword)  # Displays the current guessed letters and blanks
        print("Characters you've used: ", charused)  # Shows used characters
        guess = input("Enter a character: ")  # Asks for a guess

        # Ensures only a single character is entered
        while len(guess) > 1:
            print("Please enter one letter")
            guess = input("Enter a character: ")

        # Ensures the character hasn't been guessed before
        while guess in charused:
            print("You've already guessed this letter")
            guess = input("Enter a character: ")

        print(iscorrect(guess, word))  # Tells the player if the guess was correct or not

        # If the guess is correct, it updates the display list
        if iscorrect(guess, word) == "Correct":
            for index, letter in enumerate(word):
                if letter == guess:
                    dword[index] = guess  # Replaces underscore with the correct letter

        # Check if all letters have been guessed
        if "_" not in dword:
            win = True  # Player wins if no underscores are left

        charused += guess  # Adds the guess to used characters
        numleft -= 1  # Decreases the number of tries

        input("Press enter to continue")  # Waits for player input to continue
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal

    # Final message based on win or lose
    if win:
        print("You Won!")
    else:
        print("You've used up all your guesses\nThe word was %s\nPlay Again!" % word)

# Function to check if the guessed character is in the word
def iscorrect(guess, word):
    for letter in word:
        if letter == guess:
            return "Correct"
    return "Wrong"

# Function to set the difficulty level
def level(choice):
    while True:
        if choice.lower() == "easy":
            return 10  # Easy level gives 10 tries
        elif choice.lower() == "med":
            return 5  # Medium level gives 5 tries
        elif choice.lower() == "hard":
            return 3  # Hard level gives 3 tries
        else:
            choice = input("Please choose a difficulty from: easy, med, hard: ")  # Asks for a valid difficulty

# Main loop to keep playing or quit
contplaying = True
while contplaying:
    userinput = input("q to quit, any other key to play: ")  # Prompts the user to play or quit
    if userinput.lower() == "q":
        print("Thanks For Playing")
        contplaying = False  # Ends the game if the user wants to quit
    else:
        newgame()  # Starts a new game if the user wants to play
