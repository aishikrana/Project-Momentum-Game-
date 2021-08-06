import csv
  
fields = ['Marker', 'Name', 'Password', 'Level_1_min', 'Level_1_sec', 'Level_1_milsec', 'Level_2_min', 'Level_2_sec', 'Level_2_milsec', 'Level_3_min', 'Level_3_sec', 'Level_3_milsec', 'Level_4_min', 'Level_4_sec', 'Level_4_milsec']
  
# data rows of csv file
rows = [['Marked', 'COE', '2', '9.0'],['Sanchit', 'COE', '2', '9.1'],['Aditya', 'IT', '2', '9.3']]
  
# name of csv file
filename = "db.csv"
  
f = open(filename, "w+")
f.close()

with open(filename, 'w',newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
      
    # writing the fields
    csvwriter.writerow(fields)
      
    # writing the data rows
    #csvwriter.writerows(rows)