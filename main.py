import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents


def process(csv_contents):
  dict1 = {}
  for row in csv_contents:
    home_team = row[1]
    away_team = row[2]
    home_goal = row[3]
    away_goal = row[4]
    winner = row[5]
    gd = int(home_goal) - int(away_goal)
    gd2 = int(away_goal) - int(home_goal)
    if home_team not in dict1:
      dict1[home_team] = [0,0,0,0,0] # wins, draws, losses, goal_difference, points
    if away_team not in dict1:
      dict1[away_team] = [0,0,0,0,0] # wins, draws, losses, goal_difference, points
    
    if winner == "D":
      dict1[home_team][1] += 1
      dict1[home_team][4] += 1
      dict1[away_team][1] += 1
      dict1[away_team][4] += 1
    if winner == "H":
      dict1[home_team][0] += 1
      dict1[home_team][4] += 3
      dict1[away_team][2] += 1
      
    if winner == "A":
      dict1[away_team][0] += 1
      dict1[away_team][4] += 3
      dict1[home_team][2] += 1

    dict1[home_team][3] += gd
    dict1[away_team][3] += gd2
      
  return dict1



def printdictrow(dict1):
  print(" Team              Wins    Draws    Losses   GD    Points")
  for x,y in dict1.items():
    print(f"{x:15} {y[0]:>6}{y[1]:>6}{y[2]:>10}{y[3]:>9}{y[4]:>6}")
    
if __name__ == "__main__":
  file_contents = read_csv(csv_file)
  league_dict = process(file_contents)
  printdictrow(league_dict)
  