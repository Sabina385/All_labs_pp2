import datetime

date_1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS):")
date_2= input("Enter the second date (YYYY-MM-DD HH:MM:SS):")

date1 = datetime.datetime.strptime(date_1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date_2, "%Y-%m-%d %H:%M:%S")

difference = date2 - date1
seconds_difference = abs(difference.total_seconds())

print("The difference is:", int(seconds_difference))

