#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

total_bill = input("Welcome to the tip calculator.\nWhat was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, 15? ")
people = input("How many people to split the bill? ")

tip_float = (int(tip)/100) + 1
pay_per_person = (float(total_bill) / int(people)) * tip_float
limited_pay_per_person = round(pay_per_person, 2)
limited_pay_per_person = "{:.2f}".format(pay_per_person)

print(f"Each person should pay: ${limited_pay_per_person}")
