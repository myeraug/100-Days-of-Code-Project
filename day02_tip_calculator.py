# 100 Days of Code - The Complete Python Pro Bootcamp
# day 02 project
# tip calculator

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?: $"))
tip = int(input("How much % tip would you like to give? 10, 12, or 15? "))
new_tip = float(total_bill * tip / 100)
split_bill = int(input("How many people to split the bill? "))
pay_per_person = float((total_bill + new_tip) / split_bill)

print(f"Each person should pay: ${round(pay_per_person, 2)}")