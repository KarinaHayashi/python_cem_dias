print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
per_person = total_bill / people
per_person = round(per_person, 2)
print(f"Each person should pay: ${per_person}")

