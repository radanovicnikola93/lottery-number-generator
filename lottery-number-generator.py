import random

print "Welcome to the Lottery numbers generator."



def numbers_generator(quantity):
    numbers_l = []

    while True:
        if len(numbers_l) == quantity:
            break

        lottery_numbers = random.randint(1, 42)

        return numbers_l



