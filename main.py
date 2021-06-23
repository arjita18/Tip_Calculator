print("Welcome to the tip calculator!")
bill = float(input("Enter the total bill: $"))
people = int(input("Enter the number of people to split the bill: "))
tip = int(input("What percentage tip would you like to pay? 10, 12 and 15: "))
tipAmount = bill * (tip / 100)
amount = (tipAmount + bill) / people
print("Each person should pay: $" + str("%.2f" % round(amount, 2)))
