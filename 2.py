import random

def get_numbers_ticket(min_num, max_num, quantity):

    if not (1 <= min_num <= max_num <= 1000):
        return []
    if max_num - min_num + 1 < quantity:
        return []
    random_numbers = set()
    while len(random_numbers) < quantity:
        random_numbers.add(random.randint(min_num, max_num))

    sorted_numbers = sorted(random_numbers)
    return sorted_numbers

lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)