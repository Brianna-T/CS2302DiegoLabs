"""
Tovar, Brianna
CS2302 Aguirre Diego, TA Eduardo
10/9
Lab 3: Option B, BST/AVL/RBTrees
"""


def user():#method to get user input
    user_tree=input("Which BST would you like today? : AVL or RB-->")
    print("You have chosen, ",user_tree)
    return user_tree
    
def File():#use this to open and read text file, stores into list called "engish_words"
    File_object = open(r"words.txt","r")
    engish_words=[File_object.read().splitlines()]
    return engish_words #will return the list created

class Node:
   def __init__(self, key):
      self.left = None
      self.right = None
      self.key = key

   def __str__(self):#unused, ignore
      return "%s" % self.key
  
class AVLTree():
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0
        
def insert(self, key):
        # Create new node
        n = Node(key)

        # Initial tree
        if self.node == None:
            self.node = n
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        # Insert key to the left subtree
        elif key < self.node.key:
            self.node.left.insert(key)
        # Insert key to the right subtree
        elif key > self.node.key:
            self.node.right.insert(key)

        # Exit, key already exists in the tree
            
        # Rebalance tree if needed
        rebalance(self)
        
def rebalance(self):#rebalancing called when balance isnt correct, calls rotations
        update_heights(self,recursive=False)
        update_balances(self,False)

        while self.balance < -1 or self.balance > 1: 
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Case -> rotate y,z to the left
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()
            
            # Right subtree is larger than left subtree
            if self.balance < -1:
                
                # Right Left Case -> rotate x,z to the right
                if self.node.right.balance > 0:
                    self.node.right.rotate_right() # we're in case III
                    self.update_heights()
                    self.update_balances()

                self.rotate_left()
                self.update_heights()
                self.update_balances()

def update_heights(self, recursive=True):#updates height of tree when its changed
        if self.node: 
            if recursive: 
                if self.node.left: 
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else: 
            self.height = -1

def update_balances(self, recursive=True):#checks balance when needed
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0 
            
def rotate_right(self):
    new_root = self.node.left.node
    new_left_sub = new_root.right.node
    old_root = self.node

    self.node = new_root
    old_root.left.node = new_left_sub
    new_root.right.node = old_root

def rotate_left(self):
    new_root = self.node.right.node
    new_left_sub = new_root.left.node
    old_root = self.node

    self.node = new_root
    old_root.right.node = new_left_sub
    new_root.left.node = old_root
        
def display(self, node=None, level=0):#change?
    if not node:
        node = self.node
    if node.right.node:
        self.display(node.right.node, level + 1)
        print ('\t' * level), ('    /')

    print ('\t' * level), node

    if node.left.node:
        print ('\t' * level), ('    \\')
        self.display(node.left.node, level + 1)

def RBTree(T):
    return

def print_anagrams(word, prefix=""):#checking if word is a word in english dict
    engish_words=File()
    if len(word) <= 1:
       str = prefix + word

       if str in engish_words:
           print(prefix + word)
    else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams(before + after, prefix + cur)
               
def count_anagrams():#will search through your tree to find word and its anagrams and count
    word=input("Which word do you want to see the amount of anagrams it has?")
    count=0
    print("Anagram amount for, ",word,",is, :",count)

def main():#calls methods step by step
    List=File()
    print(List)
    if user()=="AVL":#repeats if statement, dont know why
        tree = AVLTree()
        data = File()

        print("Inserting data", data)
        for key in data: 
            insert(tree,key)
        display(tree)#not working
                
    if user()=="RB":
        RBTree(List)
        
    
    count_anagrams()
        
main()
