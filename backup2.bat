@echo off

for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"

set "fullstamp=%YYYY%-%MM%-%DD%"

echo fullstamp: "%fullstamp%"


mysqldump -h 127.0.0.1 -u root -pandree2332 mydb > C:\Users\andre\Desktop\"EnsolunaBD"\"%fullstamp%".sql

pause
exit