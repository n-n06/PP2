from datetime import timedelta, datetime as dt
x = dt.now()
print(x.strftime(format = "%Y-%m-%d"))
five_days_ago = x - timedelta(days=5)
print(five_days_ago.strftime(format = "%Y-%m-%d"))

print(f"\n{x.strftime(format="%B %d, %Y. %A")}")
print(five_days_ago.strftime(format = "%B %d, %Y. %A"))