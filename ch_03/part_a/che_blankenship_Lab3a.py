# Part A - a - i
# Convert Miles to Kilometers
# If the user input is negative number, it will print a error message and exit.
milesToKm = float(input("William, please tell me how many miles you want to convert to kilometers >>> "))
if not(milesToKm < 0):
    print("William, " + str(milesToKm) + " mil is equal to " + str(milesToKm * 1.6) + " km. ")
else:
    print("Error: Invalid input! No negative numbers.")

# Part A - a - ii
# Gallons to Liters
# If the user input is negative number, it will print a error message and exit.
galToL = float(input("William, please tell me how many gallons you want to convert to liters >>> "))
if not(galToL < 0):
    print("William, " + str(galToL) + " gal is equal to " + str(galToL * 3.9) + " L. ")
else:
    print("Error: Invalid input! No negative numbers.")

# Part A - a - iii
# Pounds to Kilograms
# If the user input is negative number, it will print a error message and exit.
poundToKg = float(input("William, please tell me how many pounds you want to convert to kilograms >>> "))
if not(poundToKg < 0):
    print("William, " + str(poundToKg) + " pound is equal to " + str(poundToKg * 0.45) + " kg. ")
else:
    print("Error: Invalid input! No negative numbers.")

# Part a - a - iv
# Inches to Centimeters
inchesToCm = float(input("William, please tell me how many inches you want to convert to centimeters >>> "))
if not(inchesToCm < 0):
    print("William, " + str(inchesToCm) + " inch is equal to " + str(inchesToCm * 2.54) + " cm. ")
else:
    print("Error: Invalid input! No negative numbers.")

# Part A - b
# Convert Faherenhit to Celsius
# If the user input is above 1000, it will print a error message and exit.
fToC = float(input("William, please tell me how much faherenhit you want to convert to celsius >>> "))
if fToC > 1000:
    print("Error: Invalid input! Input needs to be smaller than 1000.")
else:
    print("William, " + str(fToC) + " F is equal to " + str(((fToC - 32) * 5 // 9)) + " C. ")
