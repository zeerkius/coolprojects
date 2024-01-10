#Basil-Agboola Guessing-Game
#CSNE-2923
#Professor Robert Gering


from time import sleep #used through out code
import math # used for binary application
import random # used for random application

#importing this so I can display output with better style

print("LOADING") ; sleep(0.1)
print(" .") ; sleep(0.1)
print(" .") ; sleep(0.1)
print(" .") ; sleep(0.1)

print(" We are going to display a guessing game You will input a number then I the computer will try and guess it.")
print( " If the number I guess is to high input 'H' if the number is too low input 'L'  if the number is correct input 'Y'.")

#Input from user in linear search

Randomnumber = int(input(" Input a random number from 1 - 1000"))

#Variable for guesses

guess = 1

#Linear Search Application

# Python Boolean to control loops

LoopBoolean = True

# counting number of tires of guesses for variables

count = 1
while LoopBoolean:
    response = input(str("Is your number  " + str(guess)))
    if response == "Y":
        print("We guessed the number corretly!")
        print(" We guessed " + str(count) + "times")
        LoopBoolean = False
    if response == "L":
             guess += 1
             count += 1
    if response == "H":
             guess -= 1
             count += 1




#Binary Search Application

# make the user choose a diffent number

print("choose a new number"); sleep(5.0)

# prompting the user

print("Now we will use a binary solution")

#LoopBoolean so we can loop till we find an output

LoopBooleanBinary = True

# first guess variable

guessoutput = 500


# Count for binary search

guesscounter = 1

# range variable - its purpose is to further narrow down the number so we can find it

guessrange = 500

while LoopBooleanBinary:
    guessrange = guessrange / 2
    response = input(str("Is your number  " + str(guessoutput)))
    if response == "Y":
        print("We guessed the number corretly!")
        print(" We guessed " + str(guesscounter) + " times")
        LoopBooleanBinary = False
    if response == "H":
        guessoutput -= math.ceil(guessrange)
        guesscounter += 1
    if response == "L":
        guessoutput  += math.ceil(guessrange)
        guesscounter += 1


# Random Application
#prompting the user
print("Now we are going to use a random application") 

print("choose a new number"); sleep(5.0)



# too keep track of guesses

Randomguesscounter = 0
       
# Random Loop Boolean

LoopBooleanRandom = True

#RandomGuesscount

randomcount = 1



#LoopBoolean Random Low and High

LoopRandomLow = True
LoopRandomHigh = True

# Random Guess to start

guessRandom = 500

#


GuessRandomLow = 0
GuessRandomHigh = 0


while LoopBooleanRandom:
    # randint is inclusive
    response = input(str(" Is your number " + str(guessRandom)))
    if response == "Y":
        print("We guessed the number corretly!")
        print(" We guessed " + str(randomcount) + " times")
        LoopBooleanRandom = False
    if response == "L":
        while LoopRandomLow:
            GuessRandomLow = random.randint(1,1000)
            if GuessRandomLow > guessRandom:
                guessRandom = GuessRandomLow
                break
        randomcount += 1
    if response == "H":
        while LoopRandomHigh:
            GuessRandomHigh = random.randint(1,1000)
            if GuessRandomHigh < guessRandom:
                guessRandom = GuessRandomHigh
                break
        randomcount += 1
        

    



