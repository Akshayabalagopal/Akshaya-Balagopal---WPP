'''The digital root of a number n is obtained as follows: Add up the digits n to get a new number.
Add up the digits of that to get another new number. Keep doing this until you get a number
that has only one digit. That number is the digital root. For example, if n = 45893, we add up
the digits to get 4+5+8+9+3=29. We then add up the digits of 29 to get 2+9 = 11. We then add
up the digits of 11 to get 1+1 = 2. Since 2 has only one digit, 2 is our digital root. Write a
function that returns the digital root of an integer n. [Note: there is a shortcut, where the digital
root is equal to n mod 9, but do not use that here.]
'''
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
