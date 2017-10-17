@echo off

NET SESSION >NUL
IF %ERRORLEVEL% NEQ 0 GOTO ELEVATE >NUL
goto :start

:ELEVATE
CD /d %~dp0
MSHTA "javascript: var shell = new ActiveXObject('shell.application'); shell.ShellExecute('%~nx0', '', '', 'runas', 1);close();" >NUL
EXIT

:start
netsh interface set interface Ethernet ENABLED >NUL
