""" Module `utils.file2` """

from ..config import VERBOSE


def function_mul(a:int, b:int) -> int:
	""" Calculates the multiplication of `a` and `b` numbers
	:arg a: any number
	:type a: `int`
	:arg b: any number
	:type b: `int`
	:return: `int` multiplication of `a` and `b` (`a*b`)
	"""
	c = a * b
	if VERBOSE:
		print(f'>>> {a} * {b} = {c}')
	return c


def function_div(a:int, b:int) -> float:
	""" Calculates the division of `a` and `b` numbers
	:arg a: any number
	:type a: `int`
	:arg b: any number
	:type b: `int`
	:return: `float` division of `a` and `b` (`a/b`)
	"""
	c = a / b
	if VERBOSE:
		print(f'>>> {a} / {b} = {c}')
	return c
