@ECHO off
CD %~dp0

REM Runs `run.py` which runs `app` package and doesn't call `app.__main__`
python -B run.py

REM Runs `app.__main__` file without creating bytecode cache in `__pycache__`
REM python -B -m app

REM Runs `app.__main__` file
:: python -m app

EXIT /B 0
