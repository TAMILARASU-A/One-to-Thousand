"""Factorial of a Number using recursion"""

n=int(input("Enter a number:"))
def fact(n):
    if n==0 or n==1:
        return n
    else:
        return n*fact(n-1)

print(fact(n))
print(fact(4))
