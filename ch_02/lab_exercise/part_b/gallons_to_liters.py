## Part A : c ##
# Gallons to Liters
# G = 3.9 * L
again = 'y'
while again == 'y':
    try:
        input_var = float(input("Enter a number >> ")) # input value
        print("Convert ", input_var, "Gallon to Litters.")
        print("Result >>> %10.2f L." % (3.9 * input_var))
    # Pick up false cases
    except:
        print("Invalid input. Try again.")
        continue

    again = input('Do you want to  continue with another conversion? y or n: ')
