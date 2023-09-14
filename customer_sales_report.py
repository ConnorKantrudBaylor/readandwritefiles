import csv

customerID = 250 #input("Enter the customer ID you'd like to start indexing at: ")
total = 0

file = open('sales.csv','r')
csvFile = csv.reader(file)

newFile = open('salesreport.csv','w')
newFile.write('Customer ID,Total\n')

next(csvFile)

for i in csvFile:
    if customerID == i[0]:
        total += (float(i[3]) + float(i[4]) + float(i[5]))
    else:
        rounded = "{:.2f}".format(total)
        newFile.write(f"{customerID},{rounded}\n")
        customerID = i[0]
        total = float(i[3]) + float(i[4]) + float(i[5])

newFile.write(f"{customerID},{total}")