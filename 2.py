from datetime import date

print("\nDate Format \"YYYYMMDD\"\n")
date_in_1 = input("Enter Date 1 : ")
year_in_1 = int(date_in_1[0:4])
month_in_1 = int(date_in_1[4:6])
day_in_1 = int(date_in_1[6:8])

date_in_2 = input("Enter Date 2 : ")
year_in_2 = int(date_in_2[0:4])
month_in_2 = int(date_in_2[4:6])
day_in_2 = int(date_in_2[6:8])

date_1 = date(year_in_1, month_in_1, day_in_1)
date_2 = date(year_in_2, month_in_2, day_in_2)
print("Number of Days Between the two Dates :", (date_2 - date_1).days)
