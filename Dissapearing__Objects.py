"""
Basil Agboola

Prof Gering

CSNE-2923-01


"""


"""
Project Description: You are a museum curator with a formidable knowledge of data structures and algorithms. Your museum contains many rare artifacts, many revered by ancient cultures.
Unfortunately, some of the most strange and valuable items have vanished from the archives. Management has heard of your abilities,
and has thus decided that you must build a better record keeping system so that items will stop disappearing. Given that binary search trees have reasonable performance for both insertion and performance, this seems a natural choice.
"""

""" 
Videos Which aided my solution https://youtu.be/DlWxqU3LLpY?si=fp4Hsn_qzZCtUh1w
"""

## Schema of Tree
class Artifact_Node:       
       def __init__(self,value):
           self.left = None # left node
           self.right = None # right node
           self.value = value # The value of the node in this case it would be the year
       def insert(self,value): 
           if value < self.value:
                if self.left is None:
                   self.left = Artifact_Node(value)     

                else:
                    self.left.insert(value)  
           else:
                if self.right == None:   
                    self.right = Artifact_Node(value)   
                    
                else:
                    self.right.insert(value)
       # this alows us to add nodes following the convention that the left node is smaller than the right node and smaller than the parent node
       
       def traversal(self):
           if self.left:
               self.left.traversal()
           print(self.value)
           if self.right:
               self.right.traversal()    
           print(self.value)
           
       def find(self,value):
           if value < self.value: # then said node is a left node
               if self.left == None:
                    print("This is not in our Museum")
                    return False
               else:
                  return self.left.find(value)    
           elif value > self.value: # then said node is a right node
               if self.right == None:
                   print("This is not in our Museum")    
                   return False
               else:
                   return self.right.find(value)    
                   print("We found it!")
               
           else:
               print("We found it!")
               return self
           
           # the node we are looking for is the said Node

##### Creating a List for the artifacts respective year
           
Artifacts =[1835,2007,2007,1420,1969,1922,1984,1991,1492,2000,1912,1977,1543,1791,1939,2001,1903,1947,1989,1014,1964,1666,1582,2009,1990,1968,1520,1986,2020,
            1348,1879,1971,1327,1980,2004,1512,1985,1953,1925,1966,1930,1685,2006,1453,1908,1964,2023,1796,1889,1687]

#### Creating aList for the artifacts Name


Name = ["Mermaid Tail Prototype"
,"Invisible Cloak Prototype"
,"Last Screenless Phone"
,"Unicorn Horn Paperweight"
,"Lunar Landing Soundstage Photo"
,"Cursed Paperclip"
,"Surveillance Camera"
,"World's Smallest Rubik's Cube"
,"Malfunctioning Compass"
,"Millennium Bug Survival Kit"
,"Titanic Ice Cube Tray"
,"Extraterrestrial Mixtape"
,"Backup Globe"
,"Mozart's Disco Ball"
,"Art Deco Banana Peeler"
,"Hal9000"
,"Leftover Propeller"
,"Authentic Weather Balloon"
,"Berlin Wall Graffiti Stencil"
,"Viking Navigational Pool Noodle"
,"Rejected Song Lyrics"
,"Great Fire of London Original Ash"
,"Unaltered Gregorian Calendar"
,"Unused Bitcoin"
,"Hubble's First Blurry Photo"
,"Peace Sign Copyright Document"
,"Secret Spice Route Map"
,"Glowing Paperweight from Chernobyl"
,"Unopened Hand Sanitizer Bottle"
,"Scented Beak Mask"
,"Edison's First Electric Bill"
,"First Email Spam Folder"
,"Excalibur Maintenance Manual"
,"Pac-Man Unreleased Level"
,"Opportunity Rover Selfie Stick"
,"Leonardo's Leftover Paint"
,"Flux Capacitor User Manual"
,"Everest Summit Flag Replica"
,"Pharaoh's Lost Fedora"
,"Prototype Moon Boots"
,"Al Capone's Secret Diary"
,"Apple Core"
,"Prehistoric WiFi Router"
,"Medieval Coffee Maker"
,"Tunguska Event Souvenir Rock"
,"Portable Rainbow Generator"
,"Coffee Cup With HTML Code"
,"George Washington’s Teeth Mold"
,"Eiffel Tower's Missing Bolt"
,"Newton's Sketch of Black Holes"
]            

## Creating an Instance for the Museum
 
Museum = Artifact_Node(1835) 

# then adding all other years as indexes for our tree

for i in range(len(Artifacts)):     
     Museum.insert(Artifacts[i])

# Setting Up Prompt to search for Artifact by year.

user_lookup = int(input("Look up the year of the Artifact you want to find"))

# using find method to check if user's lookup year exist in the tree

Museum.find(user_lookup)
# Then using that key , I use the adress from the Artifcats to then find The Afrifact name ** via a loop **

for i in range(len(Artifacts)):       
      if user_lookup == Artifacts[i]:
         Search = Name[i]
         
# returning Artifact

print("Here is your artifact! " + str(Search))
    
    
