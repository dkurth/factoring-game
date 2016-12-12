from random import randint
import math
import sys
import colorama
from colorama import Fore, Back, Style

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
	return get_factors(n) == []

def clear_terminal():
	print(chr(27) + "[2J")

if __name__ == "__main__":

	colorama.init()
	clear_terminal()

	score = 0
	max_num = 100

	while True:
		x = randint(0, max_num)
		m = x # use this to show x after each factor is divided out
		factors = get_factors(x)
		factors.sort()

		user_factors = []

		if user_factors == factors: # prime
			continue

		print("")
		print("")
		print(Fore.BLUE + "*** Find the factors of " + str(x) + " ***")
		print()
		
		while user_factors != factors:

			# print("user_factors = {0}".format(user_factors))
			# print("factors = {0}".format(factors))

			print(Style.RESET_ALL)

			f = input("Enter a prime factor: ")
			try:
				f = int(f)
			except:
				if f.strip() == 'q':
					print("Bye!")
					sys.exit()
				continue

			if not is_prime(f):
				print(Fore.RED + "Sorry, that's not prime.  Try again!")
				continue

			if x % f == 0:
				user_factors.append(f)
				m2 = int(m / f)
				print(Fore.BLUE + "Good!  {0}/{1} = {2}".format(m, f, m2))
				m = m2
			else:
				print(Fore.RED + "Try again!")

			user_factors.sort()

		score = score + 1
		print()
		print(Fore.GREEN + "You found all the factors of {0}!".format(x))
		print("{0} = {1}".format(x, ' x '.join(str(f) for f in factors)))
		print()
		print("--------------- :-) :-D :-P ---------------- ")
		print("Your score: {0}".format(score))
		print()

