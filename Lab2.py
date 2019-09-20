"""
Tovar, Brianna
CS2302 Aguirre Diego, TA Gerardo, IA Edurardo
Last Modify: 9/19
Lab 2: Option B, Sorting
"""

class Node(object):
    password=''
    count=-1
    next=None
    
    def _init_(self,password,count,next):
        self.password=password
        self.count=count
        self.next=next
        
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
    
L=open("Passwords.txt")#reads file of combo passwords
    
#L=["hi","it"]#tester
dict={}
        
#Solution A
#need to fix first solution
    
key=L.password#needs fixing, not sure how to make current item into key to compare
for item in L:#traversing
    if item in L:#if it exists in L
        if item==key:#if its duplicated
            L.count+=1
        else:
            item=item.next
    else:
        item=L.item.next#adding item into L if it wwasn't before
print(L.count)
        
#Solution B
for i in L:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
                
#Solution A Bubble Sort

#Solution B Merge Sort

L.close()#closing the read
