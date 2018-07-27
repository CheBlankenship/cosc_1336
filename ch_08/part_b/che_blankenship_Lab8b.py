months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    try:
        assert True
        date = input("Enter a date in numeric date format (mm/dd/yy): ")
        if not "/" in date:
            mdy = []
            mdy.append(date[:2])
            mdy.append(date[2:4])
            mdy.append(date[4:])
            print(mdy)
        else:
            mdy = date.split("/")
            print(mdy)

        # Check if month, day and year are valid.
        month = int(mdy[0])
        day = int(mdy[1])
        year = int(mdy[2])

        assert 1 <= month <= 12
        assert 1 <= day <= 31
        assert year == 15
        print(str(months[month-1])+" "+str(day)+", 20"+str(year))
        exit()
    except AssertionError:

        print("Invalid input. Day must be between 1~31. Month must be between 1~12. Year must be 2015('15').")
