
print("Welcome to the tip calculator")
bill= input("what was the total bill?\t")
tip = input("what percentage tip whould you like to give? 10, 12 or 15?\t")
person = input("how many person to split the bill?")
pay = round(((int(bill)*(int(tip)/100)) + int(bill))/int(person),2)
print(f"Each person should pay: {pay}")