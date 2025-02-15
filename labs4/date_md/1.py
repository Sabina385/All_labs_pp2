import datetime

today= datetime.date.today()
past_5days=today-datetime.timedelta(days=5)
print(past_5days)

