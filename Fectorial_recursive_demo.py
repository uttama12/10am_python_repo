def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
x1=int(input("Enter number"))
print("factorial Number::",factorial(x1))