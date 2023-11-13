def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def devide(n1,n2):
  return n1/n2


num1 = int(input("What is your first number?: "))

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : devide 
}  
  # Create a dictionary of math functions: {name: key}
#iterating dictionary; __name__ is for values
for symbol, description in operations.items():
  print(f"symbol is {symbol}, description is {description.__name__}")
symbol =input("What is your symbol?: ")
num2 = int(input("What is your second number?: "))

calculation_function = operations[symbol]
answer= calculation_function(num1,num2)
print(answer)