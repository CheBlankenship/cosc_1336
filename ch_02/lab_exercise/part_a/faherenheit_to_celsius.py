## Part A : b ##
# Convert Miles to Kilometers
# C = (F - 32) * 5 / 9
again = 'y'
while again == 'y':
    try:
        input_var = input("Enter a number >> ") # input value
        print("Convert ", input_var, "F to C.")
        print("Result >>> %10.2f C." % (((int(input_var) * 5) * 5 // 9)))
    # Pick up false cases
    except:
        print("Invalid input. Try again.")
        continue

    again = input('Do you want to  continue with another conversion? y or n: ')
