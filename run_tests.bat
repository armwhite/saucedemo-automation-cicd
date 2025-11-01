@echo off
cd /d "%~dp0"

echo 🔄 Starting Selenium Grid in Docker...
docker compose up -d
timeout /t 5 >nul

set timestamp=%date:~-4,4%-%date:~-10,2%-%date:~-7,2%_%time:~0,2%-%time:~3,2%-%time:~6,2%
set timestamp=%timestamp: =0%
set report=src\reports\report_%timestamp%.html

echo 🚀 Running tests on Selenium Grid (Chrome + Firefox)
pytest -n 2 -v --html=%report% --self-contained-html

echo ✅ Report generated: %report%
start "" "%report%"
pause
