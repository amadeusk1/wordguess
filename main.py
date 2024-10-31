import random #will help randomize the word

words = ['computer','python','rainbow','book','koala','pizza','water','condition','programming','random'] #words to choose from to guess


def newgame():
    word = random.choice(words)
    print(word)

    char = ""
    numleft = 13
    while numleft > 0:
        print("Characters you've used: ",char)
        guess = input("enter a character: ")
        print(iscorrect(guess,word))
        char += guess
        numleft -= 1
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
        contplaying = False
    else:
         newgame()




