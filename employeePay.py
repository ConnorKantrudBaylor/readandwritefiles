import csv

read = open('EmployeePay.csv','r')

file = csv.reader(read)

next(file)

for i in file:
    bonus = round(int(i[3]) * float(i[4]),2)
    totalPay = round(int(i[3]) + bonus,2)
    print(f"""
          First Name: {i[1]}
          Last Name: {i[2]}
          Salary: ${round(int(i[3]),2)}
          Bonus: ${bonus}
          Pay: ${totalPay}
          """)
    input()

