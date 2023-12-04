""" Module `module2` main """

from . import use_function_mul, use_function_div, run_daemon


def main() -> int:
	""" Module `module2` main function """
	use_function_mul()
	use_function_div()
	run_daemon()
	return 0


if __name__ == '__main__':
	raise SystemExit(main())
