allowed_operators = ["+", "*", "/", "-"]


print("\nhi there this is a calculator\n")

while True:  
#ask's for the first number and saves it at first_number
  first_number = input("whats is the first number ?\n\nOr would you like to quit ?\n\n")
  try:
    if first_number == "quit":
      break
    first_number = int(first_number)
    
  #ask's for the last number and saves it at last_number
    last_number = input("\nwhats the last number ?\n")
    last_number = int(last_number)
    
  #finds what to do with the numbers
    while True:
      what_to_do = input("\nwhat would you like to do ? (+, -, *, /)\n")
      if what_to_do in allowed_operators:
        if what_to_do == "+":
          answer = (first_number + last_number)
          print(f"|{answer}|")
          break
        elif what_to_do == "-":
          answer = (first_number - last_number)
          print(f"|{answer}|")
          break
        elif what_to_do == "*":
          answer = (first_number * last_number)
          print(f"|{answer}|")
          break
        elif what_to_do == "/":
          answer = (first_number / last_number)
          print(f"|{answer}|")
          break
      else:
        print(f"pleasy type a valid operator like {allowed_operators}")

  except (ValueError, ZeroDivisionError):
    print("pls type a valid number or action and dont devide by zero :D\n")
    