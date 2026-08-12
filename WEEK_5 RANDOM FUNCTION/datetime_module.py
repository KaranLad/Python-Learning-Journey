import datetime

# 1. Current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# 2. Current date
today = datetime.date.today()
print("Today's date:", today)

# 3. Date parts
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# 4. Format date
formatted_date = today.strftime("%d/%m/%Y")
print("Formatted date:", formatted_date)

# 5. Convert string to datetime
date_string = "25-12-2026"
converted_date = datetime.datetime.strptime(date_string, "%d-%m-%Y")
print("Converted date:", converted_date)

# 6. Date difference
date1 = datetime.date(2026, 8, 5)
date2 = datetime.date(2026, 8, 15)
difference = date2 - date1
print("Difference:", difference.days, "days")

# 7. Add days
future_date = today + datetime.timedelta(days=7)
print("After 7 days:", future_date)