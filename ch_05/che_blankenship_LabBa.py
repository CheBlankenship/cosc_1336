# from modules import *
import modules

# Miles to km
m2k = input("William, please tell me how many miles you want to convert to kilometers >>> ")
mTokm = modules.milesToKm(m2k)
print(mTokm)

# F to C
if modules.checker(modules.counter):
    f2c = input("William, please tell me how much faherenhit you want to convert to celsius >>> ")
    # Pass the input value into the function parameter.
    fToc = modules.FahToCel(f2c)
    print(fToc)

# Gal to L
if modules.checker(modules.counter):
    galToL = input("William, please tell me how many gallons you want to convert to liters >>> ")
    # Pass the input value into the function parameter.
    gTol = modules.GalToLit(galToL)
    print(gTol)

# Lbs to kg
if modules.checker(modules.counter):
    poundToKg = input("William, please tell me how many pounds you want to convert to kilograms >>> ")
    # Pass the input value into the function parameter.
    ptok = modules.PoundsToKg(poundToKg)
    print(ptok)

# Inches to cm
if modules.checker(modules.counter):
    inchesToCm = input("William, please tell me how many inches you want to convert to centimeters >>> ")
    # Pass the input value into the function parameter.
    itoc = modules.InchesToCm(inchesToCm)
    print(itoc)
