# Project Idea: Calulator

operator = input('Select An Operator (+ - * /): ')
numOne = float(input('Select First Number: '))
numTwo = float(input('Select Second Number: '))

# real logic starts from here!
if operator == "+":
    print(f"Result: {numOne + numTwo}")
elif operator == "-":
    print(f"Result: {numOne - numTwo}")
elif operator == "*":
    print(f"Result: {numOne * numTwo}")
elif operator == "/":
    if numTwo != 0: # some extra feature to avoid division with zero
        print(f"Result: {numOne / numTwo}")
    else:
        print("Error: Cannot divide by zero") 
else:
    print("Invalid Operator")