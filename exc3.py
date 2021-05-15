# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)

days90 = 90 * 365
weeks90 = 90 * 52
months90 = 90 * 12

days_age = age_int * 365
weeks_age = age_int * 52
months_age = age_int * 12

days_left = days90 - days_age
weeks_left = weeks90 - weeks_age
months_left = months90 - months_age

print(f"You have {days_left}, {weeks_left} weeks, and {months_left} months left.")






