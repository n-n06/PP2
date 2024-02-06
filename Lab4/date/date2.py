import datetime

yesterday = datetime.date.today() - datetime.timedelta(days = 1)
print(yesterday)

today = datetime.date.today()
print(today)


tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
print(tomorrow)