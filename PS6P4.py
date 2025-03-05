total_gross_pay = 0
employee_count = 0

response = input("Do you want to enter employee data? (Yes/No): ").strip().lower()

while response == "yes":
    last_name = input("Enter employee last name: ")
    hours_worked = float(input("Enter hours worked: "))
    pay_rate = float(input("Enter hourly pay rate: "))

    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours_worked * pay_rate

    print("Employee:", last_name)
    print("Gross Pay: $", round(gross_pay, 2))

    total_gross_pay += gross_pay
    employee_count += 1

    response = input("Do you want to enter another employee? (Yes/No): ").strip().lower()

average_pay = total_gross_pay / employee_count if employee_count > 0 else 0

print("Total Gross Pay: $", round(total_gross_pay, 2))
print("Number of Employees:", employee_count)
print("Average Pay: $", round(average_pay, 2))
