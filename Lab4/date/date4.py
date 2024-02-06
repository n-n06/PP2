import datetime

today = datetime.date.today()
someday = datetime.date(2024, 1, 28)
diff = today - someday
print(diff.total_seconds())
