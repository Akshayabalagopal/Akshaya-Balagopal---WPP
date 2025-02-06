def digit_root(n):

    while(n//10!=0):
        sum=0

        while n>0:
            p=n%10
            sum=sum+p
            n=n//10
        n=sum
    return n
    
n=int(input("Enter the no: "))
result=digit_root(n)
print("Digital root of n is: ", result)
