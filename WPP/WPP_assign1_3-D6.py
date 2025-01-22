'''Consider a 3-D co-ordinate space. input 10 3-D points. find the nearest neighbour for each of the points in your 3-d space and store
them in a list. the final output is a list with each consisting of a point and its nearest neighbour.[Hint: Use distance between two
points formula].
'''
L=[]
L1=[]
import math
for i in range(10):
    L2=[]
    for j in range(3):
        Cor=int(input("Enter the co-ordinate: "))
        L2.append(Cor)
    L.append(L2)
for i in range(len(L)):
    for j in range(i+1, len(L)):
        a1,a2,a3=L[i][0],L[i][1],L[i][2]
        b1,b2,b3=L[j][0],L[j][1],L[j][2]
        dist=math.sqrt(((a1-b1)**2)+ ((a2-b2)**2)+ ((a3-b3)**2))
        L1.append(dist)
print("\nThe minimum distance: ", min(L1))
    