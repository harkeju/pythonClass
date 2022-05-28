print("Welcome to Comand-Line Calculator!\n\n INSTRUCTIONS:\n use any of the following operators for your mathemathecal operations,\n Additions: + \n Subtractions: - \n Multiplications: * \n Division: / \n Modulus (Remainder): %")
print("\nLET'S START!\n")
first_number = float(input("Enter a number: "))

select_operator = input("Choose a mathematical operation: ")

second_number = float(input("Enter another number: "))

if select_operator == "+":
  result = round(first_number + second_number)
  print(f"The answer is {result}")
elif select_operator == "-":
  result = round(first_number - second_number)
  print(f"The answer is {result}")
elif select_operator == "*":
  result = round(first_number * second_number)
  print(f"The answer is {result}")
elif select_operator == "/":
  result = round(first_number / second_number)
  print(f"The answer is {result}")
elif select_operator == "%":
  result = round(first_number % second_number)
  print(f"The answer is {result}")
else:
  print("Error! Please read the instructions carefully.")
