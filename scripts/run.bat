@echo off
chcp 65001 >nul

REM Change to project root directory
cd /d "%~dp0\.."

echo ========================================
echo Article Generator - Run Script
echo ========================================
echo.

call conda activate py10
if errorlevel 1 (
    echo ERROR: Cannot activate py10 environment
    echo Please run scripts\setup.bat first
    pause
    exit /b 1
)

python main.py

pause

