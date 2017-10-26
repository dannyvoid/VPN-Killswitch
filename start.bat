@echo off

net session >nul
if %errorlevel% neq 0 goto elevate >nul
goto :start

:elevate
cd /d %~dp0
mshta "javascript: var shell = new ActiveXObject('shell.application'); shell.ShellExecute('%~nx0', '', '', 'runas', 1);close();" >nul
exit

:start
cd /d %~dp0
python app.py
