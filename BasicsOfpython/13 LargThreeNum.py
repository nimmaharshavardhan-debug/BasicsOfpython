# Take three numbers and find the largest.
num1 = int(input("Enter num1 value : "))
num2 = int(input("Enter num2 value : "))
num3 = int(input("Enter num3 value : "))
if (num1 >= num2 ):
    print(num1," is greater than ",num2,num3)
elif(num2 >= num3):
    print(num2," is greater than ",num3,num1,)
else:
    print(num3," is greater than ",num1,num2)