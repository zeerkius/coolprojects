#function
#this function will filter through parameter "x" that is a string and will then change everywhere inside the string  "A"
#into "f$"
def strfilter(x):
    for i in range(len(x)):
        if x[i] == "A":
            x = x.replace(x[i],"f$")
    return x
  
#
print("This is a Password generator, It will go through multiple steps that will from user input create a new password!")
website = input(str("What is the name of the website you would like a password for?"))
print("\n")
website = website.lower()
#multiply the number of letters in webiste by six
websiteletters = len(website)
websiteletters = websiteletters * 6
# If number of letters in website is divisble by three or not two diffrent speacial charecters will be added based on if the 
# statement is true or not
ampersand = "&"
exclamation = "!"
if websiteletters % 3 == 0:
    websiteletters = str(websiteletters) + exclamation
else:
    websiteletters = str(websiteletters) + ampersand
print(websiteletters + "  " + "This is after multiplying numbers of letters in website by six , then checking if that same number is divisble ")
print(" by three If this stament is true it will add exclamation point if not then it will add a ampersand")
print("\n")
# Using this dictionary which has all possible special charecters and lowecase letters for the input, it will assign
# the first two charcecters of the input to their coresponding values
frstwebsitechr = websiteletters[0]
scndwebsitechr = websiteletters[1]
letterschrs = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18
           ,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26," ":27,"!":28,"@":29,"#":30,"$":31,"%":32,"^":33,"&":34,"*":35,
           "(":37,")":38,"-":39,"_":40,"+":41,"=":42,"[":43,"]":44,"{":45,"}":46,"\\":47,"|":48,":":49,";":50,"'":51,"<":52,">":53,
           "?":54,"/":55,"~":56,"`":57}
for key in letterschrs.keys():
  value = letterschrs[key]
  if frstwebsitechr == key:
      frstwebsitechr = value
  if scndwebsitechr == key:
      scndwebsitechr = value
frstscndstr = (str(frstwebsitechr) + str(scndwebsitechr))
print(frstscndstr + "  " + "this after looping through my dictionary of charcters and special charcetres and then assigning the integer values")
print(" to the FIRST and SECOND character in the input corresponding to it, then putting both of them together in a string")
print("\n")
#captalize last two letters of the original input 
lastchr1 = website[len(website)-1]
lastchr2 = website[len(website)-2]
lastchr1 = lastchr1.upper()
lastchr2 = lastchr2.upper()
lastchrs = (str(lastchr2) + str(lastchr1))
print(lastchrs + "  " + "this is after selecting the last two chareceters in the input and captalizing them")
print("\n")
# Using this dictionary above which has all possible special charecters and lowecase letters for the input, it will assign
# the last two charcecters of the input to their coresponding values 
#there will also be a repetiion of the lower method due to the capatalization of the last two charecters
lastchr1=lastchr1.lower()
lastchr2=lastchr2.lower()
for key in letterschrs.keys():
  value = letterschrs[key]
  if lastchr1 == key:
      lastchr1 = value
  if lastchr2 == key:
      lastchr2 = value
lastchr12 = (str(lastchr1) + str(lastchr2))
print(lastchr12 + "   " + "This is after looping through the dictionary again and checking the LAST two and then assigning values to them")
print("and joining them both as a string")
print("\n")
#add first and last letters of website
frstlast = website[0] + website[len(website)-1]
#calling the function with two variables in the code, the ouput of the function will then be saved into two other variable in which 
#will be used to output the final password
output1 = strfilter(frstlast) 
output2 = strfilter(lastchrs) 
print(output1 + "   " + "this is after calling my function that checks if a ceartin charecter is *A* and changes that instances to f$ ")
print(" ^^^ This call was specifically for the first and last  charecter in the input")
print("\n")
print(output2 + "   " + " This again calls the same function however calls back the last two charecters from the input that were")
print("capatalized")
print("\n")
finalpass =  websiteletters + frstscndstr + output2 + lastchr12 + output1
print( "Here is your final password >>>" + "  " + finalpass)




    


    
    

        
    
         

       
        


   

