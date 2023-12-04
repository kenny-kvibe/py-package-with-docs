import app
import app.config as cfg


def main() -> int:
	print('App run')

	if cfg.VERBOSE:
		a, b = cfg.NUMBER_A, cfg.NUMBER_B
		print(f'>>> Numbers: {a = }, {b = }')

	# Run `module1` functions
	app.module1.use_function_hello()
	app.module1.use_function_sum()

	# Run `module2` functions
	app.module2.use_function_mul()
	app.module2.use_function_div()

	app.module2.run_daemon()
	
	return 0


if __name__ == '__main__':
	raise SystemExit(main())
