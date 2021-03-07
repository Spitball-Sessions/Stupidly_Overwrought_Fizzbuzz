import random
from collections import namedtuple
from fizzbuzz_designations import FizzBuzz
from calculations import FizzBuzzList

def printing_fizzbuzz_proofs():
    list = FizzBuzzList.fizzbuzzlist
    print(f'fizz is {FizzBuzz.fizz}, buzz is {FizzBuzz.buzz}, fizzbuzz is {FizzBuzz.fizzbuzz}, fizz * buzz is {FizzBuzz.fizzx}')
    print("So:")
    print(', '.join(list).replace("Fizzbuzz,", "Fizzbuzz,\n"))

def report_attempts():
    for i in range(len(FizzBuzzList.attempts)):
        print(f"It took {FizzBuzzList.attempts[i]} tries to get number {i+1}")

def show_attempts():
    FizzBuzz.get_fizzbuzz_attributes()
    FizzBuzzList.convert_lists()
    printing_fizzbuzz_proofs()
    report_attempts()

def dont_show_attempts():
    FizzBuzz.get_fizzbuzz_attributes()
    FizzBuzzList.convert_lists()
    printing_fizzbuzz_proofs()

def  main():
    inputs = input("Would you like to see the attempts?\n")
    if inputs == "yes" or inputs == "y":
        show_attempts()
    else:
        dont_show_attempts()



if __name__ == '__main__':
    main()
