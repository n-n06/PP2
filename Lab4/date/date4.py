import datetime

#today
today = datetime.date.today()

#inputing a date
day, month, year = tuple(map(int, input("Input a date in the DD.MM.YYYY format: ").split(".")))

someday = datetime.date(year, month, day)
diff = today - someday
print(diff.total_seconds())
