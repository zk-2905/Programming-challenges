distance = float(input("Enter your distance travelled in metres: "))
time = float(input("Enter how long it took you travel that distance in seconds: "))

def speed():
    return distance/time
result = speed()

print(f"{result} m/s")