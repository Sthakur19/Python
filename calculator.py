from art1 import logo

#Add function
def add(n1, n2):
  return n1 + n2

#Substract Function
def substract(n1, n2):
  return n1 - n2

#multiple Functiom
def multiple(n1, n2):
  return n1 * n2

#devide Function
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiple,
  "/" : divide
}

def calculator():
  print(logo)
  num1 = float(input("Please enter first number?: "))
  for key in operations:
    print(key)
  should_continue = True
  while should_continue:
    operation_symbol = input("Please an operations ")
    num2 = float(input("Whats the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    exit_or_contine= float(f"Type 'y' to continue  calculating with {answer}: or type 'N' to start new calculation ")
    if exit_or_contine == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
  

 
    
  
