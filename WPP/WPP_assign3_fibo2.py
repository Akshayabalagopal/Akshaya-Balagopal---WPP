def fibonacci(n):

    a,b=0,1
    while b<=n:
        if b==n:
            return True
        a,b=b,a+b
    return False

T=int(input("Enter the no of terms: "))
for i in range(T):
    N=int(input("Enter the no: "))
    if fibonacci(N):
        print("IsFibo")
    else:
        print("IsNotFibo")
