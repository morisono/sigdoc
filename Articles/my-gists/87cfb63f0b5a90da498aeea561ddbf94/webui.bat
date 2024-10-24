@echo off
REM  CLS
ECHO.
REM Running Admin shell

:init
 setlocal DisableDelayedExpansion
 set cmdInvoke=1
 set winSysFolder=System32
 set "batchPath=%~dpnx0"
 rem this works also from cmd shell, other than %~0
 for %%k in (%0) do set batchName=%%~nk
 set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
 setlocal EnableDelayedExpansion

:checkPrivileges
  NET FILE 1>NUL 2>NUL
  if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
  if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)
  ECHO.
  REM Invoking UAC for Privilege Escalation..

  ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
  ECHO args = "ELEV " >> "%vbsGetPrivileges%"
  ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
  ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
  ECHO Next >> "%vbsGetPrivileges%"

  if '%cmdInvoke%'=='1' goto InvokeCmd

  ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
  goto ExecElevation

:InvokeCmd
  ECHO args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
  ECHO UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"

:ExecElevation
 "%SystemRoot%\%winSysFolder%\WScript.exe" "%vbsGetPrivileges%" %*
 exit /B

:gotPrivileges
 setlocal & cd /d %~dp0
 if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)


REM Get system information
:check_environment
echo Checking environment...
for /f "tokens=2 delims==" %%A in ('wmic os get Caption /value') do set "OS=%%A"
for /f "tokens=2 delims==" %%A in ('wmic os get Version /value') do set "VERSION=%%A"

echo Environment check passed.
echo Operating System: %OS%
echo Version: %VERSION%



REM Check if the OS is Windows
:check_os
if "%OS%"=="Windows_NT" (
    echo Running on Windows
) else (
    echo This script is intended to run on Windows. Exiting...
    pause
)

REM Set default values if not defined
if not defined PYTHON (set PYTHON=python)
if defined GIT (set "GIT_PYTHON_GIT_EXECUTABLE=%GIT%")
if not defined VENV_DIR (set "VENV_DIR=%~dp0%venv")

set ERROR_REPORTING=FALSE

REM Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.10 or later.
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%V in ('python --version 2^>^&1') do (
    set PYTHON_VERSION=%%V
)
echo Detected Python version: %PYTHON_VERSION%


REM Check if venv exists, if not create it
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        exit /b 1
    )
)

REM Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

REM Check if requirements are installed
pip freeze | findstr /C:"gradio==4.37.1" > nul
if %errorlevel% neq 0 (
    echo Installing requirements...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install requirements.
        exit /b 1
    )
)

REM Run the application
echo Starting the application...
python src/app/run.py
if %errorlevel% neq 0 (
    echo Failed to start the application.
    exit /b 1
)

REM Keep the window open to see errors
pause

REM Deactivate the virtual environment
REM deactivate

REM endlocal
