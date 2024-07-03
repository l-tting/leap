basic_salary = float(input("Enter basic salary: "))
overtime = float(input("Enter overtime hours worked: "))

if overtime <= 50:
    rate = 300 * overtime
else:
    rate = 15000 + ((overtime -50) * 350)

gross_salary = basic_salary + rate


if gross_salary < 9500:
    tax = 0
elif gross_salary >=9500 and gross_salary < 16000:
    tax = 0.03 * gross_salary
elif gross_salary >= 16000 and gross_salary < 25000:
    tax = 0.05 * gross_salary
elif gross_salary >= 25000 and gross_salary < 35000:
    tax = 0.08 * gross_salary
elif gross_salary >= 35000 and gross_salary < 40000:
    tax = 0.11 * gross_salary
elif gross_salary >= 40000 and gross_salary < 50000:
    tax= 0.12 * gross_salary
else:
    tax = 0.14 * gross_salary



nssf = 80
nhif = 200
service_charge = 100
deductions = nssf + nhif + service_charge + tax
net_salary = gross_salary - deductions

print(f"Basic salary is KSH. {basic_salary}")
print(f"Overtime hours worked: {overtime}")
print(f"Overtime pay earned: {rate}")
print(f"Gross salary is KSH. {gross_salary}")
print(f"PAYE on gross is KSH.{tax}")
print(f"Total deductions is KSH. {deductions}")
print(f"Net pay for this month is KSH. {net_salary}")


