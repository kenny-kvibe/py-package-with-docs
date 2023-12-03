
# Sphinx
> Documentation Generator Tool
> DOCs:  https://www.sphinx-doc.org/en/master


# Python `import` system
  https://docs.python.org/3/reference/import.html


# Python `__init__` vs `__main__` files

- `__init__.py` is run when you import a package into a running python program,
  which does not do anything as its only purpose is to mark the directory as a package.
  On the otherhand, it contains most of the code and defines all the classes.

- `__main__.py` is run as `'__main__'` when you run a package as the main program.
  For instance, `python -m package_name` at a command line runs `package_name/__main__.py`,
  which starts the package.

- In the context of `from . import file`, the `.` is `package_name`,
  so importing `.` imports `package_name`, which runs `package_name/__init__.py`.


# Package module usage

> Runs `run.py` which runs `app` package and doesn't call `app.__main__`
```cmd
python -B run.py
```

>  Runs `app.__main__` file without creating bytecode cache in `__pycache__`
```cmd
python -B -m app
```

>  Runs `app.__main__` file
```cmd
python -m app
```