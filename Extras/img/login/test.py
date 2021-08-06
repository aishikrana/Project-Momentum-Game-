import csv
  


  
# name of csv file
filename = "db.csv"

a="amit"
b="cse"
c="2"
d="8"
lister=[a,b,c,d]

lines=[]

r = csv.reader(open(filename,newline='')) # Here your csv file
lines = list(r)

# with open(filename, 'r',newline='') as csvfile:
#     csv_reader=csv.reader(csvfile)
    
#     for ele in csv_reader:
#         if ele[1]=='akp':
#             print("exists!")
#             break
print(len(lines))




# writer = csv.writer(open(filename, 'w', newline=''))
# writer.writerows(lines)
  

