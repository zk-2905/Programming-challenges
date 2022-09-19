conversion = str(input("Would like to convert cm into inches or inches into cm: "))
number = float(input("Enter a number: "))

def convert_cm(number):
    return number*0.393700787
result1 = convert_cm(number)


def convert_inch(number):
    return number*2.54
result2 = convert_inch(number)


if conversion == "cm into inches":
    print(f"{result2} inches" )
elif conversion == "inches into cm":
    print(f"{result1} cm")