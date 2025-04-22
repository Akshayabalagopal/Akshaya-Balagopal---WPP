'''Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary whose keys
are the product names and whose values are the prices. when the user is done entering products and prices, allow them to repeatedly
enter a product name and print the corresponding price or a message if the product is not in the dictionary.
'''
D={}
no1=int(input("Enter the no of items: "))
for i in range(no1):
    pro_name=input("Enter the product name: ")
    price=int(input("Enter the price: "))
    D[pro_name]=price
while True:
    search=input("product to be searched: ")
    for i in D:
        temp=search
        if search==i:
            print("Price is: ", D[temp])
    print("\n")
    print("Enter 1 to search more", "Enter 2 to exit", sep="\n")
    choice=int(input("Enter your choice: "))
    if choice!=1:
        break
