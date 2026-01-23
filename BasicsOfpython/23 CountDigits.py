# count the number digits 

num = int(input("Enter a value : "))
count = 0
if abs(num)==0:
    count=1
else:
    while (abs(num)>0):
        count+=1
        abs(num)//10

print("Number of digits :",count)



