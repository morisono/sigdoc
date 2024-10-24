@echo off
REM  CLS
set ERROR_LOG=error.log
set ERROR_REPORTING=FALSE

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
echo.
REM Invoking UAC for Escalation..

echo Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
echo args = "ELEV " >> "%vbsGetPrivileges%"
echo For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
echo args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
echo Next >> "%vbsGetPrivileges%"

if '%cmdInvoke%'=='1' goto InvokeCmd

echo UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
goto ExecElevation

:InvokeCmd
echo args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
echo UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"

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

:check_disk_space
echo.
echo Checking disk space...
for /F "tokens=2 delims==" %%A in ('wmic logicaldisk where "DeviceID='C:'" get FreeSpace /value') do set "free_space=%%A"
set /a free_space_mb=free_space / 1048576
echo Free space: !free_space! bytes

if !free_space! lss 1073741824 (
    echo Insufficient disk space. Only !free_space_mb! MB available.
    exit /b 1
) else (
    echo Sufficient disk space available: !free_space_mb! MB
)

:check_network
echo.
echo Checking network connection...
ping -n 1 www.example.com >nul
if !errorlevel! neq 0 (
    echo Network connection failed. >> "!ERROR_LOG!"
    goto error
)
echo Network connection successful.

:set_time_limit
echo.
echo Setting time limit...
set start_time=%time%
set time_limit=3600
echo time_limit: !time_limit!


:port_settings
set port=8080
set ipaddress=192.168.1.10
PowerShell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"
netsh advfirewall firewall add rule name="Open Port %port%" protocol=TCP dir=in localport=%port% action=allow
netsh interface portproxy add v4tov4 listenport=%port% listenaddress=0.0.0.0 connectport=%port% connectaddress=%ipaddress%

REM Function to check the shell
:check_shell
echo.


REM Check if the OS is Windows
:check_os
echo.
if "%OS%"=="Microsoft Windows 11 Pro" (
    echo Running on Windows
) else (
    echo This script is intended to run on Windows. Exiting...
    pause
)

REM Set default values if not defined
if not defined PYTHON (set PYTHON=python)
if defined GIT (set "GIT_PYTHON_GIT_EXECUTABLE=%GIT%")
if not defined VENV_DIR (set "VENV_DIR=%~dp0%venv")


REM Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.10 or later.
    exit /b 1
)

REM Check Python version
echo.
for /f "tokens=2" %%V in ('python --version 2^>^&1') do (
    set PYTHON_VERSION=%%V
)
echo Detected Python version: %PYTHON_VERSION%


REM Check if venv exists, if not create it
echo.
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        exit /b 1
    )
)

REM Activate the virtual environment
echo.
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

:create_shortcut
echo.
echo Creating shortcut...
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%~dp0Launch.lnk'); $Shortcut.TargetPath = '%~dpnx0'; $Shortcut.Save()"
if %errorlevel% neq 0 (
    echo Error creating shortcut. >> %ERROR_LOG%
)

REM Run the application
echo.
echo Starting the application...
python src/app/run.py
if %errorlevel% neq 0 (
    echo Failed to start the application.
    exit /b 1
)

:error
echo.
echo An error occurred. Check %ERROR_LOG% for details.
exit /b 1

:end
echo Script completed successfully.
exit /b 0

REM Keep the window open to see errors
pause

REM Deactivate the virtual environment
REM deactivate

REM endlocal

