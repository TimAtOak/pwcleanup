@echo off
echo Removing old EXE...
if exist dist\main.exe del dist\main.exe
echo Building new EXE...
python -m PyInstaller --onefile main.py
echo Done! Check dist\main.exe
pause