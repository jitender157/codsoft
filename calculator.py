def calculator():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))


  print("Choose the operation:")
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")

  operation = input("Enter the operation (1/2/3/4): ")
  if operation == '1':
      result = num1 + num2
      op_symbol = '+'
  elif operation == '2':
      result = num1 - num2
      op_symbol = '-'
  elif operation == '3':
      result = num1 * num2
      op_symbol = '*'
  elif operation == '4':
      if num2 != 0:
          result = num1 / num2
          op_symbol = '/'
      else:
          print("Error: Division by zero is not allowed.")
          return
  else:
      print("Invalid operation choice. Please choose 1, 2, 3, or 4.")
      return

  print(f"The result of {num1} {op_symbol} {num2} is: {result}")

calculator()
