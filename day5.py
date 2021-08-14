# day5
# a list of fruits is created
fruits = ["Apples", "Peach", "Pear"]
# each fruit is assigned a variable "fruit"
for fruit in fruits:
    # printing each fruit for the whole fruits list
    print(fruit)
    print(fruit + " Pie")
    print(fruits)
print(fruits)

# calculating an average of students' heights
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0  # a total height is unknown
for height in student_heights:  # we take every value from the student_heights list
    total_height += height  # we add every value taken from the student_heights list to the total_height until the
    # list is finished
print(f"total height = {total_height}")  # printing the total height of all students

number_of_students = 0  # a total number of students is unknown
for student in student_heights:  # we take every index of every value from the student_heights list
    number_of_students += 1  # we add every index taken from the student_heights list to the number_of_students until
    # the list is finished
print(f"number of students = {number_of_students}")  # printing the total number of students

average_height = round(total_height / number_of_students)
print(average_height)

# checking the biggest number in the list
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_number = 0
for number in student_scores:
    if number > max_number:
        max_number = number
print(f"The highest score in the class is: {max_number}")

# calculating a sum of all the evens from 1 to 100
total = 0
for number in range(0, 101, 2):
    total += number
print(total)

# fizz-buzz task
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# random password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for letter in letters:
    print(random(letters))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(x, random)
