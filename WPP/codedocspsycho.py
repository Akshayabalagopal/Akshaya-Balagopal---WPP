#codedocs admin psycho
num = int(input("Enter the no of people:"))
L=[]
for i in range(num):
    hgt = int(input("Enter the height of people present:"))
    L.append(hgt)
swap=0
print("Height order is:")
for i in range(num):
    print(L[i])
for i in range(num):
    small = i
    for j in range(i+1, num):
        if L[j]<L[small]:
            small = j
    if small != i:
            L[i],L[small]= L[small],L[i]
            swap+=1
print("Sorted height order is:")
for i in range(num):
    print(L[i])
print("\nNo of min swaps is:",swap, sep="\n")