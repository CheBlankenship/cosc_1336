# nums    = "0123456789" # Expect input charactors to be in nums.
# counter = 1

# Check the counter status.
# def checker(counter):
#     return counter < 4
    # Pass the input value into the function parameter.

## 1, Mil to Km ##
def milesToKm(m2k):
    try:
        # Check if the input can be convert into type float.
        checker = float(m2k)
        # Expect var checker is larger than or eql to 0.
        assert True
        assert checker >= 0
        m2k = float(m2k)
        result = format(m2k, ".2f") + " mil is equal to " + format(m2k * 1.6, ".2f") + " km."
        return result
    except AssertionError:
        print("AssertionError: Your input is smaller than 0. No negative numbers.")
        return None
    else:
        print("Unexpected Error.")
        return None


## 2, F to C ##
def FahToCel(f2c):
    try:
        # Check if the input can be convert into type float.
        checker = float(f2c)
        # Expect var checker is larger than or eql to 1000.
        assert True
        assert checker >= 1000
        f2c = float(f2c)
        return format(f2c, ".2f") + " F is equal to " + format(((f2c - 32) * 5 // 9), ".2f") + " C."
    except AssertionError:
        print("AssertionError: Your input is smaller than 0. No negative numbers.")
        return None
    else:
        print("Unexpected Error.")
        return None



    # global counter
    # while counter < 4:
    #     # Check if the input is valid or not.
    #     if (f2c):
    #         valid_num = True
    #         for i in f2c:
    #             if i not in nums:
    #                 valid_num = False
    #         # If the input is a number, process it.
    #         if (valid_num and  not(float(f2c) < 1000)):
    #             f2c = float(f2c)
    #             counter = 1
    #             return format(f2c, ".2f") + " F is equal to " + format(((f2c - 32) * 5 // 9), ".2f") + " C."
    #         else:
    #             print("Error: Invalid input. No negative numbers and charactors. Input needs to be larger than 1000.\n")
    #             counter = counter + 1
    #             if counter < 4:
    #                 f2c = input("William, please tell me how much faherenhit you want to convert to celsius >>> ")
    #     else:
    #         print("Error: Invalid input. No negative numbers and charactors. Input needs to be larger than 1000.\n")
    #         counter = counter + 1
    #         if counter < 4:
    #             f2c = input("William, please tell me how much faherenhit you want to convert to celsius >>> ")



## 3, Gal to L ##
def GalToLit(galToL):

    try:
        # Check if the input can be convert into type float.
        checker = float(galToL)
        # Expect var checker is larger than or eql to 1000.
        assert True
        assert checker >= 0
        galToL = float(galToL)
        return format(galToL, ".2f") + " gal is equal to " + format(galToL * 3.9, ".2f") + " L."
    except AssertionError:
        print("AssertionError: Your input is smaller than 0. No negative numbers.")
        return None
    else:
        print("Unexpected Error.")
        return None

    # global counter
    # while counter < 4:
    #     # Check if the input is valid or not.
    #     if (galToL):
    #         valid_num = True
    #         for i in galToL:
    #             if i not in nums:
    #                 valid_num = False
    #         # If the input is a number, process it.
    #         if (valid_num and not(float(galToL) < 0)):
    #             galToL = float(galToL)
    #             counter = 1
    #             return format(galToL, ".2f") + " gal is equal to " + format(galToL * 3.9, ".2f") + " L."
    #         else:
    #             print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
    #             counter = counter + 1
    #             if counter < 4:
    #                 galToL = input("William, please tell me how many gallons you want to convert to liters >>> ")
    #     else:
    #         print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
    #         counter = counter + 1
    #         if counter < 4:
    #             galToL = input("William, please tell me how many gallons you want to convert to liters >>> ")



## 4, Lb to Kg ##
def PoundsToKg(poundToKg):

    try:
        # Check if the input can be convert into type float.
        checker = float(poundToKg)
        # Expect var checker is larger than or eql to 1000.
        assert True
        assert checker >= 0
        poundToKg = float(poundToKg)
        return format(poundToKg, ".2f") + " pound is equal to " + format(poundToKg * 0.45, ".2f") + " kg."
    except AssertionError:
        print("AssertionError: Your input is smaller than 0. No negative numbers.")
        return None
    else:
        print("Unexpected Error.")
        return None


    # global counter
    # while counter < 4:
    #     # Check if the input is valid or not.
    #     if (poundToKg):
    #         valid_num = True
    #         for i in poundToKg:
    #             if i not in nums:
    #                 valid_num = False
    #         # If the input is a number, process it.
    #         if (valid_num and not(float(poundToKg) < 0)):
    #             poundToKg = float(poundToKg)
    #             counter = 1
    #             return format(poundToKg, ".2f") + " pound is equal to " + format(poundToKg * 0.45, ".2f") + " kg."
    #         else:
    #             print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
    #             counter = counter + 1
    #             if counter < 4:
    #                 poundToKg = input("William, please tell me how many pounds you want to convert to kilograms >>> ")
    #     else:
    #         print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
    #         counter = counter + 1
    #         if counter < 4:
    #             poundToKg = input("William, please tell me how many pounds you want to convert to kilograms >>> ")



## 5, Inch to cm ##
def InchesToCm(inchesToCm):

    try:
        # Check if the input can be convert into type float.
        checker = float(inchesToCm)
        # Expect var checker is larger than or eql to 1000.
        assert True
        assert checker >= 0
        inchesToCm = float(inchesToCm)
        return format(inchesToCm, ".2f") + " inch is equal to " + format(inchesToCm * 2.54, ".2f") + " cm."
    except AssertionError:
        print("AssertionError: Your input is smaller than 0. No negative numbers.")
        return None
    else:
        print("Unexpected Error.")
        return None

    # global counter
    # while counter < 4:
    #     # Check if the input is valid or not.
    #     if (inchesToCm):
    #         valid_num = True
    #         for i in inchesToCm:
    #             if i not in nums:
    #                 valid_num = False
    #         # If the input is a number, process it.
    #         if (valid_num and not(float(inchesToCm) < 0)):
    #             inchesToCm = float(inchesToCm)
    #             counter = 1
    #             return format(inchesToCm, ".2f") + " inch is equal to " + format(inchesToCm * 2.54, ".2f") + " cm."
    #         else:
    #             print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
    #             counter = counter + 1
    #             if counter < 4:
    #                 inchesToCm = input("William, please tell me how many inches you want to convert to centimeters >>> ")
    #     else:
    #         print("Error: Invalid input. No negative numbers and charactors. Only positive numbers.\n")
    #         counter = counter + 1
    #         if counter < 4:
    #             inchesToCm = input("William, please tell me how many inches you want to convert to centimeters >>> ")
