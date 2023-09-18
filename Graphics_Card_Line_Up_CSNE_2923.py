# Basil Agboola
# Prof Gering
# CSNE-2923-01
'''
Project Description: You are going to build ticketing software for a major graphics card manufacturer. People want their graphics cards (think about this like the most important internal part of a PlayStation), and there's no supply, because greedy studious AI researchers have bought nearly all the available cards from manufacturers! So each person must wait in a digital line for their chance to buy a card.

Requirements:
You have a limited supply of graphics cards. You may represent this internally as a stack, or a linked list.
You must be able to add to the graphics card supply on demand when new shipments arrive.
People can wait in line. The line has zero people to begin with.
No more than 100 people can wait in line. After 100 people are waiting in line, the line should report that it is full.
Management has decided that in order to make the waiting process more fun, we must add "gamification".
Thus, the person at the head of the line has a 50% chance of success of getting the next card
And there must also be a 50% chance that the card is given to someone else in line (randomly distributed).
Your program must be started from the command-line (No Colab submissions).
Extra information:

You can figure out things on your own by looking them up! This is half the job of a typical software engineering role.
For example, for this assignment, you will need to know several details:
How to run Python code from the command line
How to print text to the command line
How to get user input from the command line
Each of the above items is a simple search away
Divide and conquer: break things down into small steps that you can solve!

'''
# Graphics Card LineUp
# Video link which helped me create Linked lista and functions #https://youtu.be/JlMyYuY1aXU?si=_g26_pc0OswAT6F7


# Creating Linked list to represent finite number of Graphics Cards
import pprint # to output objects
import random # to pick random person who gets %50% chance 
import sys #  so that we can exit the code when necessary
import operator # so we can iterate over items in dictionary

class GraphicsCard:
    def __init__(self, data=None):
        self.data = data # past data point
        self.next = None # pointer to next data point

class DisplayObject:
    def __str__(self):
        return self
    def __repl__(self):
        return


class GraphicsCardData:
        def __init__(self):
            self.head = GraphicsCard() #constructing head Graphics Card

        def Shipment(self,data): 
            # to apppend we must make  a refernece variable that is a "new node" then traverse the linked list then finally 
            new_GraphicsCard = GraphicsCard(data)
            currentcard = self.head
            while currentcard.next != None:
                currentcard = currentcard.next
            currentcard.next = new_GraphicsCard
        
        def supply(self):
           # to find how many graphics cards are currently in house
            currentcard = self.head
            stock = 0
            while currentcard.next != None: 
                # traverse and then tally up number of graphics cards
                stock += 1
                currentcard = currentcard.next
            return stock
        def show(self):
            # we use array so we can dispay stock of graphic cards
            cards = [] 
            currentstock = self.head
            while currentstock.next != None: 
                # we then traverse through each card and then append data for the card to the array
                currentstock = currentstock.next
                cards.append(currentstock)
            #print(cards)
        def ReturnPerson(self,index): # how to return ceartin index within our list that represents a person in line
            if index >= self.length():
                print(" You are not in line")
                return None
            lineorder = 0
            linenumber = self.head
            while True:
                linenumber = linenumber.next
                if lineorder == index: return linenumber.data
                lineorder += 1
        def leaveline(self,index):  # how to delete graphics card after someone receives it
            if index >= self.supply():
                print(" Invalid")
            lineorder = 0
            linenumber = self.head
            while True:
                lastinline = linenumber
                linenumber = linenumber.next
                if lineorder == index:
                    lastinline.next = linenumber.next
                    return
                lineorder += 1

# Using the Data Structure in our Application

Playstation = GraphicsCardData()  # creating instance of the linked list to represent Graphic Cards


supplies = int(input(" How many Graphic Cards are coming in shipment today  "))

for i in range(supplies):
    count = 1
    Playstation.Shipment(count) # representing graphics cards with linked list
    count += 1

# this is where we create a  dictionary to represnt the amount of people in line when the Playstation opens , lets say Playsation opens at 9:00 AM

PeopleInLine = int(input(" How many people are in line at 9:00 AM  "))
print( "There are " + str(PeopleInLine) + " In line !")
# this is where we handle the amount of people in Line
if (PeopleInLine > 100):
    print("There are too manny people in Line!")
    sys.exit()

LuckyPerson = random.randint(1,PeopleInLine)
# person to Luck  dictionary

PersontoLuck = {}
# creating count variable so we can create dictionary
count = 1
for i in range(PeopleInLine):
    PersontoLuck.update({count:(50 / count)})
    count += 1
#part of the code that alots the amount of lucky person to get ticket
for key in PersontoLuck.keys():
    value = PersontoLuck[key]
    if LuckyPerson == key:
        PersontoLuck.update({key:50.0})
pprint.pprint(PersontoLuck) # displaying order of luck/who gets grpahics card

# distributing based on luck

for j in range(supplies):
    for key in PersontoLuck.keys():
        value = PersontoLuck[key]
        Luckiest = max(PersontoLuck.items(),key=operator.itemgetter(1))[0]
        PersontoLuck.update({Luckiest: -1}) # this way the dictionary length doesent change so we can continue to iterate it
        print("$$ We made a transaction! $$")
        Playstation.leaveline(Luckiest) # this way the person gets the specific graphics card for them
        pprint.pprint(PersontoLuck)



# It seems to work until we get around our 40th transaction