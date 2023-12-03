""" Module `utils.file1` """

from ..config import VERBOSE


def function_hello():
	""" prints `Hello world` """
	print('>>> Hello world')


def function_sum(a:int, b:int) -> int:
	""" Calculates the sum of `a` and `b` numbers
	:arg a: any number
	:type a: `int`
	:arg b: any number
	:type b: `int`
	:return: `int` sum of `a` and `b` (`a+b`)
	"""
	c = a + b
	if VERBOSE:
		print(f'>>> {a} + {b} = {c}')
	return c
