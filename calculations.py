import random
from fizzbuzz_designations import FizzBuzz

class FizzBuzzList:
    def __init__(self, number_list, attempt_list, list_length, usable, spiteful):
        self.numbers = number_list
        self.attempts = attempt_list
        self.list_length = list_length
        self.fizzbuzzlist = usable
        self.spiteful = spiteful


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

        FizzBuzzList.numbers = list[1:]
        FizzBuzzList.attempts = attempt_list


    def create_fizzbuzz_list():
       list_length = FizzBuzz.fizzx*10
       usable_list = []

       for i in range(list_length):
           if FizzBuzzList.numbers[i] % FizzBuzz.fizzbuzz == 0:
               usable_list.append("Fizzbuzz")
           elif FizzBuzzList.numbers[i] % FizzBuzz.buzz == 0:
               usable_list.append("Buzz")
           elif FizzBuzzList.numbers[i] % FizzBuzz.fizz == 0:
               usable_list.append("Fizz")
           else:
               usable_list.append(str(FizzBuzzList.numbers[i]))

       FizzBuzzList.fizzbuzzlist = usable_list

    def create_attempt_list():
        list_length = len(FizzBuzzList.attempts)
        spite = []

        for i in range(list_length):
            if FizzBuzzList.attempts[i] % FizzBuzz.fizzbuzz == 0:
                spite.append("Fizzbuzz")
            elif FizzBuzzList.attempts[i] % FizzBuzz.buzz == 0:
                spite.append("Buzz")
            elif FizzBuzzList.attempts[i] % FizzBuzz.fizz == 0:
                spite.append("Fizz")
            else:
                spite.append(FizzBuzzList.attempts[i])

        FizzBuzzList.spiteful = spite

    def convert_lists():
        FizzBuzzList.create_list()
        FizzBuzzList.create_fizzbuzz_list()
        FizzBuzzList.create_attempt_list()

