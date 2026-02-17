@echo off
chcp 65001 >nul

REM Change to project root directory
cd /d "%~dp0\.."

echo ========================================
echo 英文文章生成器 - Article Generator
echo GUI 图形界面版本
echo ========================================
echo.

call conda activate py10
if errorlevel 1 (
    echo ERROR: 无法激活 py10 环境
    echo Please run scripts\setup.bat first
    pause
    exit /b 1
)

echo 正在启动 GUI 界面...
echo.

REM 启动 GUI 版本（默认模式）
python main.py

pause

