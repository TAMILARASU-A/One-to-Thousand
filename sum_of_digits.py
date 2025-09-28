"""Sum of digits"""

n=int(input("Enter a number:"))
lst=0
temp=n
while temp>0:
    lst+=temp%10
    temp=temp//10
print(lst)
