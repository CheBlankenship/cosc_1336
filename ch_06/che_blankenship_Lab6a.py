import modules

input_file = "conversion.txt"

for _ in range(4):

        try:
            inp = input("Choose the converter \nMiles to kilometer (enter '1') \nGallons to liters (enter '2') \nPounds to kilograms   (enter '3') \nInches to centimeters (enter '4') \nFahrenheit to Celsius (enter '5') \n>>> ")
            inp = int(inp)
            if inp == 1:
                m2k = str(input("Please tell me how many miles you want to convert to kilometers >>> "))
                if (m2k):
                    mTokm = modules.milesToKm(m2k)
                    print(mTokm)
                else:
                    print("check")

        except ValueError as error:
            print("ERROR:", error)
        except TypeError as error:
            print("ERROR:", error)
        finally:
            print("ERROR: No negative numbers! Or there is some error for your input. ")

    # if input == '2':
    #     print("check 2>> ")
    #     galToL = input("Please tell me how many gallons you want to convert to liters >>> ")
    #     gTol = modules.GalToLit(galToL)
    #     print(gTol)
    #
    # if input == '3':
    #     print("check 3>> ")
    #     poundToKg = input("Please tell me how many pounds you want to convert to kilograms >>> ")
    #     ptok = modules.PoundsToKg(poundToKg)
    #     print(ptok)
    #
    # if input == '4':
    #     print("check 4>> ")
    #     inchesToCm = input("Please tell me how many inches you want to convert to centimeters >>> ")
    #     itoc = modules.InchesToCm(inchesToCm)
    #     print(itoc)
    #
    # if input == '5':
    #     print("check 5>> ")
    #     f2c = input("Please tell me how much faherenhit you want to convert to celsius >>> ")
    #     fToc = modules.FahToCel(f2c)
    #     print(fToc)


#
# try:
#     pass
# except Exception as e:
#     raise
