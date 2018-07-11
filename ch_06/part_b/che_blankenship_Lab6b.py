import sys

input_file = open("grades.txt", "a+")

counter = 0
while True:

    # Student name
    try:
        assert True
        student_name = str(input("Enter students name : "))
        assert len(student_name) > 0

        ## Student grade ##
        try:
            assert True
            student_grade = float(input("Enter students grade : "))
            assert 0 <= student_grade <= 100

            # Chack if both student_name and student_grade are valid.
            try:
                if (student_name) and (student_grade):
                    counter = counter + 1
                    input_file.write("Student name: "+ str(student_name) + ", Grade: " + str(student_grade) + ".\n")
                    if counter >= 12:
                        break
            except NameError:
                print("* NameError: Student name or student grade is invalid .\n* Please start over again.\n")
            ## close input validation error handling ##
        except AssertionError:
            print("AssertionError: Student grade should be between 0 ~ 100.\n* Please start over again.\n")
        except ValueError:
            print("ValueError: Could not convert student grade to type float.\n* Please start over again.\n")
        except NameError:
            print("NameError: Student grade is undefined.\n* Please start over again.\n")
        ## close student grade err handling ##

    except AssertionError:
        print("AssertionError: Invalid student name. Enter a valid input.")
    ## close student name error handling ##



input_file.close()



# Open file, read file, display data.
try:
    read_file = open("grades.txt", "r")
    with read_file as f:
        lines = f.readlines()
        for line in lines:
            print(line)
except IOError:
    print ("Could not read file:", read_file)
except NameError:
    print("NameError: File name not found.")
except: #handle other exceptions such as attribute errors
   print ("Unexpected error:", sys.exc_info()[0])
