import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max:
        return []

    if quantity < 1 or quantity > max - min + 1:
        return []

    numbers = []

    while len(numbers) < quantity:
        number = random.randint(min, max)

        if number not in numbers:
            numbers.append(number)

    numbers.sort()

    return numbers

print(get_numbers_ticket(1, 67, 7))