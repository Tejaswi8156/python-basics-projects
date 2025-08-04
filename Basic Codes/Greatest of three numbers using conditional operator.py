num1 = float(input("Enter the number: "))
num2 = float(input("Enter the number: "))
num3 = float(input("Enter the number: "))
if (num1>num2) and (num1>num3):
    greatest= num1
elif (num2>num1) and (num2>num3):
    greatest= num2
else:
    greatest= num3
print("the greatest among these three numbers are: ",greatest)