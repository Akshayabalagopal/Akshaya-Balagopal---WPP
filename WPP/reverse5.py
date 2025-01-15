#find reverse of a no
num=int(input("Enter a number: "))
print("The reversed number is: ")
sum=0
while num>0 :
    digit=num%10
    sum=(sum*10)+digit
    num=num//10
    print(digit,end=" ")