income = float(input("Enter the annual income: "))
tax = 0

if income < 85528:
    tax = income * 0.18 - 556.02
    if tax < 0:
        tax = 0.0
# Write the rest of your code here.
elif income >= 85528:
    tax = 14839.02 + 0.32 * (income - 85528)

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
