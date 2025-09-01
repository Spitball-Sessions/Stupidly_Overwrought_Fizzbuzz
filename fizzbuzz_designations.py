import random
from collections import namedtuple

class FizzBuzz:
    def __init__(self, fizz, buzz, fizzbuzz, fizz_x_buzz):
        self.fizz = fizz
        self.buzz = buzz
        self.fizzbuzz = fizzbuzz
        self.fizzx = fizz_x_buzz

    def get_fizzed(self):
        self.fizz = random.randint(2, 5)
        # FizzBuzz.get_buzzed() <- why doesn't this work?

    def get_buzzed(self):
        buzz = 0
        fizz = self.fizz
        while buzz < 99:
            buzz = random.randint(1, 10)
            if buzz <= fizz or (buzz % fizz) == 0:
                continue
            else:
                self.buzz = buzz
                return

    def get_fizzbuzzed(self):
        self.fizzbuzz = (self.fizz + self.buzz)


    def get_fizzxed(self):
        self.fizzx = (self.fizz * self.buzz)

    @staticmethod
    def get_fizzbuzz_attributes():
        FizzBuzz.get_fizzed()
        FizzBuzz.get_buzzed()
        FizzBuzz.get_fizzbuzzed()
        FizzBuzz.get_fizzxed()
