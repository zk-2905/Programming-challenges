def input_string():
  valid_input = False
  while valid_input==False:
    try:
      user_string = str(input("Input a string:"))
      if user_string.isalpha()!=True:
        raise ValueError
      else:
        valid_input = True
        user_string = user_string.upper()
        dict_substring = find_substrings(user_string)
        calc_score(dict_substring)
        scores = calc_score(dict_substring)
        printoutput(scores)
        
    except ValueError:
      print("Not a valid string")
    
    

def calc_score(dict_substring):
  Vscore = 0
  Cscore = 0
  vowels = ["A","E","I","O","U"]
  consonants = ["B","C","D","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"]
  for x,y in dict_substring.items():
    for i in vowels:
      if x[0] == i:
        Vscore += y
  for x,y in dict_substring.items():
    for i in consonants:
      if x[0] == i:
        Cscore += y
  
  return (Vscore, Cscore)
      
def printoutput (scores):
  print(f'Stuart {scores[1]}')
  print(f'Kevin {scores[0]}')  
  


def find_substrings(user_string):
  length= len(user_string)
  words = []
  dict_count = {}
  for x in range(length):
    for i in range(x,length):
      words.append(user_string[x:i+1])

  for item in words:
    if item not in dict_count:
      dict_count[item] = 1
    else:
      dict_count[item] += 1
  return dict_count


if __name__ =="__main__":
  input_string()
  
  