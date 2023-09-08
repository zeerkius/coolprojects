import turtle
import math
#this part below is what returns the binary value of your decimal form age
def binaryconv(x):
    global binary
    binary = ""
    if x == 1:
        binary = "0000001"
    if x == 0:
        binary = "0000000"
    for i in range(7):
          if x % 2 == 0:
            binary = binary + "0"
          if x % 2 == 1:
            binary = binary + "1"
          x = math.floor(x/2)
    print(binary[::-1])
#        
#this part below is what limits the age        
    
age = int(input("Input your age!"))
binaryconv(age)
if age > 122:
    print("invalid age - must be less than or equal to 122")
    quit()
if age < 0:
    print("invalid age - must be greater or equal than 0")
    quit()

#cake
birthdaycake = turtle.Turtle()
birthdaycake.color("#4E3524")
birthdaycake.begin_fill()
for i in range(4):
    birthdaycake.forward(200)
    birthdaycake.right(90)
birthdaycake.end_fill()
birthdaycake.right(270)
#candles
#red means 0
#green means 1
for i in range(6,-1,-1):
    if binary[i] == "0":
        birthdaycake.color("red")
    else:
        birthdaycake.color("green")
    birthdaycake.begin_fill()
    birthdaycake.forward(50)
    birthdaycake.right(90)
    birthdaycake.forward(26)
    birthdaycake.right(90)
    birthdaycake.forward(50)
    birthdaycake.left(90)
    birthdaycake.forward(2)
    birthdaycake.left(90)
    birthdaycake.end_fill()
   

    
