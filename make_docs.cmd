@ECHO off
CD %~dp0

SETLOCAL
SET "DOC_DIR=docs"

IF EXIST %DOC_DIR% (
	PUSHD %DOC_DIR% >NUL
	make.bat html
	POPD >NUL
	START "" "%~dp0%DOC_DIR%\_build\html\index.html"
) ELSE (
	ECHO Directory "%DOC_DIR%" not found ^(run "init_docs.cmd" first^), exiting ...
)

ENDLOCAL
EXIT /B 0
