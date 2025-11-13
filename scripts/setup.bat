@echo off
chcp 65001 >nul

REM Change to project root directory
cd /d "%~dp0\.."

echo ========================================
echo Article Generator - Setup Script
echo ========================================
echo.

echo [1/3] Activating conda environment...
call conda activate py10
if errorlevel 1 (
    echo ERROR: Cannot activate py10 environment
    echo Please create py10 environment first: conda create -n py10 python=3.10
    pause
    exit /b 1
)

echo [2/3] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [3/3] Setting up environment variables...
if not exist config\.env (
    copy config\.env.example config\.env
    echo.
    echo SUCCESS: config\.env file created
    echo.
    echo IMPORTANT:
    echo Please edit config\.env file and add your API key
    echo Then run: scripts\run.bat or python main.py
    echo.
) else (
    echo SUCCESS: config\.env file already exists
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Edit config\.env file and add your API key
echo 2. Run: scripts\run.bat or python main.py
echo.
pause

