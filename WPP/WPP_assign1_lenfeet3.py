'''Write a program that asks the user to enter a length in feet.
the program should then be give the user option to conver from feet to inches, yards, miles, millimeters, centimeters, meters or
kilometers. say if the user enters a 1, then the program converts to inches, if they enter 2, then the program converts to yards, etc.
while this can be done with if statements, it is much shorter with lists and is also easier to add new conversions if you use lists
'''

lgt=int(input("Enter the length in feet:"))
lst=['inches','yards','miles','millimeters','centimeters','meters','kilometers']
conversions=[12,1/3,1/5280,304.8,30.48,0.3048,0.0003048]
print("Enter 1 to convert to inches")
print("Enter 2 to convert to yards")
print("Enter 3 to convert to miles")
print("Enter 4 to convert to millimeters")
print("Enter 5 to convert to centimeters")
print("Enter 6 to convert to meters")
print("Enter 7 to convert to kilometers")
cho=int(input("Enter your choice:"))
if ((cho>0)) & ((cho<8)):
    print(lgt, "Feet is: ",lgt*conversions[cho-1], lst[cho-1])
else:
    print("Choice invalid")
