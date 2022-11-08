import turtle
import math

def draw1(x1,y1):
  turtle.goto(x1,y1)
  angle1 = y1/x1
  turtle.write(angle1)
  return angle1
  
def draw2(x1,y1,x2,y2):
  turtle.goto(x2,y2)
  angle2 = (y2 - y1) / (x2 - x1)
  turtle.write(angle2)
  return angle2

def calcangle(angle1,angle2):
  if angle1 > angle2:
    formula = (angle1 - angle2) / (1 +(angle1 * angle2))
    rad = math.atan(formula)
  else:
    formula = (angle2 - angle1) / (1 +(angle1 * angle2))
    rad = math.atan(formula)
  
  return rad

def convert(rad):
  deg = rad * (180 / math.pi)
  print(f'The angle between the two slopes is {deg}')





    
if __name__ =="__main__":
  x1 = int(input("Enter your first x coordinate: "))
  x2 = int(input("Enter your second x coordinate: "))
  y1 = int(input("Enter your first y coordinate: "))
  y2 = int(input("Enter your second y coordinate: "))
  angle1 = draw1(x1,y1)
  angle2 = draw2(x1,y1,x2,y2)
  rad = calcangle(angle1,angle2)
  convert(rad)