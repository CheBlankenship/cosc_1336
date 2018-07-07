## Note ##
# 1, The program will ask you for a valid input
#   for ever until you enter a valid input.
# 2, If will ask you ten times to enter a valid input.
#   However, if you input a invalid input three times
#



# import modules.py file which has all the converter functions.
import modules

# Using the while loop so it doesn't exit.
# It will keep asking the input till the user enters a valid input.
while True: # infinit

    input_file = open("conversions.txt", "w+")
    print("- Options ----------------------------")
    print("| Miles to kilometer     :enter 'a'")
    print("| Gallons to liters      :enter 'b'")
    print("| Pounds to kilograms    :enter 'c'")
    print("| Inches to centimeters  :enter 'd'")
    print("| Fahrenheit to Celsius  :enter 'e'")
    print("------------------------------------\n")

    try:
        option = input("Enter the number for the converter you want to use >>> ")
        assert True
        assert option == 'a' or option == 'b' or option == 'c' or option == 'd' or option == 'e'

        for _ in range(10):

            if option == "a":
                print("Current counter sta >> ", modules.counter)
                while True:
                    try:
                        m2k = str(input("Please tell me how many MILES you want to convert to KILOMETERS >>> "))
                        m2k = int(m2k)
                        if (m2k):
                            mTokm = modules.milesToKm(m2k)
                            print(mTokm)
                            input_file.write(mTokm+"\n")
                    except ValueError:
                        print("ValueError: Invalid input. Only numbers.\n")
                        continue

            # if option == "b":
            #     galToL = str(input("Please tell me how many GALLONS you want to convert to LITERS >>> "))
            #     if (galToL):
            #         gTol = modules.GalToLit(galToL)
            #         print(gTol)
            #         input_file.write(galToL+"\n")
            #
            # if option == "c":
            #     poundToKg = str(input("Please tell me how many POUNDS you want to convert to KILOGRAMS >>> "))
            #     if (poundToKg):
            #         ptok = modules.PoundsToKg(poundToKg)
            #         print(ptok)
            #         input_file.write(ptok+"\n")
            #
            # if option == "d":
            #     inchesToCm = str(input("Please tell me how many INCHES you want to convert to CENTIMETERS >>> "))
            #     if (inchesToCm):
            #         itoc = modules.InchesToCm(inchesToCm)
            #         print(itoc)
            #         input_file.write(itoc+"\n")
            #
            # if option == "e":
            #     f2c = str(input("Please tell me how much FAHERENHIT you want to convert to CELSIUS >>> "))
            #     if (f2c):
            #         fToc = modules.FahToCel(f2c)
            #         print(fToc)
            #         input_file.write(f2c+"\n")

            # It will call quit to exit the program when _ reaches 9.
            if _ == 9:
                quit()

    except AssertionError as err:
        print("AssertionError: Invalid input. Enter 'a', 'b', 'c', 'd' or 'e'.\n")
        continue
    # except ValueError as error:
    #     print("ERROR:",error,"\n")
    # except EOFError as err:
    #     print(err)
    # except IOError as err:
    #     print(err)
    # finally:
    #     print("check")

    input_file.close()
