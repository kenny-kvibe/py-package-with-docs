""" Module `module2.mod` """

from .. import utils
from ..config import NUMBER_A, NUMBER_B


def use_function_mul():
	""" Using the `utils` module `function_mul` function """
	print('>>> Result:', utils.function_mul(NUMBER_A, NUMBER_B))


def use_function_div():
	""" Using the `utils` module `function_div` function """
	print('>>> Result:', utils.function_div(NUMBER_A, NUMBER_B))

def run_daemon():
	""" Run the daemon - non-exit process, prints per second """
	i = 0
	loop = True
	try:
		while loop:
			i += 1
			print(f'>>> Loop: {i}')
			time.sleep(1)
	except KeyboardInterrupt:
		print('Exiting ...')
		loop = False
