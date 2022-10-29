import csv 
from pathlib import Path 

csv_file = Path("AAPL.csv")

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
    date = row[0]
    adj_close = float(row[5])
    volume = float(row[6])
    new_date = date.split("-")
    year_month = new_date[0] + new_date[1]
    if year_month not in dict1:
      dict1[year_month] = [0,0,0]  #total sales, Volume, index [0] / index[1]
    
    #### Index 0 ####
    total_sales = adj_close * volume
    dict1[year_month][0] = total_sales
    

    #### Index 1 ####
    dict1[year_month][1] += volume

    
    #### Index 2 ####
    index2 = total_sales / volume
    dict1[year_month][2] += index2      
  
  return dict1


def printdict(dict1):
  print(" Year_Month              Total_Sales          Volume        Avg_Total_Sales")
  for x,y in dict1.items():
    print(f"{x:20} {y[0]:>20}{y[1]:>15}{y[2]:>20}")


if __name__ =="__main__":
  file_contents = read_csv(csv_file)
  dict = process(file_contents)
  printdict(dict)