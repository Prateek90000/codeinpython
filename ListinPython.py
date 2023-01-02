import numpy as np

listofnumbers = list(range(10))
print("listofNumbers", listofnumbers)

# problem 2 list of alternate numbers
# listofnumbers = list(range(start number1,end number10,gap2))
listofnumbers = list(range(1, 10, 2))
print("listofNumbers", listofnumbers)
# list in reverse
# listofnumbers = list(range(10,1,-2)) minus takes the list in reverse
listofnumbers = list(range(1, 100, 1))
print("listofNumbers", listofnumbers)

# can we iterate through the list and print if it's the multiple of 3?
listofmultiplesof3 = []
for num in listofnumbers:
    if num % 3 == 0:
        print(num)

listofmultiplesof3 = list(range(3, 100, 3))
listofmultiplesof5 = list(range(5, 100, 5))
print("listofmultiplesof3=", listofmultiplesof3, "listofmultiplesof5=", listofmultiplesof5)
listofmultiplesof3and5 = []
for num in listofmultiplesof3:
    if num in listofmultiplesof5:
        listofmultiplesof3and5.append(num)
print("listofmultiplesof3and5=", listofmultiplesof3and5)

#  merge two lists
listofmultiplesof3or5 = listofmultiplesof3 + listofmultiplesof5
sortedlistofmultiplesof3or5 = sorted(listofmultiplesof3or5)
print("sortedlistofmultiplesof3or5=", sortedlistofmultiplesof3or5)

# remove duplicates from the merge list
deduplicatedlist = []
for numIndex in range(1, len(sortedlistofmultiplesof3or5), 1):
    num = sortedlistofmultiplesof3or5[numIndex - 1]
    next_num = sortedlistofmultiplesof3or5[numIndex]
    if num != next_num:
        deduplicatedlist.append(num)
print("deduplicatedlist=", deduplicatedlist)

listofwords = ["rahul", "prateek", "tushti", "rohit", "meenakshi"]
print("prateek" in listofwords)

# take user inputs and print them
name =input("What is your name?")
print("Hi, %s, Welcome to our game!"%name)

#  stone,paper,scissors
hasError = True
while(hasError):
    try:
        numgames = input("How many games you want to play?")
        numgames = int(numgames)
        if(numgames>1 and numgames<100):
            hasError = False
        else:
            print(" you have made an error, please retry")
    except:
        print(" you have made an error, please retry")
        hasError = True
print("Thanks %s, we will play %d games!"%(name,numgames))
listofchoices = ["Rock", "Paper", "Scissors"]
np.random.seed(7)
def PlayGame(listofchoices):
    computerchoicenumber = np.random.randint(0,3)
    computerchoice = listofchoices[computerchoicenumber]
    print("computerchoice=", computerchoice)

    hasError = True
    while(hasError):
        try:
            yourchoice = input("what is your choice,please choose between Rock,Paper,Scissor?")
            if(yourchoice in listofchoices):
                hasError = False
            else:
                print(" you have made an error, please retry")
        except:
            print(" you have made an error, please retry")
            hasError = True
    print("humanchoice", yourchoice)
    if(yourchoice=="Rock" and computerchoice=="Rock") or (yourchoice=="Paper" and computerchoice=="Paper") or (yourchoice=="Scissor" and computerchoice=="Scissor"):
        return 0
    if(yourchoice=="Rock" and computerchoice=="Scissor") or (yourchoice=="Paper" and computerchoice=="Rock") or (yourchoice=="Rock" and computerchoice=="Scissor"):
        return 1
    if(yourchoice=="Paper" and computerchoice=="Scissor") or (yourchoice=="Rock" and computerchoice=="Paper") or (yourchoice=="Scissor" and computerchoice=="Rock"):
        return -1
    return 0
numGamesWon = 0
for gamenumber in range(numgames):
    numGamesWon = numGamesWon+PlayGame(listofchoices)

if (numGamesWon>0):
    print("you are lucky, you won !")
elif (numGamesWon<0):
    print("So sorry, you lost")
else:
    print("the game is draw")
