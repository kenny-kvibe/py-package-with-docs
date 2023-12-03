""" Module `module1.mod` """

from .. import utils
from ..config import NUMBER_A, NUMBER_B


def use_function_hello():
	""" Using the `utils` module `function_hello` function """
	utils.function_hello()


def use_function_sum():
	""" Using the `utils` module `function_sum` function """
	print('>>> Result:', utils.function_sum(NUMBER_A, NUMBER_B))
