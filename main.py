import random #will help randomize the word

words = ['computer','python','rainbow','book','koala','pizza','water','condition','programming','random'] #words to choose from to guess


def newgame():
    #word = random.choice(words)
    word = "tree"
    print(word)

    char = ""
    numleft = 13
    dword = []
    for i in word:
         dword.append("_")
    while numleft > 0:
        print(dword)
        print("Characters you've used: ",char)
        guess = input("enter a character: ")
        print(iscorrect(guess,word))
        if iscorrect(guess,word):
            c = 0
            for i in word:
                if i == guess:
                    print(c, "here")
                    dword[c] = guess
                c+=1
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




