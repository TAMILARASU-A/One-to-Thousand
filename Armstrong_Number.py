"""Armstrong_Number"""

num=int(input("Enter a number to check it is an Armstrong or not:"))
temp=num
len=len(str(num))
val=0
while num>0:
    n=num%10
    val=val+n**len
    num=num//10
if val==temp:
    print("Armstrong Number...!")
else:
    print("Not an Armstrong Number...!")
