def convert1(prompt):
  roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100 }
  final1 = 0
  roman_num2 = {}
  for x in prompt:
    if x not in roman_num2:
      roman_num2[x] = 1
    else:
      roman_num2[x] += 1
  
  final_dict = {}
  for i,j in roman_num2.items():
    for x,y in roman_num.items():
      if x == i:
        final_dict[i] = y * j
  for x,y in final_dict.items():
     if x in prompt:
       final1 += y
  print(f'Value of {prompt} is: {final1} ')
  return final1

def convert2(prompt2):
  roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100 }
  final2 = 0
  roman_num2 = {}
  for x in prompt2:
    if x not in roman_num2:
      roman_num2[x] = 1
    else:
      roman_num2[x] += 1
  
  final_dict = {}
  for i,j in roman_num2.items():
    for x,y in roman_num.items():
      if x == i:
        final_dict[i] = y * j
  for x,y in final_dict.items():
     if x in prompt2:
       final2 += y
  print(f'Value of {prompt2} is: {final2} ')
  return final2

def sum(a,b):
  sum = a + b
  print(f'Digital sum is: {sum}')
  return sum

def convert3(c):
  roman_num = ""
  while c > 0:
    if c >= 100:
      c -= 100
      roman_num += "C"
    elif c >= 50:
      c-= 50
      roman_num += "L"
    elif c >= 10:
      c-= 10
      roman_num += "X"
    elif c >= 5:
      c-= 5
      roman_num += "V"
    else:
      c-=1
      roman_num += "I"
  print(f'Roman Sum is: {roman_num}')
  
if __name__ == "__main__":
  prompt = input("Enter your first roman numeral: ")
  a = convert1(prompt)
  prompt2 = input("Enter your second roman numeral: ")
  b = convert2(prompt2)
  c = sum(a,b)
  convert3(c)