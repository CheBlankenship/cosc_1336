total_gross_pay = 0         # total
employee_base_salary = 2000 # In dollars.
get_bonus = False           # True or False based on
vacation_reduction = 0      # $-200 if the employee take more than 3 days off.
total_bonus = 0             # Initial bonus mount.
days_of_vacation = 0

## Step 1. The name of the salesperson - ok
employee_name = str(input("Enter employee\'s name \n>>> "))
# Invalid input.
if not (employee_name):
    print("*** Invalid input. Input will be set as 'Anonymous' ***\n")
    employee_name = "Anonymous"

## Step 2. Their base salary - ok
employee_work_hours = input("Enter employee\'s working hours for this month \n>>> ")
if ((employee_work_hours) and (float(employee_work_hours) >= 0)):
    employee_work_hours = float(employee_work_hours)
# Invalid input.
else:
    print("*** Invalid input. No negative numbers. Input will be set to 176 hours ***\n")
    employee_work_hours = 176

## Step 3. The commission earned (in Dollars). - ok
sales_commission_bonus = input("Enter employee\'s sales commission for this month \n>>> $")
if ((sales_commission_bonus) and (float(sales_commission_bonus) >=0)):
    sales_commission_bonus = float(sales_commission_bonus)
    # If commission rate is less than 10000.
    if (sales_commission_bonus < 10000):
        sales_commission_bonus = 0
    # If commission rate is between 10000 and 100000.
    elif ((10000 <= sales_commission_bonus) and (sales_commission_bonus <= 100000)):
        sales_commission_bonus = 0
    # If commission rate is between 100001 and 5000000.
    elif ((100001 <= sales_commission_bonus) and (sales_commission_bonus <= 500000)):
        sales_commission_bonus = 1000
    # If commission rate is between 5000001 and 1000000.
    elif ((500001 <= sales_commission_bonus) and (sales_commission_bonus <= 1000000)):
        sales_commission_bonus = 5000
    # If commission rate is more than 1000000.
    elif (sales_commission_bonus > 1000000):
        sales_commission_bonus = 10000
# Invalid input.
else:
    print("*** Invalid input. No negative numbers. Input will be set to 0 ***\n")
    sales_commission_bonus = 0

## Step 4. Their longevity with the company.
employee_longevity_bonus = input("Enter employee\'s longevity in month notation \n>>> ")
if (employee_longevity_bonus):
    if (float(employee_longevity_bonus) >= 0):
        employee_longevity_bonus = float(employee_longevity_bonus)
        # Case one: employee is working more than 3 month but didn't make commission more than 1000000.
        if (employee_longevity_bonus >= 3):
            get_bonus = True
        # Case two: employee is working more than 3 mo and made commission more than 1000000.
        if (employee_longevity_bonus >= 60) and (sales_commission_bonus >=1000000):
            get_bonus = True
            total_bonus = total_bonus + 1000
        # Case three: employee didn't work longer than 3 month.
        if(employee_longevity_bonus < 3):
            sales_commission_bonus = 0
            employee_longevity_bonus = 0
            total_bonus = 0
            get_bonus = False
# Invalid input.
else:
    print("*** Invalid input. No negative numbers. Input will be set to 0 ***\n")
    employee_longevity_bonus = 0


## Step 5. Check how many vacations the employee is taking.
days_of_vacation = input("Enter employee\'s days of vacation for this month \n>>> ")
# If the employee takes more than 3 days off.
if (days_of_vacation):
    if (float(days_of_vacation) >= 3):
        days_of_vacation = float(days_of_vacation)
        vacation_reduction = -200
        total_bonus = total_bonus - 200
        # If the employee takes less than 3 days.
        if (float(days_of_vacation) < 3):
            days_of_vacation = float(days_of_vacation)
# Invalid input.
else:
    print("*** Invalid input. No negative numbers. Input will be set to 0 ***\n")
    days_of_vacation = 0


print("COM Bounus > ", sales_commission_bonus)
### Print ###
total_bonus = total_bonus + sales_commission_bonus
total_gross_pay = employee_base_salary + total_bonus
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
print("| Total bonus                | $", format(total_bonus, ".2f"))
print("| Total gross pay            | $", format(total_gross_pay, ".2f"))
print("+----------------------------+------------------------------+")
