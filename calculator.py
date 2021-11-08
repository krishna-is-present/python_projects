
def operation(number1,number2,operator):
  if operator == "+":
    return number1 + number2
  elif operator == "-":
    return number1 - number2
  elif operator == "*":
    return number1 * number2
  elif operator == "/":
    return number1 / number2


number1 = int(input("What is the first number? \n"))

operator = input("What is the operator? \n")

number2 = int(input("What is the second number? \n"))

print(f"The output is {number1} {operator} {number2} = {operation(n1,n2,o)}")
