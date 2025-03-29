def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b
def modulus(a,b):
    return a%b
def power(a,b):
    return a**b

def calculator():
    print("🖩 Simple CLI Calculator")
    print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide)")
    
    while True:
        try:
            operator = input("Enter operation (+, -, *, /,%,**) or 'q' to quit: ")

            if operator.lower() == 'q':
                print("Exiting calculator. Goodbye! 👋")
                break
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator=="%":
                result=modulus(num1,num2)
            elif operator=="**":
                result=power(num1,num2)
            else:
                print("❌ Invalid operator! Please enter +, -, *, or /")
                continue

            print(f"✅ Result: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")

calculator()
