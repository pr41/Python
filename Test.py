num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = float(input("Choose operation(1 to 4):"))

if choice == 1:
    answer = num1 + num2 
    print("The answer is", answer)
elif choice == 2:
    answer = num1 - num2
    print("The answer is", answer)
elif choice == 3:
    answer = num1 * num2 
    print("The answer is", answer)
elif choice == 4:
    if num2 != 0:
        answer = num1 / num2
        print("The answer is", answer)
    else:
        print("Not Defined")
else:
     print("Invalid Choice")
