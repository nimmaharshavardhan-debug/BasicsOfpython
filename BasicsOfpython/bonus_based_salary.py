# Calculate bonus based on salary.
salary = int(input("Enter salary: "))

if salary >= 50000:
    bonus = salary * 0.10
elif salary >= 30000:
    bonus = salary * 0.07
else:
    bonus = salary * 0.05

print("Bonus amount:", bonus)
