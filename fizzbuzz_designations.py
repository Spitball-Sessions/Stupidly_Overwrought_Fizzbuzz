import random
from collections import namedtuple

class FizzBuzz:
    def __init__(self, fizz, buzz, fizzbuzz, fizz_x_buzz):
        self.fizz = fizz
        self.buzz = buzz
        self.fizzbuzz = fizzbuzz
        self.fizzx = fizz_x_buzz

    def get_fizzed():
        FizzBuzz.fizz = random.randint(2, 5)
        # FizzBuzz.get_buzzed() <- why doesn't this work?

    def get_buzzed():
        buzz = 0
        fizz = FizzBuzz.fizz
        while buzz < 99:
            buzz = random.randint(1, 10)
            if buzz <= fizz or (buzz % fizz) == 0:
                continue
            else:
                FizzBuzz.buzz = buzz
                return

    def get_fizzbuzzed():
        FizzBuzz.fizzbuzz = (FizzBuzz.fizz + FizzBuzz.buzz)


    def get_fizzxed():
        FizzBuzz.fizzx = (FizzBuzz.fizz * FizzBuzz.buzz)

    @staticmethod
    def get_fizzbuzz_attributes():
        FizzBuzz.get_fizzed()
        FizzBuzz.get_buzzed()
        FizzBuzz.get_fizzbuzzed()
        FizzBuzz.get_fizzxed()
