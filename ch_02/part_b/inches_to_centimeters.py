## Part A : e ##
# Inches to Centimeters
# Inch = 2.54 * cm
again = 'y'
while again == 'y':
    try:
        input_var = float(input("Enter a number >> ")) # input value
        print("Convert ", input_var, "Inches to Centimeters.")
        print("Result >>> %10.2f cm." % (2.54 * input_var))
    # Pick up false cases
    except:
        print("Invalid input. Try again.")
        continue

    again = input('Do you want to  continue with another conversion? y or n: ')
