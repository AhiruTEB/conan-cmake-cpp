@echo off
setlocal

REM === Configuration variables ===
set PROFILE=profiles/windows-clang

REM === Release ===
conan install . -pr:a=%PROFILE% -s build_type=Release --build=missing
conan build . -pr:a=%PROFILE% -s build_type=Release --build=missing 

REM === Debug ===
REM conan install . -pr:a=%PROFILE% -s build_type=Debug --build=missing
REM conan build . -pr:a=%PROFILE% -s build_type=Debug --build=missing

pause
endlocal
