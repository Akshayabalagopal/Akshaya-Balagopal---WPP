'''Take numbers from 1 to 1000. create equivalance classes for modulo 5 on this set of  numbers.
check the validity of your equivalance classes.[Hint: union of all equivalance classes should be the orginal set/list]
'''
num=[]
n=int(input("Enter the number: "))
for i in range(n):
    num.append(i)

L1=[]
L2=[]
L3=[]
L4=[]
L5=[]

for i in range(n):
    rem=i%5
    if rem==0:
        L1.append(i)
    elif rem==1:
        L2.append(i)
    elif rem==2:
        L3.append(i)
    elif rem==3:
        L4.append(i)
    elif rem==4:
        L5.append(i)
print(L1)
print("\n")
print(L2)
print("\n")
print(L3)
print("\n")
print(L4)
print("\n")
print(L5)
print("\n")

if set(L1+L2+L3+L4+L5)==set(range(n)):
    print("Eqivalance classes are valid")
    