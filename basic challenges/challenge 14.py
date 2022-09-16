string1= str(input("Enter a sentence: "))
split = (string1.split(" "))
list1=[]
for word in split:
    if word == "the":
        list1.append("the")
stringlength =len(list1)
print(f" You have the word 'the' this many times {stringlength}")
