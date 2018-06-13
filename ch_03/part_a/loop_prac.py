avg_num = int(input("Enter a number >> "))
sum = 0
count = 0

while not avg_num == 9999:
    sum = sum + avg_num
    count = count + 1
    avg_num = int(input("Enter a number. If you want to exit, enter 9999. \n>>> "))


print("Average >> ", sum / count)
