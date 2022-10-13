operator = {'+': lambda i, j: i + j,
           '-': lambda i, j: i - j,
           '*': lambda i, j: i * j,
           '/': lambda i, j: i / j,}

def table ():
  try:
    numbers = int(input("Please enter a number: "))
  except:
    numbers = int(input("Please enter a number again: "))  
  
  operation = input("Please enter an operation: +, -, *, /: ")
  
  firstline = operation + " | "
  calc = ""
  for x in range(numbers+1):
    firstline+= f'{str(x):<4}'
  print(firstline) 
  print("-"*int(5*(numbers+1)))
  for i in range(numbers+1):
    calc += f"{str(i):<2}|"
    for j in range(numbers+1): 
      try:
        calc += f'{round(operator[operation](i, j),1):<5}'
      except ZeroDivisionError:
        calc += f'{0:<3}'
    
    calc += "\n"
  
  print(calc)
  
table()