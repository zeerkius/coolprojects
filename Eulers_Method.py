#Basil Agboola
#To Nick Zoller
#Cal 2 Lab 2

def equ(equation,step,icondition,n):
    x = 0
    h = icondition
    z = step
    if equation[1] == "X":
        for i in range(n -1):
            x = h + (float(equation[0])*step) * z
            h = x
            step += z
        print(x)
#this function does the Eulers method
# equations is the string that the user gives
# it first looks at the string and return the equation[0],part of it
#this means the only part with a number so, and since this code only takes function 4X,5X,... it works
# then it will do n - 1 iterations because it will do one more iteration after the first calculation of the tangent line
#h will be the constant from the tangent line , it will be a constant because it only takes 4X,5X and all other infinite equation of the form
# then h will equal x in the next iteration as the mehod builds on the former reult
# then will multiply the first number ie. the 4,5,6.. by the step  then multiply the general unchnaging step
#the step will increment each iteration with each iteration, ie in 4X example 0.1,0.2..

c = int(input("What is your right endpoint"))
## this is the rightendpoint
a = int(input("What is your left endpoint "))
## this is the left endpoint
h = float(input("What is your step size "))
## the stepsize within each iteration
f = float(input("Inital condition , y(0) = ? "))
#this is the initial condition
#this specidic code can only solve equations like 4X,5X,6X...
if c <= a:
    print("Invalid input - Upper value is greater ")
if (c or a) < 0:
    print("Invalid input - Negative Value " )
    quit()
#This portion negates any errors / invalid inputs that would cause a mistake in a calculating iterations
n = int((c - a)/h)
# number of iterations
print("This approximation will have " + str(n) + " Iterations  \n ")
#explaining to user how many iterations there will be
print("Input your diffrential equation in this format without space , X will corespond to the variable")
print("Outputs will look like this \n ")
print("Integer X, withoutspace ex. 4X")
diffeq = str(input("Input different + Do not hit the space button and then type your input"))
#equation will be in for 5X,6X,...
equ(diffeq,h,f,n)
## calls function


