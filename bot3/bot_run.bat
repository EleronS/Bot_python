@echo off

call %~dp0bot\bot3\venv\Scripts\activate

cd %~dp0bot\bot3

set TOKEN=

python bot_t.py

pause