from random import randint
from functools import reduce
from AsciiIncluder import AsciiIncluder

import math
import operator
import sys
import colorama

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_factors(n):
    factors = []
    for i in range(2, n):
        while n % i == 0:
            factors.append(i)
            n = int(n/i)
    return factors

def is_prime(n):
    return get_factors(n) == [] and n != 1

def clear_terminal():
    print(chr(27) + "[2J")
    for i in range(10):
        print("")

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

if __name__ == "__main__":

    colorama.init()
    clear_terminal()

    score = 0
    max_num = 100

    goal = input("How many numbers are we factoring today? ")
    try:
        goal = int(goal)
    except:
        print("That is invalid.")
        sys.exit()


    while goal > 0:
        x = randint(0, max_num)
        m = x # use this to show x after each factor is divided out
        factors = get_factors(x)
        factors.sort()

        user_factors = []

        if user_factors == factors: # prime
            continue

        goal -= 1

        print("")
        print("")
        print(colorama.Fore.BLUE + "*** Find the factors of " + str(x) + " ***")
        print()
        
        while prod(user_factors) != x:

            # print("user_factors = {0}".format(user_factors))
            # print("factors = {0}".format(factors))

            print(colorama.Style.RESET_ALL)

            f = input("Enter a prime factor: ")
            try:
                f = int(f)
            except:
                if f.strip() == 'q':
                    print("Bye!")
                    sys.exit()
                continue

            if not is_prime(f):
                print(colorama.Fore.RED + "Sorry, that's not prime.  Try again!")
                continue

            if m % f == 0:
                print("x = {0}, f = {1}, x % f = {2}".format(x, f, x % f))
                user_factors.append(f)
                m2 = int(m / f)
                print(colorama.Fore.BLUE + "Good!  {0}/{1} = {2}".format(m, f, m2))
                m = m2
            else:
                print(colorama.Fore.RED + "Try again!")

            user_factors.sort()

        score = score + 1
        print()
        print(colorama.Fore.GREEN + "You found all the factors of {0}!".format(x))
        print("{0} = {1}".format(x, ' x '.join(str(f) for f in factors)))
        print()
        print("--------------- :-) :-D :-P ---------------- ")
        print("Your score: {0}".format(score))
        print()

    ai = AsciiIncluder("art")
    print(colorama.Fore.GREEN + ai.art["trogdor"])

