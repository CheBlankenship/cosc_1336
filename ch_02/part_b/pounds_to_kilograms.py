## Part A : d ##
# Pounds to Kilograms
# P = 0.45 * K
again = 'y'
while again == 'y':
    try:
        input_var = float(input("Enter a number >> ")) # input value
        print("Convert ", input_var, "Pounds to Kilograms.")
        print("Result >>> %10.2f kg." % (0.45 * input_var))
    # Pick up false cases
    except:
        print("Invalid input. Try again.")
        continue

    again = input('Do you want to  continue with another conversion? y or n: ')
