def mypart():
  answer = int(input("Select Number between 10 and 49: "))
  factor = 99 - answer
  return factor

def yourpart():
  factor = mypart()
  number = int(input("Select a number between 50 and 99: "))
  number2 = number + factor
  if number2 >= 200:
    number3 = (number2 - 200) + 2
  else:
    number3 = (number2 - 100) + 1
  final = number - number3
  return final

print("We are going to play a  game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!")
print("This will be the answer.")
print(yourpart())
