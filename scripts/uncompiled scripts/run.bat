@echo off

cd ..
cd diskmth

set srcPath=%cd%

cd ..
cd python

start pythonw.exe "%srcPath%\Main.py"