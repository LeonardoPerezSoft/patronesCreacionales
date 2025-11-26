@echo off
REM Script para ejecutar los ejemplos del Singleton - Gestor de Impresion
REM Configura la codificacion correcta para Windows

setlocal enabledelayedexpansion

REM Establecer PYTHONIOENCODING para UTF-8
set PYTHONIOENCODING=utf-8

REM Cambiar al directorio del proyecto
cd /d "%~dp0"

echo.
echo =====================================================================
echo  DEMOSTRACION: GESTOR DE IMPRESION - SINGLETON vs SIN SINGLETON
echo =====================================================================
echo.

REM Ejecutar main.py
python main.py

pause
