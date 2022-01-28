@echo off

set buildScriptPath=%cd%

cd ..
cd python

start /wait python.exe "%buildScriptPath%\build.py"