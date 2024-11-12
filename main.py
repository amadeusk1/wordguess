import random #will help randomize the word
import os #will be used to clear the terminal
#note that the single character variables are very vital for the code but do not have a word to define them

words = ['computer','python','rainbow','book','koala','pizza','water','condition','programming','random'] #words to choose from to guess


def newgame():
    word = random.choice(words)
    charused = ""
    numleft = level("placeholder")
    os.system('cls' if os.name == 'nt' else 'clear')
    dword = []
    win = False
    for i in word:
         dword.append("_")
    while numleft > 0 and win == False:
        print("You have %s number of tries left!" %numleft)
        print(dword)
        print("Characters you've used: ",charused)
        guess = input("enter a character: ")
        while len(guess) > 1:
             print("Please enter one letter")
             guess = input("enter a character: ")
        while guess in charused:
             print("You've already guessed this letter")
             guess = input("enter a character: ")
        print(iscorrect(guess,word))
        if iscorrect(guess,word):
            c = 0
            for i in word:
                if i == guess:
                    #print(c, "here")
                    dword[c] = guess
                c+=1
        l = 0
        for i in dword:
             if i in word:
                  l += 1
        if l >= len(word):
             win = True
        charused += guess
        numleft -= 1
        input("Press enter to continue")
        os.system('cls' if os.name == 'nt' else 'clear') #clears terminal
    if win == True:
         print("You Won!")
    else:
        print("You've used up all your guesses\nThe word was %s\nPlay Again!" %word)

def iscorrect(guess,word):
        for i in word:
            if i == guess:
                return "Correct"     
        return "Wrong"

def level(choice):
     i = 0
     while i == 0:
        if choice.lower() == "easy":
            return 10
        elif choice.lower() == "med":
            return 5
        elif choice.lower() == "hard":
            return 3
        else:
            choice = input("Please choose a difficulty from: easy, med, hard: ")
          
    

contplaying = True
while contplaying:
    userinput = input("q to quit, any other key to play: ")
    if userinput == "q" or userinput == "Q":
        print("Thanks For Playing")
        contplaying = False
    else:
         newgame()




