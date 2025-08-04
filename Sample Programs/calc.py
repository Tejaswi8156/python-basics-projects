num1 = int(input("Enter the First Number:"))
num2 = int(input("Enter the Second Number:"))

sum_result = num1+num2
subtract_result = num1-num2
multiply_result = num1*num2
divide_result = num1/num2

print("Select any Operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice(1/2/3/4): ")

if choice == "1":
    print("Result of Operation is: ",sum_result)
elif choice == "2":
    print("Result of operation is: ", subtract_result)
elif choice == "3":
    print ("Result of Operation is: ", multiply_result)
elif choice == "4":
    if num2 != 0:
        print("Result of operation is: ", divide_result)
    else:
        print("Error: Cannot Divide by Zero")
else:
    print("Invalid Choice.")