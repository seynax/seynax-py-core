@echo off

for /F "delims=" %%A in ('git log -1 --format^="%%H" -- %f%') do set "g=%%A"
echo %g%|clip
powershell Get-Clipboard