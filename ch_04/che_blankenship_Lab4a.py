counter = 1 # Add +1 everytime the user enters a invalid input.
nums    = "0123456789" # Expect input charactors to be in nums.



## Mil to Km ##
while counter < 4:
    milesToKm = input("William, please tell me how many miles you want to convert to kilometers >>> ")
    # Check if the input is valid or not.
    if (milesToKm):
        # Check if the input chars are only in nums : O(n)
        valid_num = True
        for i in milesToKm:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and not(float(milesToKm) < 0)):
            milesToKm = float(milesToKm)
            print(format(milesToKm, ".2f"), " mil is equal to ", format(milesToKm * 1.6, ".2f"), " km. \n\n")
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



## Gal to L ##
while counter < 4:
    galToL = input("William, please tell me how many gallons you want to convert to liters >>> ")
    # Check if the input is valid or not.
    if (galToL):
        # Check if the input chars are only in nums : O(n)
        valid_num = True
        for i in galToL:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and not(float(galToL) < 0)):
            galToL = float(galToL)
            print(format(galToL, ".2f"), " gal is equal to ", format(galToL * 3.9, ".2f"), " L. \n\n")
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



## Lb to Kg ##
while counter < 4:
    poundToKg = input("William, please tell me how many pounds you want to convert to kilograms >>> ")
    # Check if the input is valid or not.
    if (poundToKg):
        # Check if the input chars are only in nums : O(n)
        valid_num = True
        for i in poundToKg:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and not(float(poundToKg) < 0)):
            poundToKg = float(poundToKg)
            print(format(poundToKg, ".2f"), " pound is equal to ", format(poundToKg * 0.45, ".2f"), " kg. \n\n")
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



## Inch to cm ##
while counter < 4:
    inchesToCm = input("William, please tell me how many inches you want to convert to centimeters >>> ")
    # Check if the input is valid or not.
    if (inchesToCm):
        # Check if the input chars are only in nums : O(n)
        valid_num = True
        for i in inchesToCm:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and not(float(inchesToCm) < 0)):
            inchesToCm = float(inchesToCm)
            print(format(inchesToCm, ".2f") + " inch is equal to " + format(inchesToCm * 2.54, ".2f") + " cm. \n\n")
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



## F to C ##
while counter < 4:
    fToC = input("William, please tell me how much faherenhit you want to convert to celsius >>> ")
    # Check if the input is valid or not.
    if (fToC):
        # Check if the input chars are only in nums : O(n)
        valid_num = True
        for i in fToC:
            if i not in nums:
                valid_num = False
        # If the input is a number, process it.
        if (valid_num and  not(float(fToC) < 1000)):
            fToC = float(fToC)
            print(format(fToC, ".2f") + " F is equal to " + format(((fToC - 32) * 5 // 9), ".2f") + " C. \n\n")
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
