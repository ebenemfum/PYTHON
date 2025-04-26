print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
#tip = (float(input("How much tip would you like to give? 10, 12, or 15?")/100)*total)
tip = (float(input("How much tip would you like to give? 10, 12, or 15?")) / 100) * total

split = float(input("How many people to split the bill?"))
each_total = float((round((total + tip)/split,2)))
print(f"Each person should pay: ${each_total}")