# Import seed and sample functions
from random import seed
from random import sample
from time import gmtime


def push_lucky_numbers(lucky_list):
    subset = sample(sequence, 6)
    for y in subset:
        if y not in lucky_list:
            lucky_list.append(y)


def fill_lucky_list(lucky_list):
    for z in range(7):
        # seed random number generator
        seed(gmtime())
        for x in range(13):
            push_lucky_numbers(lucky_list)


sequence = [i for i in range(1, 61)]
numbers = []
fill_lucky_list(numbers)
seed(gmtime())
for n in range(1, 4):
    lucky = sample(numbers, 6)
    print("Lucky numbers - ", n, lucky)

