# Part A - a - i
# Convert Miles to Kilometers
# If the user input is negative number, it will print a error message and exit.
milesToKm = float(input("William, please tell me how many miles you want to convert to kilometers >>> "))
if not(milesToKm < 0):
    print(str(milesToKm) + " mil is equal to " + str(milesToKm * 1.6) + " km. ")
    galToL = float(input("William, please tell me how many gallons you want to convert to liters >>> "))
    if not(galToL < 0):
        print(str(galToL) + " gal is equal to " + str(galToL * 3.9) + " L. ")
        poundToKg = float(input("William, please tell me how many pounds you want to convert to kilograms >>> "))
        if not(poundToKg < 0):
            print(str(poundToKg) + " pound is equal to " + str(poundToKg * 0.45) + " kg. ")
            inchesToCm = float(input("William, please tell me how many inches you want to convert to centimeters >>> "))
            if not(inchesToCm < 0):
                print(str(inchesToCm) + " inch is equal to " + str(inchesToCm * 2.54) + " cm. ")
                fToC = float(input("William, please tell me how much faherenhit you want to convert to celsius >>> "))
                if not (fToC > 1000):
                    print(str(fToC) + " F is equal to " + str(((fToC - 32) * 5 // 9)) + " C. ")
