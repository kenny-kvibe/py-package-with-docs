""" Module `module1` main """

from . import use_function_hello, use_function_sum


def main() -> int:
	""" Module `module1` main function """
	use_function_hello()
	use_function_sum()
	return 0


if __name__ == '__main__':
	raise SystemExit(main())
