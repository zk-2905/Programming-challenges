answer = 7
x = 0
while x == 0 :
    guess = int(input("Guess a number: "))
    if guess == answer:
        print("Well done!")
        break
else:
    print("Try again")