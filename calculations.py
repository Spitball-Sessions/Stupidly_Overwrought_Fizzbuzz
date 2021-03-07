import random
from fizzbuzz_designations import FizzBuzz


def create_list():
    list = [0]
    attempt_list = []
    y = 0

    while len(list) != 1001:
        x = random.randint(0,1000)
        if x != (list[-1] + 1):
            y += 1
            continue
        else:
            attempt_list.append(y)
            y = 0
            list.append(x)
    print(list)
    print(attempt_list)




def length_list(input):
    pass