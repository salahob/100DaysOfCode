
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tips = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

tips_as_percent = tips / 100
total = bill * tips_as_percent
total_bill = bill + total

bill_per_person = "{:.2f}".format(total_bill / people)
print(f"Each person should pay: ${bill_per_person}")
