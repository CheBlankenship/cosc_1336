## Part A : a ##
# Convert Miles to Kilometers
# One mile = 1.6 km
again = 'y'
while again == 'y':
    try:
        input_var = input("Enter a number >> ") # input value
        print("Convert ", input_var, "miles to kilometers.")
        print("Result >>> ", int(input_var) * 1.6, " kilometers.")
    # Pick up false cases
    except:
        print("Invalid input. Try again.")
        continue

    again = input('Do you want to  continue with another conversion? y or n: ')
