# Grades
grade_a = 90 # Over 90
grade_b = 80 # Over 80
grade_c = 70 # Over 70
grade_d = 60 # Over 60
grade_e = 50 # Over 50
num_of_students = 0 # Counter
total_score     = 0

# Expect the input value which can be converted into type float.
score = float(input("Enter your score. Or enter -1 to stop the program. \n>>> "))

while (score != -1):
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

    score = float(input("Enter your score. Or enter -1 to stop the program. \n>>> "))

# At the end of the program calculate a class average unless there were NO grades entered.
if (num_of_students):
    print("---------------------+-------------------------")
    print("| Average score      |", total_score // num_of_students)
    print("| Number of grades   |", num_of_students)
    print("---------------------+-------------------------")
