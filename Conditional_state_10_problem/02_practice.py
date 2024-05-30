# Movie ticket price

# from datetime import datetime

# current_date_time = datetime.now()

# weekday_number = current_date_time.weekday()

# age = int(input("Enter your age : "))

# price_for_adult = 12
# price_for_child = 8

# if age >= 18:
#     print(f"You are and adult ticket price for you ${price_for_adult}")
#     if weekday_number == 0:
#         print("Hurray today is monday you got $2 discount $",price_for_adult-2 )
# elif age < 18:
#     print(f"You are a child ticket price for you ${price_for_child}")
#     if weekday_number == 0:
#         print("Hurray today is monday you got $2 discount $",price_for_child-2 )
# else:
#     print("System error...................")


# --------------------------------------------------------------------

# Other Solution : 

age = int(input("Enter your age : "))
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print(price)