'''create the following lists using a for loop.
a) a list containing of integers 0 through 49
b) a list containing squares of integers 1 through 50
c) list['a','bb','ccc','dddd'] that ends with 26 copies of the letter z
'''

#a)
L=[]
for i in range(50):
    L.append(i)
print("a)", L)
print("\n")

#b)
L=[]
for i in range(1,51):
    L.append(pow(i,2))
print("b)", L)
print("\n")

#c)
L=[]
str=''
for i in range(1,27):
    L.append(chr(96+i)*i)
print("c)", L)
print("\n")