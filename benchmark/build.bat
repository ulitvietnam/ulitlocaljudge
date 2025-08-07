@echo off
cls
setlocal

set "SUCCESS=false"

:: Kiểm tra Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found!
    goto end
) else (
    echo Python found!
)

:: Kiểm tra g++
where g++ >nul 2>nul
if %errorlevel% neq 0 (
    echo C++ not found!
    goto end
) else (
    echo C++ found!
)

echo Installing Python libraries from requirements.txt...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install Python libraries!
    goto end
)

:: Clean up
if exist benchmark_PY.exe (
    echo Deleting benchmark_PY.exe...
    del /q benchmark_PY.exe
)

if exist benchmark_CPP.exe (
    echo Deleting benchmark_CPP.exe...
    del /q benchmark_CPP.exe
)

if exist build (
    echo Deleting build folder...
    rmdir /s /q build
)

if exist dist (
    echo Deleting dist folder...
    rmdir /s /q dist
)

if exist benchmark_PY.spec (
    echo Deleting benchmark_PY.spec...
    del /q benchmark_PY.spec
)

echo Building benchmark_PY.py...
python -m PyInstaller --onefile src\benchmark_PY.py
if %errorlevel% neq 0 (
    echo Failed to build benchmark_PY!
    goto end
)

echo Copying benchmark_PY.exe from dist folder...
copy /y dist\benchmark_PY.exe benchmark_PY.exe >nul
if %errorlevel% neq 0 (
    echo Failed to copy benchmark_PY.exe!
    goto end
)

:: Clean up again
if exist build (
    echo Deleting build folder...
    rmdir /s /q build
)

if exist dist (
    echo Deleting dist folder...
    rmdir /s /q dist
)

if exist benchmark_PY.spec (
    echo Deleting benchmark_PY.spec...
    del /q benchmark_PY.spec
)

echo Building benchmark_CPP.cpp...
g++ -O2 -Wall -Wextra -g src\benchmark_CPP.cpp -o benchmark_CPP.exe
if %errorlevel% neq 0 (
    echo Failed to build benchmark_CPP!
    goto end
)

echo Build completed successfully!
set "SUCCESS=true"

:end
if "%SUCCESS%"=="true" (
    endlocal
    exit /b 0
) else (
    echo.
    echo Press any key to exit...
    pause >nul
    endlocal
    exit /b 1
)