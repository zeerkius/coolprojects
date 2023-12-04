# Basil Agboola
# Robert Gering
# Heap of Presents
# CSNE-2923-01

# Project Description
'''
Project Description: Santa has hired you to keep track of his Christmas present delivery system. Naturally, you have decided that the optimal data structure for this task is a heap.

Requirements:
Your program must implement a heap, in which each element of the heap is composed of a tuple containing a numeric delivery priority and gift name.
Santa must be able to run your program from the command line, and input new presents (insert operation).
Santa must be able to view the current-highest delivery priority (peek operation).
Santa must be able to deliver a gift (remove operation).
'''
# Link for aiding in builiding heap data structure https://youtu.be/hkyzcLkmoBY?si=wtQDpUzuT_qPSrEt



# this creates our Heap
class Heap:
    def __init__(self,capacity,name): # where capcity represents the max items
        self.storage = [0]*capacity # since we will sue an areay to implement our heap. The capacity will be the array length
        self.capacity = capacity
        self.size = 0 # this initializing the size of the list to zero 
        self.name_storage = [0]*capacity # initilaizing the names list , we will also use an array to implement the list of names associated with the nodes
        self.name = name
            
    def getParentIndex(self,index):
        return (index-1)//2 # this will help us return the index of the parent nodes
    
    def getLeftChildIndex(self,index):
        return 2*index + 1 # returns the left index nodes    
    
    def getRightChildIndex(self,index):
        return 2* index + 2 # return ths right index nodes 
    
    def hasparent(self,index): # this will let us know if a node has a index or not , meaning if it is the root method , will return true or false
        return self.getParentIndex(index) >= 0 # when it satifies the condition this means it ha s a parent and isnt the root node
    
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size # if it passes the condition it means it has a left child
    
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size # if it passes the condition it means it ha s a right child
    
    def returnNameParent(self,index,name): # this will allow us to return the name associated with the node
        for i in range(len(self.name_storage)): # travers the list name
            if self.name_storage[i] == getParentIndex(self,index): # see if index mateches the specific index we are looking for 
                name = self.name_storage[self.getParentIndex(index)]# then return that index which will then allow us to return the index name , we will then repeat this for right and left nodes
                return name  

    def returnNameLeftChild(self,index,name):# left childern
        for i in range(len(self.name_storage)):
            if self.name_storage[i] == getLeftChildIndex(self,index):
                name = self.name_storage[self.getLeftChild(self,index)]
                return name
    
    def returnNameRightChild(self,index,name): # right children
        for i in range(len(self.name_storage)):    
            if self.name_storage[i] == getRightChildIndex(self,index):
                name = self.name_storage[self.getRightChildIndex(self,index)]
                return name
    
    def parent(self,index): # returns priority node number these methods will be repeated for left and right childern
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self,index): # left children
        return self.storage[self.getLeftChildIndex(index)] 
    
    def rightChild(self,index): # right children
        return self.storage[self.getRightChildIndex(index)]
    
    def IsFullPriority(self):
        return self.size == self.capacity # this will let us know if we can add more presents to check priority of
    
    def IsFullNames(self):
        return self.name_storage == self.capacity # this will let us know if our name list is full
        
     
    def swap(self,index1,index2): # this is for swapping children when partialy sorting the heap so it satifies the heap condition
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
    

        
    def heapifyUp(self):
        index = self.size - 1 # this defines
        while((self.hasparent(index)) and (self.parent(index) > self.storage[index])): # this walks up the heap as long as we have a parent node and it is greater
            self.swap(self.getParentIndex(index),index) #if not then we swap it
            index = self.getParentIndex(index) 
    
    def removeMin(self): # does the bottow down functionality when resorting after removing
        if(self.size == 0):
            raise Exception("Empty Heap")
        data = self.storage[0] 
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return data
    
    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            if(self.storage[index] < self.storage[smallerChildIndex]):
                break
            else:
                self.swap(index,smallerChildIndex)
            index = smallerChildIndex            
        
        



    # we are now going to create functions so we can append inside our heap
    def appendpresents(self,data):
        if self.IsFullPriority():
           print("The present priority list is full")
        self.storage[self.size] = data # this will then append the present priority which will be a number
        self.size += 1 # since the heap may be full then it will ad more space in case we wwould like to append more to th heap
        self.heapifyUp() # this will then partially order our heap in a last in first out way
        
    # we will do the same for names
    def appendname(self,name):
        if self.IsFullNames():
            print("All the good children have been accounted for")
        self.name_storage[self.size] = name # this will append the names to the names list
        self.size += 1 
        self.heapifyUp()
   
    def peek(self): # returns hightest priority element
        return min(self.storage)
        
# creating instance of heap
Presents = Heap(100,"Christmas 2023") # capacity of the heap will be 100 presents with its name specifiying the year


for i in range(100): 
    Presents.appendpresents(i+1)
    

print(Presents.peek())


    
for i in range(100):
    Presents.removeMin()


    


    
    

