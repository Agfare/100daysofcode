# data types and conversion
# integer into string
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

# integer into string
a = str(123)
print(type(a))

# integer into float
a = float(123)
print(type(a))

# a code to add first digit of a two-digit number to the second one
two_digit_number = input("Type a two digit number: ")
# first we define a type of a number
print(type(two_digit_number))
# creating variables for each digit
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
# printing the output with a type conversion in mind
print(int(first_digit) + int(second_digit))

# BMI calculator
# asking a user about his/her parameters
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# printing the result with a concatenation of two strings and types conversion into integer and float to calculate a BMI
print("Your BMI is: " + str((int(weight) / float(height) ** 2)))

# Death calculator
age = input("What is your current age?")
what_is_left_years = int(years) - int(age)
days_left = int(what_is_left_years) * 365
weeks_left = int(what_is_left_years) * 52
months_left = int(what_is_left_years) * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

# Tip calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
print(bill)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
print(tip)
split = int(input("How many people to split with? "))
tip_percent = tip / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
split_amount = round(total_bill / split, 2)
print(f"Each person should pay: {split_amount}")