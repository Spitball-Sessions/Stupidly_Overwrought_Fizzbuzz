import random
from collections import namedtuple

class FizzBuzz:
    def get_buzz(fizz):
        while fizz:
            buzz = random.randint(1, 10)
            if buzz <= fizz or (buzz % fizz) == 0:
                continue
            else:
                return buzz

    def get_fizz():
        fizz = random.randint(2, 5)
        buzz = FizzBuzz.get_buzz(fizz)
        return fizz, buzz


    def get_fizzbuzz_attributes(fizz_buzz):
        fizzbuzz = fizz_buzz[0] + fizz_buzz[1]
        fizz_x_buzz = fizz_buzz[0] * fizz_buzz [1]

        fizzbuzzattributes = namedtuple('FizzbuzzAttributes', ['fizz', 'buzz', 'fizzbuzz','fizz_x_buzz'])
        fizzbuzz_attributes = fizzbuzzattributes(fizz=fizz_buzz[0], buzz=fizz_buzz[1], fizzbuzz=fizzbuzz, fizz_x_buzz = fizz_x_buzz)

        print(fizzbuzz_attributes.fizzbuzz)

        return fizzbuzz_attributes

