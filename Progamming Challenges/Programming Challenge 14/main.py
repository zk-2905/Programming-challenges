def calc(prompt):
  op = prompt[4:]
  if op == '+':
    print(int(prompt[0]) + int(prompt[2]))
  elif op == '-':
    print(int(prompt[0]) - int(prompt[2]))
  elif op == '*':
    print(int(prompt[0]) * int(prompt[2]))
  elif op == '/':
    print(int(prompt[0]) / int(prompt[2]))
  elif op == '//':
    print(int(prompt[0]) // int(prompt[2]))
  elif op == '%':
    print(int(prompt[0]) % int(prompt[2]))
  elif op == '**':
    print(int(prompt[0]) ** int(prompt[2]))


if __name__ =="__main__":
  x = 0
  while x == 0:
    prompt = input("Enter your calculation: ")
    calc(prompt)
    if prompt[0] == 'q':
      break
  