total_gross_pay = 0
monthly_working_hour = 176 # 40h/week and 31days.
employee_base_salary = 2000 # In dollars.
get_bonus = False
vacation_reduction = 0
total_bonus = 0 # Initial bonus mount.
overtime_salary = 0
hourly_salary = 2000 // monthly_working_hour
overtime_hourly_salary = 2000 // monthly_working_hour * 1.25


## Step 1. The name of the salesperson - ok
employee_name = str(input("Enter employee\'s name >>> "))
if not (employee_name):
    print("*** Invalid input. Input will be set as 'Anonymous' ***\n")
    employee_name = "Anonymous"

## Step 2. Their base salary - ok
employee_work_hours = input("Enter employee\'s working hours for this month >>> ")
if ((employee_work_hours) and (float(employee_work_hours) >= 0)):
    employee_work_hours = float(employee_work_hours)
    if employee_work_hours > 176:
        overtime_salary = overtime_salary + (overtime_hourly_salary * (employee_work_hours - monthly_working_hour))
else:
    print("*** Invalid input. No negative numbers. Input will be set to 176 hours ***\n")
    employee_work_hours = 0

## Step 3. The commission earned (in Dollars). - ok
sales_commission_bonus = input("Enter employee\'s sales commission for this month >>> $")
if ((sales_commission_bonus) and (float(sales_commission_bonus) >=0)):
    sales_commission_bonus = float(sales_commission_bonus)
    if (sales_commission_bonus < 10000):
        sales_commission_bonus = 0
    elif ((10000 <= sales_commission_bonus) and (sales_commission_bonus <= 100000)):
        sales_commission_bonus = sales_commission_bonus * 2/100
    elif ((100001 <= sales_commission_bonus) and (sales_commission_bonus <= 500000)):
        sales_commission_bonus = sales_commission_bonus * 15/100
    elif ((500001 <= sales_commission_bonus) and (sales_commission_bonus <= 1000000)):
        sales_commission_bonus = sales_commission_bonus * 28/100
    elif (sales_commission_bonus > 1000000):
        sales_commission_bonus = sales_commission_bonus * 35/100
else:
    print("*** Invalid input. No negative numbers. Input will be set to 0 ***\n")
    sales_commission_bonus = 0

## Step 4. Their longevity with the company.
employee_longevity_bonus = input("Enter employee\'s longevity in month notation >>> ")
if ((employee_longevity_bonus) and (float(employee_longevity_bonus) >= 0)):
    employee_longevity_bonus = float(employee_longevity_bonus)
    if ((0 <= employee_longevity_bonus) and (employee_longevity_bonus < 3)):
        sales_commission_bonus = 0
        employee_longevity_bonus = 0
        total_bonus = 0
        get_bonus = False
    if employee_longevity_bonus >= 3:
        get_bonus = True
    if (employee_longevity_bonus >= 12*5) and (sales_commission_bonus >=1000000):
        total_bonus = total_bonus + 1000
else:
    print("*** Invalid input. No negative numbers. Input will be set to 0 ***\n")
    employee_longevity_bonus = 0


## Step 5. Check how many vacations the employee is taking.
days_of_vacation = input("Enter employee\'s days of vacation for this month >>> ")
if ((days_of_vacation) and (float(days_of_vacation) > 3)):
    days_of_vacation = float(days_of_vacation)
    vacation_reduction = -200
    total_bonus = total_bonus - 200
if ((days_of_vacation) and (float(days_of_vacation) < 3)):
    days_of_vacation = float(days_of_vacation)
else:
    print("*** Invalid input. No negative numbers. Input will be set to 0 ***\n")
    days_of_vacation = 0



### Print ###
total_bonus = total_bonus = total_bonus + sales_commission_bonus
total_gross_pay = employee_base_salary + days_of_vacation + total_bonus + overtime_salary
print("+----------------------------+------------------------------+")
print("+ PAYCHECK ------------------+------------------------------+")
print("+----------------------------+------------------------------+")
print("| Item                       | Value                         ")
print("+----------------------------+------------------------------+")
print("| Employee name              | ", employee_name)
print("| Employee work hours        | ", format(employee_work_hours, ".2f"))
print("| Vacation days              | ", days_of_vacation)
print("| Base salary                | $", format(employee_base_salary, ".2f"))
print("| Vacation reduction         | $", format(vacation_reduction, ".2f"))
print("| sales commission bonus     | $", format(sales_commission_bonus, ".2f"))
print("| Overtime salary            | $", format(overtime_salary, ".2f"))
print("| Total bonus                | $", format(total_bonus, ".2f"))
print("| Total gross pay            | $", format(total_gross_pay, ".2f"))
print("+----------------------------+------------------------------+")
