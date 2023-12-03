""" Module `module2.mod` """

from .. import utils
from ..config import NUMBER_A, NUMBER_B


def use_function_mul():
	""" Using the `utils` module `function_mul` function """
	print('>>> Result:', utils.function_mul(NUMBER_A, NUMBER_B))


def use_function_div():
	""" Using the `utils` module `function_div` function """
	print('>>> Result:', utils.function_div(NUMBER_A, NUMBER_B))
