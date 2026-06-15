num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
num3 = (input("Want to add a another number?(y/n):"))
if num3 == 'y':
    num3 = float(input("Enter the number: "))
else: 
    num3 = 0

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = float(input("Enter your choice (1-4): "))

if operation == 1:
    if num3 != 0:
        result = num1 + num2 + num3
        print("The result of addition is:", result)
    else:
     result = num1 + num2
    print("The result of addition is:", result)

elif operation == 2:
    if num3 != 0:
        result = num1 - num2 - num3
        print("The result of the subtraction is:", result)
    else:
        result = num1 - num2
        print("The result of the subtraction is:", result)

elif operation == 3:
    if num3 != 0:
        result = num1 * num2 * num3
        print("The result of multiplication is:", result)
    else:
        result = num1 * num2
        print("The result of multiplication is:", result)

elif operation == 4: 
    if num2 != 0 and num3 != 0:
        result = num1 / num2/ num3
        print("The result of division is:", result)

    elif num2 != 0:
     result = num1 / num2
    print("The result of division is:", result)
else:  
    print("Not defined")

