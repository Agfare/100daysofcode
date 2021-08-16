# Arguments and parameters
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")


greet_with("Jack Bauer", "Nowhere")

# Paint area calculator

import math


def paint_calc(height, width, cover):
    area = height * width
    cans_number = math.ceil(area / cover)
    print(f"You'll need {cans_number} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)

# Caesar cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"Your message is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for char in cipher_text:
        position = alphabet.index(char)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"Your message is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
