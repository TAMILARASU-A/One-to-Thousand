"""Finding_Smallest_element"""

arr=[10,20,30,40,50,50,10]
low=arr[0]

for a in arr: 
    if a<low:
        low=a

print("Smallest Element is:",low)
