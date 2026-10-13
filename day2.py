# Café Outing Split-Bill Calculator

bill = float(input("Enter the total bill: "))
friends = int(input("Enter the number of friends: "))

tip = bill * 10 / 100
total_bill = bill + tip

each_person = total_bill / friends

print("Total bill with 10% tip:", total_bill)
print("Each person pays:", each_person)