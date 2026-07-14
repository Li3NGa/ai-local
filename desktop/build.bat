@echo off

pip install -r requirements.txt

pyinstaller --noconsole --onefile main.py --name AIWorld

echo Build finished.
pause
