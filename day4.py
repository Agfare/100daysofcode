# random integer generator
import random

randomInteger = random.randint(1, 10)
print(randomInteger)

randomFloat = random.random() * 5
print(randomFloat * 5)

# heads or tails
import random

randomInteger = random.randint(0, 1)
if randomInteger == 0:
    print("Tails")
else:
    print("Heads")
