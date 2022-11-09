def slayer():
  print("Guess a six-digit number SLAYER so that following equation is true, where each letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS.")
  guess = str(input("Enter your guess for SLAYER: "))
  num1 = guess[1::]
  num2 = guess[0]
  final_num = num1 + num2

  if int(guess) + int(guess) + int(guess) == int(final_num):
    print("Your guess is correct: ")
    print(f"SLAYER + SLAYER + SLAYER = {final_num}")
    print(f"LAYERS = {final_num}")
    print("Thanks for playing.")
  else:
    print("Your guess is incorrect")
    print(f"SLAYER + SLAYER + SLAYER = {guess}")
    print(f"LAYERS = {final_num}")
    print("Thanks for playing.")


  
slayer()