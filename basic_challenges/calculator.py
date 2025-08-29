# calculator.py
def simple_calculator():
    print("Python Calculator")
    num1 = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ")
    num2 = float(input("Second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"
    
    print(f"Result: {result}")

if __name__ == "__main__":
    simple_calculator()