salary = 50000
exper = 5



# Solution one
if (salary > 50000) and (exper > 5):
    print("You are qualified!")
else:
    print("You arn't qualifies")


# Solution Two
if (salary > 50000):
    if (exper > 5):
        print("Qualified!")
else:
    print("Not qualified.")
