import random
from collections import namedtuple
from fizzbuzz_designations import FizzBuzz




def  main():
    fizzbuzz_tuple = FizzBuzz.get_fizzbuzz_attributes(FizzBuzz.get_fizz())

    print(f'fizz is {fizzbuzz_tuple.fizz}, buzz is {fizzbuzz_tuple.buzz}, fizzbuzz is {fizzbuzz_tuple.fizzbuzz}, fizz * buzz is {fizzbuzz_tuple.fizz_x_buzz}')



if __name__ == '__main__':
    main()
