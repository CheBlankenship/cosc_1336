students = []

counter = 0

while counter < 12:
    try:
        assert True
        student_name = input("Enter student's name: ")
        assert len(student_name) > 0
        students.append(str(student_name))
        counter = counter + 1
    except AssertionError:
        print("Invalid input. Try again.")


print("Student name list: ", students)

def list_modification(arr):
    # 1, Sort the list in alphabetical order.
    arr.sort()
    print("Sort alphabetical: ", arr)
    # 2, Sort the list again in reverse order.
    arr.sort(reverse=True)
    print("Reverse: ", arr)
    # 3, Append the instructor’s name on the list.
    teacher_name = input("Instructor name: ")
    arr.append(str(teacher_name))
    # 4, Insert your own name at the beginning of the list.
    arr.insert(0, "Che Blankenship")
    # 5, Write the list to a file named “names.txt”.
    output_file = open("names.txt", "w+")
    for item in arr:
        output_file.write(item+"\n")
    output_file.close()
    #6, Display the contents of the file named :”names.txt”.
    input_file = open("names.txt", "r")
    print("names.txt content")
    print("-----------------")
    for item in input_file:
        print(item)
    input_file.close()
    #7, Convert the list to a Tuple.
    arr = tuple(arr)
    print("Convert list into tuple: ", arr)


list_modification(students)
