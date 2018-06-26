import datetime

print("formatting and rounding...")
value = 12.3456
width = 20
precision = 4

my_fstr = f"The value is {value}"
print(my_fstr)

my_formatstr = "The value is {value}".format(value=value)
print(my_formatstr)

# my_fstr = f"The value is {value:{width}.{precision}}"
# print(my_fstr)

# print("\ndates and times...")
# today = datetime.datetime.today()

# today_no_format = f"{today}"
# print(today_no_format)

# formatted_day = f"{today:%B %d, %Y}"
# print(formatted_day)

# weekday = f"Today is a {today:%A}"
# print(weekday)

