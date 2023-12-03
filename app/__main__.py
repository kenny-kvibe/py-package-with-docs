""" Package module `app` main """

from . import module1, module2


def main() -> int:
	""" Module `app` main function """
	print('App __main__')

	# use module1
	module1.use_function_hello()
	module1.use_function_sum()

	# use module2
	module2.use_function_mul()
	module2.use_function_div()

	return 0


if __name__ == '__main__':
	raise SystemExit(main())
