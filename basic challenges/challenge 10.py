import random

options =["rock","paper","scissors"]

rop = random.choice(options)

print(" Do you want to play rock, paper, scissors")
choice = str(input("Enter your choice: "))
print(rop)
if rop == choice:
    print("It is a tie")
elif rop == "paper" and choice == "rock":
    print(" HAHAHAHA you lose and I win")
elif rop == "rock" and choice == "paper":
    print(" Well done you beat me")
elif rop == "rock" and choice == "scissors":
    print(" HAHAHAHA you lose and I win")
elif rop == "scissors" and choice == "rock":
    print("Well done you beat me")
elif rop == "scissors" and choice == "paper":
    print("HAHAHAHA you lose and I win")
