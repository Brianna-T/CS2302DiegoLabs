"""
Tovar, Brianna
CS2302 Aguirre Diego, TA Gerardo, IA Edurardo
Last Modify: 9/22
Lab 2: Option B, Sorting
"""
import time

class Node(object):  #node attributes
    password=""
    count=-1
    next=None
    
    def _init_(self,password,count,next):
        self.password=password
        self.count=count
        self.next=next
        
class List(object):  #list attributes
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
LL=List()#creates Linked List(head, tail)
        
def IsEmpty(LL):  
    return LL.head == None
        
def Append(LL,x): 
    # Inserts x at end of list L
    if IsEmpty(LL):
        LL.head = Node(x)
        LL.tail = LL.head
    else:
        LL.tail.next = Node(x)
        LL.tail = LL.tail.next
        
def file(filename):
    L=open(filename,'r')
    for i in range(1000):
        L.readline().split('\t')
    return L
        
#Solution A
def solutionA(L):
    for i in range(len(L)):#traversing txt file list
        if L[i] in LL:#if that password is in LL already
            LL[i].count+=1#count up for that password
        else:
            Append(LL,i)
    return LL

#Solution B
def solutionB(L):
    for i in L:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    return

#Solution A Bubble Sort
def BubbleSort(L):
    change= True#variable for boolean
    while change:
        t=L.head#setting variable for start of list
        change= False
        while t.next is not None:
            if t.item<t.next.item:#if current item is less than next item
                temp=t.item
                t.item=t.next.item#switch
                t.next.item=temp
                change= True#changing boolean to keep track of whats True/False
            t=t.next#onto next item
            

#Solution B Merge Sort
def Merge(L):
    if IsEmpty:
        return None
    else:
        DivideConquor(L)
        print(L)
    
def DivideConquor(L):
    temp=L.head
    mid=len(L)//2
    L1=L[mid:]
    L2=L[:mid]
    i=0#tracking for L1
    j=0#tracking for L2
    f=0#tracking for entire L
    while temp is not None:
        while i<len(L1) and j<len(L2):#if both split lists are less than its length
            if L1[i]>L2[j]:#if its value is bigger, then will make compare/sort
                L[f]=L2[j]
                j+=1
            else:
                L[f]=L1[i]
                i+=1
            f+=1
        while i<len(L1):#if L1 index less than length
            L[f]=L1[i]
            i+=1
            f+=1
        while j<len(L2):#if L2 index less than length
            L[f]=L2[j]
            j+=1
            f+=1
    return L

def main():
    L=file('Passwords.txt')
    solutionA(L)
    
main()