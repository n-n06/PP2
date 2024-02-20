from datetime import timedelta
from datetime import date

today = date.today()
print(today)
five_days_ago = today - timedelta(days=5)
print(five_days_ago)


print(f"\n{today.strftime(format="%B %d, %Y. %A")}")
print(five_days_ago.strftime(format = "%B %d, %Y. %A"))