#codedocs admin kidnap
#T= no of test cases
#N= no of boxes
#S= no of swaps
#X= box with gold coin or position

T = int(input("Enter the no of test cases:"))
N = int(input("Enter the no of boxes:"))
X = int(input("Enter the position of the coin currently:"))
for i in range(T):
    S = int(input("Enter the no of swaps:"))
    for j in range(S):
        first_box = int(input("Enter first box to be swapped:"))
        second_box= int(input("Enter second box to be swapped:"))
        if X==first_box:
            X = second_box
        elif X==second_box:
            X = first_box
            print("The current position of the coin:", X)
