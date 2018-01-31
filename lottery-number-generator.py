import random


def numbers_generator(quantity):
    numbers_l = []

    while True:
        if len(numbers_l) == quantity:
            break

        lottery_numbers = random.randint(1, 42)

        if lottery_numbers not in numbers_l:
            numbers_l.append(lottery_numbers)
            numbers_l.sort()

    return numbers_l



def main():
    print "***LOTTERY NUMBER GENERATOR***"

    while True:
        user_input_quantity = raw_input('How many random lottery numbers would you have? ')


        quantity_number = int(user_input_quantity)
        print numbers_generator(quantity_number)

        again = raw_input('Would you like to run the program again? (y/n) ')

        if again != 'y' and again != 'yes':
            break

if __name__ == '__main__':
    main()