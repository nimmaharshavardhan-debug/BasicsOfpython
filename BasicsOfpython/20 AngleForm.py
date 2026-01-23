# Check whether three angles form a triangle.

angel_1 = int(input("Enter the value of angel one : "))
angel_2 = int(input("Enter the value of angle two : "))
angel_3 = int(input("Enter the value of angel two : "))

totalAngle = angel_1+angel_2+angel_3

if (totalAngle>0 and  totalAngle==180):
    print("It form a Triangle")
else:
    print("It  not form a Triangle")