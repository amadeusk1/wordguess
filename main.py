import random #will help randomize the word
import os #will be used to clear the terminal

words = ['computer','python','rainbow','book','koala','pizza','water','condition','programming','random'] #words to choose from to guess


def newgame():
    #word = random.choice(words)
    word = "tree"
    print(word)

    charused = ""
    numleft = 13
    dword = []
    for i in word:
         dword.append("_")
    while numleft > 0:
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
        charused += guess
        numleft -= 1
        #os.system('cls' if os.name == 'nt' else 'clear')
    print("You've used up all your guesses")

def iscorrect(guess,word):
        for i in word:
            if i == guess:
                return "Correct"     
        return "Wrong"


contplaying = True
while contplaying:
    userinput = input("q to quit, any other key to play: ")
    if userinput == "q" or userinput == "Q":
        print("Thanks For Playing")
        contplaying = False
    else:
         newgame()




