gross_pay               = 0     # total.
employee_base_salary    = 2000  # Base salary in dollars.
vacation_reduction      = 0     # -$200 if the employee take more than 3 days .
total_bonus             = 0     # Initial bonus amount.
sales_commission        = 0     # Sales commission
sales_bonus             = 0     # Bonus based on your sales record.


## Step 1. The name of the salesperson.
employee_name = str(input("Enter employee\'s name \n>>> "))
# Invalid input.
if not (employee_name):
    print("*** Invalid input. Employee\'s name will be set to 'Anonymous' ***\n")
    employee_name = "Anonymous"


## Step 2. The commission and bonus base on the sales amount (in Dollars).
sales = input("Enter the amount of sales which the employee made for this month \n>>> $")
if (sales):
    if (float(sales) >=0):
        sales = float(sales)
        # If: commission rate is less than 10000.
        if (sales < 10000):
            sales_commission = 0
            sales_bonus = 0
        # If: commission is more than 10000
        if(sales >= 10000):
            sales_commission = (sales * (2 / 100))
            sales_bonus =  0
            # If: commission is more than 100000
            if(sales >= 100001):
                sales_commission = (sales * (15 / 100))
                sales_bonus = 1000
                # If: commission is more than 500000
                if (sales >= 500001):
                    sales_commission = (sales * (28 / 100))
                    sales_bonus = 5000
                    # If: commission is more than 1000000
                    if (sales > 1000000):
                        sales_commission = (sales * (35 / 100))
                        sales_bonus = 100000
    # Invalid input.
    else:
        print("*** Invalid input. No negative numbers. Commission will be set to 0 ***\n")
        commission_and_bonus = 0
# Invalid input.
else:
    print("*** Invalid input. No negative numbers. Commission will be set to 0 ***\n")
    commission_and_bonus = 0


## Step 3. Their longevity with the company.
employee_longevity_bonus = input("Enter employee\'s longevity in month notation \n>>> ")
if (employee_longevity_bonus):
    if (float(employee_longevity_bonus) >= 0):
        employee_longevity_bonus = float(employee_longevity_bonus)
        # Case one: employee is working more than 3 month but didn't make commission more than 1000000.
        if (employee_longevity_bonus >= 3):
            # Case two: employee is working more than 3 mo and made commission more than 1000000.
            if (employee_longevity_bonus >= 60):
                if (sales >=100000):
                    total_bonus = total_bonus + 1000
        # Case three: employee didn't work longer than 3 month.
        else:
            commission_and_bonus = 0
            employee_longevity_bonus = 0
            total_bonus = 0
            # get_bonus = False
    # Invalid input.
    else:
        print("*** Invalid input. No negative numbers. Longevity will be set to 0 ***\n")
        employee_longevity_bonus = 0
# Invalid input.
else:
    print("*** Invalid input. No negative numbers. Longevity will be set to 0 ***\n")
    employee_longevity_bonus = 0


## Step 4. Check how many vacations the employee is taking.
days_of_vacation = input("Enter employee\'s days of vacation for this month \n>>> ")
if (days_of_vacation):
    # Check if the input is not a negative number or not.
    days_of_vacation = float(days_of_vacation)
    if (days_of_vacation >= 0):
        # If the employee takes off more than 3 days.
        if (days_of_vacation >= 3):
            vacation_reduction = -200
    # Invalid input.
    else:
        print("*** Invalid input. No negative numbers. Input will be set to 0 ***\n")
        days_of_vacation = 0
# Invalid input.
else:
    print("*** Invalid input. No negative numbers. Input will be set to 0 ***\n")
    days_of_vacation = 0



### Print ###
# Sum all the values.
total_bonus = total_bonus + sales_bonus + sales_commission + vacation_reduction
gross_pay = employee_base_salary + total_bonus
print("+----------------------------+------------------------------+")
print("+ PAYSTUB -------------------+------------------------------+")
print("+----------------------------+------------------------------+")
print("| Item                       | Value                         ")
print("+----------------------------+------------------------------+")
print("| Employee name              | ", employee_name)
print("| Vacation days              | ", days_of_vacation, "days")
print("| Base salary                | $", format(employee_base_salary, ".2f"))
print("| Sales commission           | $", format(sales_commission, ".2f"))
print("| Sales bonus                | $", format(sales_bonus, ".2f"))
print("| Vacation reduction         | $", format(vacation_reduction, ".2f"))
print("| Total bonus                | $", format(total_bonus, ".2f"))
print("| Gross pay                  | $", format(gross_pay, ".2f"))
print("+----------------------------+------------------------------+")
