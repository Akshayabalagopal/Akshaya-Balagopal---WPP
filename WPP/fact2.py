#to find the factorial of a no
num=int(input("Enter a number: "))
fact=1
i=1
while i<num :
    fact=fact*i
    i+=1
    print("Factorial of a no: ", fact)