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
    print("- Options ------------------------------")
    print("| Miles to kilometer     :enter 'a'")
    print("| Gallons to liters      :enter 'b'")
    print("| Pounds to kilograms    :enter 'c'")
    print("| Inches to centimeters  :enter 'd'")
    print("| Fahrenheit to Celsius  :enter 'e'")
    print("+ Other option -------------------------")
    print("| Exit the program       :enter 'exit'")
    print("----------------------------------------\n")

    try:
        option = input("Enter the number for the converter you want to use >>> ")
        assert True
        assert option == 'a' or option == 'b' or option == 'c' or option == 'd' or option == 'e'

        count_num_of_convert = 0
        while True:

            if option == "a":
                while True:
                    try:
                        m2k = str(input("Please tell me how many MILES you want to convert to KILOMETERS >>> "))
                        # Check if the input can be convert into type float.
                        checker = float(m2k)
                        mTokm = modules.milesToKm(m2k)
                        print(mTokm)
                        if (mTokm):
                            input_file.write(mTokm+"\n")
                            count_num_of_convert += 1
                        if count_num_of_convert == 10:
                            quit()
                    except ValueError:
                        print("ValueError: Invalid input. No strings or negative numbers.\n")
                        if count_num_of_convert == 10:
                            quit()
                        else:
                            input_file.write("Invalid input."+"\n")
                            count_num_of_convert += 1
                            if count_num_of_convert == 10:
                                quit()
                            else:
                                continue


            if option == "b":
                while True:
                    try:
                        gal2L = str(input("Please tell me how many GALLONS you want to convert to LITERS >>> "))
                        # Check if the input can be convert into type float.
                        checker = float(gal2L)
                        galToLit = modules.GalToLit(gal2L)
                        print(galToLit)
                        if (galToLit):
                            input_file.write(galToLit+"\n")
                            count_num_of_convert += 1
                        if count_num_of_convert == 10:
                            quit()
                    except ValueError:
                        print("ValueError: Invalid input. No strings or negative numbers.\n")
                        if count_num_of_convert == 10:
                            quit()
                        else:
                            input_file.write("Invalid input."+"\n")
                            count_num_of_convert += 1
                            if count_num_of_convert == 10:
                                quit()
                            else:
                                continue


            if option == "c":
                while True:
                    try:
                        pound2Kg = str(input("Please tell me how many POUNDS you want to convert to KILOGRAMS >>> "))
                        # Check if the input can be convert into type float.
                        checker = float(pound2Kg)
                        pTokg = modules.PoundsToKg(pound2Kg)
                        print(pTokg)
                        if (pTokg):
                            input_file.write(pTokg+"\n")
                            count_num_of_convert += 1
                        if count_num_of_convert == 10:
                            quit()
                    except ValueError:
                        print("ValueError: Invalid input. No strings or negative numbers.\n")
                        if count_num_of_convert == 10:
                            quit()
                        else:
                            input_file.write("Invalid input."+"\n")
                            count_num_of_convert += 1
                            if count_num_of_convert == 10:
                                quit()
                            else:
                                continue


            if option == "d":
                while True:
                    try:
                        inches2Cm = str(input("Please tell me how many INCHES you want to convert to CENTIMETERS >>> "))
                        # Check if the input can be convert into type float.
                        checker = float(inches2Cm)

                        inchesToCm = modules.InchesToCm(inches2Cm)
                        print(inchesToCm)
                        if (inchesToCm):
                            input_file.write(inchesToCm+"\n")
                            count_num_of_convert += 1
                        if count_num_of_convert == 10:
                            quit()
                    except ValueError:
                        print("ValueError: Invalid input. No strings or negative numbers.\n")
                        if count_num_of_convert == 10:
                            quit()
                        else:
                            input_file.write("Invalid input."+"\n")
                            count_num_of_convert += 1
                            if count_num_of_convert == 10:
                                quit()
                            else:
                                continue


            if option == "e":
                while True:
                    try:
                        f2c = str(input("Please tell me how much FAHERENHIT you want to convert to CELSIUS >>> "))
                        # Check if the input can be convert into type float.
                        checker = float(f2c)

                        fToc = modules.FahToCel(f2c)
                        print(fToc)
                        if (fToc):
                            input_file.write(fToc+"\n")
                            count_num_of_convert += 1
                        if count_num_of_convert == 10:
                            quit()
                    except ValueError:
                        print("ValueError: Invalid input. No strings or negative numbers.\n")
                        if count_num_of_convert == 10:
                            quit()
                        else:
                            input_file.write("Invalid input."+"\n")
                            count_num_of_convert += 1
                            if count_num_of_convert == 10:
                                quit()
                            else:
                                continue



    except AssertionError:
        if option != "exit":
            print("AssertionError: Invalid input. Enter 'a', 'b', 'c', 'd' or 'e'.\n")
            continue
        else:
            exit()

    input_file.close()
