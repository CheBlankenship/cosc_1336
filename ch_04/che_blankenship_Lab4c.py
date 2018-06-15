# Grades
grade_a = 90 # Over 90
grade_b = 80 # Over 80
grade_c = 70 # Over 70
grade_d = 60 # Over 60
grade_e = 50 # Over 50
num_of_students = 0 # Counter
total_score     = 0


score = input("Enter student's score. Or enter -1 to stop. \n>>> ")
# Handle if the vlue is a valid input and enable to conver into type float.
if ((score) and (float == type(float(score)))):
    print("check >>> ")
    if ((score) and (float == type(float(score)))):
        score = float(score)
        while score != -1:
            num_of_students = num_of_students + 1
            if score >= grade_a:
                print('Congratulations! Your grade is A.')
                total_score = total_score + score
            else:
                if score >= grade_b:
                    print('Your grade is B. Good job!')
                    total_score = total_score + score
                else:
                    if score >= grade_c:
                        print('Your grade is C. Soso.')
                        total_score = total_score + score
                    else:
                        if score >= grade_d:
                            print('Your grade is D...')
                            total_score = total_score + score
                        else:
                            print('You made an F! Obviously you did not study.')
                            total_score = total_score + score
            score = float(input("Enter your score. \n>>> "))
            # If input score is invalid and not able to convert into float, it will exit.
            if not ((score) and (float == type(float(score)))):
                print("Error: Invalid input. No charactors. Only numbers. ")
        print("-----------------------------------------------")
        print("Number of students   >> ", num_of_students, "students")
        print("Total score          >> ", total_score)
        print("Average score        >> ", total_score // num_of_students)
        print("-----------------------------------------------")
    else:
        print("Error: Invalid input. No charactors. Only numbers. ")
else:
    print("Error: Invalid input. No charactors. Only numbers. ")
