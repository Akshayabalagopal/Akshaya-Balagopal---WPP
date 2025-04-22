'''find digits
you are given a number N, you need to print the number of positions where digits exactly divides N.
input: first line contains T number of test cases followed by T lines each containing N.
constraints: 1<=T<=15, 0<=N<=10^10
output: for each test case print the number of positions in n where digits in that number exactly divides the number N in seperate
line.
input: 2 12 13
output: 2 1
'''

L=[]
T=int(input("Enter no of test cases: "))
for i in range(T):
    n=int(input("Enter the number: "))
    L.append(n)
    count=0

for i in range(T):
    temp=L[i]
    count=0
    while (temp!=0):
        p=temp%10
        if L[i]%p==0:
            count+=1
        temp=temp//10
    print("Count: ", count)
    count=0
