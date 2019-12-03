"""
Tovar, Brianna
CS2302 Aguirre Diego, TA Eduardo
12/1
Lab 7: Dynamic Programming, Implement Edit-Distance
"""
import numpy as np

def edit_distance(s1,s2): #gives distance between both, such as words
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] ==s2[j-1]:
                d[i,j] =d[i-1,j-1]
            else:
                n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                d[i,j] = min(n)+1
    #print(d)          
    return d[-1,-1]

a= 'TURN'
b= 'STURN'
c= 'LEARN'

print("Results of difference:")
print(edit_distance(a,b))
print(edit_distance(b,c))