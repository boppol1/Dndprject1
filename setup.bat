@echo off
REM Setup script for NeverEndingQuest (Windows)

echo ==========================================
echo NeverEndingQuest - Setup
echo ==========================================
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed
    echo Please install Python 3.9 or higher from python.org
    pause
    exit /b 1
)

echo Python found
python --version
echo.

REM Install requirements
echo Installing Python packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo Package installation failed
    pause
    exit /b 1
)

echo Packages installed successfully
echo.

REM Setup config
if not exist config.py (
    echo Setting up configuration...
    copy config_template.py config.py
    echo Created config.py
    echo.
    echo IMPORTANT: Edit config.py and add your OpenAI API key!
    echo Get one at: https://platform.openai.com/api-keys
) else (
    echo config.py already exists
)

echo.
echo ==========================================
echo Setup Complete!
echo ==========================================
echo.
echo Next steps:
echo 1. Edit config.py and add your OpenAI API key
echo 2. Run: python main.py
echo.
pause
