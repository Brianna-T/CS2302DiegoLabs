"""
Tovar, Brianna
CS2302 Aguirre Diego, TA Eduardo
11/9
Lab 5: No Option, Least Recently Used Cache
"""
class Node:
    def __init__(self, key, value):
        """
        creating node to have the key, value with it,
        and the prev and next pointers to help keep track
        """
        self.prev=None
        self.key=key
        self.value=value
        self.next=None
        
class LRUcache:
    def _init_(self,cap):
        self.head=Node('head','head')
        self.tail=Node('tail','tail')
        self.cap=cap
        self.dict={}
        
        
    #Problem A    
    def get(self,k):
        """
        will take a reference to a key in self.dict
        and then print its value
        """
        if k==None:
            return None
        if k not in self.dict:
            return -1
        for key, value in self.dict:#error:not enough values to unpack (expected 2, got 1)
            if key==k:
                return value
        
    def put(self,key,value):#unfinished
        """
        Insert or replace the value
        if the given key is not already in the cache. When the cache reaches its 
        maximum capacity, it should invalidate the least recently used 
        item before inserting a new item.
        """
        if self is None:
            return None
        if key or value is None:
            return "no key nor value given"
        
        return
    
    def size(self):
        if self is None:
            return None
        count=0
        for i in self.dict:
            count+=1
        return print("LRU size is: ",count)
    
    def capacity(self):
        if self is None:
            return None
        return print("Max Capacity is: ",self.cap)
        
    #Problem B
    """
    Given a list of words (strings), 
    print the k most frequent elements in descending order. 
    When you print, you have to print the word and its number 
    of occurrences in the list.

    If two words have the same frequency, the word with the 
    lower alphabetical order comes first. Use a heap to receive credit.

    """
    
    def print_descend(self):#unfinished
        if self is None:
            return None
        #create helper method to determine the amount of times word appears
        return
    
    def count(self):
        count=0
        for i in self.dict:
            #if
            count+=1
        return count
    
def main():
    LRU=LRUcache()
    LRU.cap=3
    LRU.dict={"A":0,"B":1,"C":2}
    print("Current Cache is: ",LRU.dict)
    LRU.head=next(iter(LRU.dict))
    print("Head now: ",LRU.head)

    
    #LRU.get("A")
    LRU.size()
    LRU.capacity()
    
    LRU2=LRUcache()
    LRU2.cap=3
    LRU2.dict={"Hello":0,"World":2,"Python":4}
    print("Current Cache is: ",LRU2.dict)
    
main()
        
            

