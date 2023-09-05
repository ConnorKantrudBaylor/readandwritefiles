import csv

customer_country = open('customer_country.csv','w')

x = 0

customers = open('customers.csv','r')

csv_file = csv.reader(customers)

next(csv_file) #skips a row

for record in csv_file:
    fullname = record[1] + " " + record[2]
    customer_country.write(f'{fullname}, {record[4]}\n')
    x += 1

print(f'{x} entries written.')
