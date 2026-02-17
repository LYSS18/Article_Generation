@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo 英文文章生成器 - GUI版本
echo Article Generator - GUI Version
echo ========================================
echo.

REM 激活conda环境
call conda activate py10
if errorlevel 1 (
    echo ERROR: 无法激活py10环境
    echo Please run scripts\setup.bat first
    pause
    exit /b 1
)

echo 正在启动GUI界面...
echo.

REM 运行GUI程序
python main_gui.py

pause

