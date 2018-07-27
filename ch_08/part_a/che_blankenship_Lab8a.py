# This is a program that converts to a specific unit.
# It will check
# 1, If the input is valid.
# 2, If the input is enable to convert into type float().
# 3, If the input is larger than 0 (1 ~ 4).
# 4, If the input is larger than 1000 (5).
# 5, How many times the user entered a invalid input.
#    If the user enters a invalid input more than 3 times,
#    the program will terminate.

counter = 1 # Add +1 everytime the user enters a invalid input.
nums    = "0123456789" # Expect input charactors to be in nums.



## 1, Mil to Km ##
while counter < 4:
    milesToKm = input("William, please tell me how many miles you want to convert to kilometers >>> ")
    # Check if the input is valid or not.
    if (milesToKm):
        # Check if the input chars are only in nums.
        # Success case: Best, Avg, Worst -> O(n).
        # Negative case: Best->O(1), Avg->O(n/2), Worst->O(n)
        valid_num = True
        for i in milesToKm:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and not(float(milesToKm) < 0)):
            milesToKm = float(milesToKm)
            # print(format(milesToKm, ".2f"), " mil is equal to ", format(milesToKm * 1.6, ".2f"), " km. \n\n")
            counter = 5
        else:
            print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
            counter = counter + 1
    else:
        print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
        counter = counter + 1
# Reset.
if counter == 5:
    counter = 1



## 2, Gal to L ##
while counter < 4:
    galToL = input("William, please tell me how many gallons you want to convert to liters >>> ")
    # Check if the input is valid or not.
    if (galToL):
        # Check if the input chars are only in nums.
        # Success case: Best, Avg, Worst -> O(n).
        # Negative case: Best->O(1), Avg->O(n/2), Worst->O(n)
        valid_num = True
        for i in galToL:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and not(float(galToL) < 0)):
            galToL = float(galToL)
            # print(format(galToL, ".2f"), " gal is equal to ", format(galToL * 3.9, ".2f"), " L. \n\n")
            counter = 5
        else:
            print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
            counter = counter + 1
    else:
        print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
        counter = counter + 1
# Reset.
if counter == 5:
    counter = 1



## 3, Lb to Kg ##
while counter < 4:
    poundToKg = input("William, please tell me how many pounds you want to convert to kilograms >>> ")
    # Check if the input is valid or not.
    if (poundToKg):
        # Check if the input chars are only in nums.
        # Success case: Best, Avg, Worst -> O(n).
        # Negative case: Best->O(1), Avg->O(n/2), Worst->O(n)
        valid_num = True
        for i in poundToKg:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and not(float(poundToKg) < 0)):
            poundToKg = float(poundToKg)
            # print(format(poundToKg, ".2f"), " pound is equal to ", format(poundToKg * 0.45, ".2f"), " kg. \n\n")
            counter = 5
        else:
            print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
            counter = counter + 1
    else:
        print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
        counter = counter + 1
# Reset.
if counter == 5:
    counter = 1



## 4, Inch to cm ##
while counter < 4:
    inchesToCm = input("William, please tell me how many inches you want to convert to centimeters >>> ")
    # Check if the input is valid or not.
    if (inchesToCm):
        # Check if the input chars are only in nums.
        # Success case: Best, Avg, Worst -> O(n).
        # Negative case: Best->O(1), Avg->O(n/2), Worst->O(n)
        valid_num = True
        for i in inchesToCm:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and not(float(inchesToCm) < 0)):
            inchesToCm = float(inchesToCm)
            # print(format(inchesToCm, ".2f") + " inch is equal to " + format(inchesToCm * 2.54, ".2f") + " cm. \n\n")
            counter = 5
        else:
            print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
            counter = counter + 1
    else:
        print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
        counter = counter + 1
# Reset.
if counter == 5:
    counter = 1



## 5, F to C ##
while counter < 4:
    fToC = input("William, please tell me how much faherenhit you want to convert to celsius >>> ")
    # Check if the input is valid or not.
    if (fToC):
        # Check if the input chars are only in nums.
        # Success case: Best, Avg, Worst -> O(n).
        # Negative case: Best->O(1), Avg->O(n/2), Worst->O(n)
        valid_num = True
        for i in fToC:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and  not(float(fToC) < 1000)):
            fToC = float(fToC)
            # print(format(fToC, ".2f") + " F is equal to " + format(((fToC - 32) * 5 // 9), ".2f") + " C. \n\n")
            counter = 5
        else:
            print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
            counter = counter + 1
    else:
        print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
        counter = counter + 1
# Reset.
if counter == 5:
    counter = 1



## Ask user's name and email address ##
while True:
    try:
        user_name = input("Enter your name >>> ")
        assert True
        assert len(user_name) > 0
        while True:
            try:
                user_email = input("Enter your email address >>> ")
                assert ("@" in user_email) and (len(user_email) > 1)
                # and (".com" in user_email)
                print(format(galToL, ".2f"), " gal is equal to ", format(galToL * 3.9, ".2f"), " L. \n")
                print(format(galToL, ".2f"), " gal is equal to ", format(galToL * 3.9, ".2f"), " L. \n")
                print(format(poundToKg, ".2f"), " pound is equal to ", format(poundToKg * 0.45, ".2f"), " kg. \n")
                print(format(inchesToCm, ".2f") + " inch is equal to " + format(inchesToCm * 2.54, ".2f") + " cm. \n")
                print(format(fToC, ".2f") + " F is equal to " + format(((fToC - 32) * 5 // 9), ".2f") + " C. \n")
            except AssertionError:
                print("Assertion error : Invalid input. Check if you have '@' in your email address.")
    except AssertionError:
        print("Assertion error : Invalid input.")
