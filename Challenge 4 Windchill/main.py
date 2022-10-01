def your_wind_chill(degrees, MPH):
  yourwindchill = 35.74 + 0.6215 * degrees - 35.75 * MPH**0.16 + 0.4275 * degrees*MPH**0.16
  return yourwindchill


def auto_wind_chill1():
  windchill1 = 35.74 + 0.6215 * 10 - 35.75 * 15**0.16 + 0.4275 * 10*15**0.16
  return windchill1

def auto_wind_chill2():
  windchill2 = 35.74 + 0.6215 * 0 - 35.75 * 25**0.16 + 0.4275 * 0*25**0.16
  return windchill2

def auto_wind_chill3():
  windchill3 = 35.74 +0.6215 * -10 - 35.75 * 35**0.16 + 0.4275 * -10*35**0.16
  return windchill3
  
auto1 = auto_wind_chill1()
auto2 = auto_wind_chill2()
auto3 = auto_wind_chill3()
print(f"Temperature of 10 and speed of 15 gives windchill of: {auto1}")
print(f"Temperature of 0 and speed of 25 gives windchill of: {auto2}")
print(f"Temperature of -10 and speed of 35 gives windchill of: {auto3}")
degrees = float(input("Temperature: "))
MPH = float(input("Speed: "))
final = your_wind_chill(degrees, MPH)
print(f"Windchill: {final}")