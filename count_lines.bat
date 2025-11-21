@echo off
REM Line Counter - Windows Batch File
REM Usage: count_lines.bat [directory] [--details]

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not in your PATH.
    echo Please install Python 3.6 or higher and try again.
    echo.
    pause
    exit /b 1
)

REM Check if count_lines.py exists
if not exist "count_lines.py" (
    echo.
    echo ERROR: count_lines.py not found in current directory.
    echo Please make sure you're running this from the correct folder.
    echo.
    pause
    exit /b 1
)

REM Run the Python script
python count_lines.py %*

REM Check if script ran successfully
if errorlevel 1 (
    echo.
    echo ERROR: Script execution failed.
    echo.
    pause
    exit /b 1
)

echo.
pause

