import datetime

noww=datetime.datetime.now()
print("Original datetime:", noww)

drop_microseconds=noww.replace(microsecond=0)
print ("Without_microseconds:",drop_microseconds)