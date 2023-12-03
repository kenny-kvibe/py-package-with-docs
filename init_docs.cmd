@ECHO off
CD %~dp0

SETLOCAL
SET "DOC_DIR=docs"
SET "PKG_DIR=app"

IF NOT EXIST %DOC_DIR% (
	MKDIR %DOC_DIR%
	PUSHD %DOC_DIR% >NUL
	sphinx-quickstart
	POPD >NUL
	sphinx-apidoc -o %DOC_DIR% %PKG_DIR%
) ELSE (
	ECHO Directory "%DOC_DIR%" already exists, exiting ...
)

ENDLOCAL
EXIT /B 0
