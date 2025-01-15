#to swap two nos without using third variable
no1=int(input("Enter the first number: "))
no2=int(input("Enter the second number: "))
no1=no1+no2
no2=no1-no2
no1=no1-no2 
print("After swap: ")
print("The first no: ", no1)
print("The second no: ", no2)