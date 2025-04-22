'''write a program that generates 100 random integers that are either 0 or 1.
Then find the longest run of zeroes, the largest of zeroes in a row.
For instance, the longest run of zeroes in [1,0,1,1,0,0,0,0,1,0,0] is 4.
'''

import random
L=[]
L1=[]
for i in range(100):
    L.append(random.randint(0,1))
print(L)
count=0
for i in range(len(L)):
   if L[i]==0:
      count+=1
      if i==len(L)-1:
         L1.append(count)
      elif L[i+1]==1:
         L1.append(count)
         count=0
print("\n")
print("Maximum occurance of 0 in the list: ", max(L1))
print("\n")