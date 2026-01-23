# Check whether a number is a two-digit number.


num = int(input("Enter a value : "))
if (num>=10 and num<=99 and abs(num)):
    print("two digit number")
else:
    print("it is not a two digit number")