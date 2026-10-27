# Defining the 4 operators with return values
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try: 
         return num1 / num2
    except ZeroDivisionError:
         print("Error! Can't divide by zero!")
         return 

def main(): 
        print("===Function Calculator===")
        print("Choose an Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

choice = input("Enter choice (1/2/3/4): ").strip()

if choice not in ("1", "2", "3", "4"):
     print("Invalid choice! Exiting program.")

# Try/Except block for catching non-number inputs
try:
    num1= float(input("Enter first number: "))
    num2= float(input("Enter the second number: "))
except ValueError:
     print("Error! Invalid input dectected! Please enter numbers only.")

# Perform calculations based on choice
if choice == "1":
     result = add(num1, num2)
     print(f"Result: {num1}+{num2} = {result}") 

elif choice == "2":
     result = subtract(num1, num2)
     print(f"Result: {num1}-{num2} = {result}")

elif choice == "3":
     result = multiply(num1, num2)
     print(f"Result: {num1}*{num2} = {result}")

elif choice == "4":
     result = divide(num1, num2)
     if result is not None:
          print(f"Result: {num1} / {num2} = {result}")
