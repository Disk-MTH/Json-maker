@echo off

set zipPath=%cd%

cd ..

set decompPath=%cd%

echo Python environment decompiling !

powershell Expand-Archive -LiteralPath '%zipPath%\python.zip' -DestinationPath '%decompPath%\python' -Force

echo Done !

pause