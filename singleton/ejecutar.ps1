# Script para ejecutar los ejemplos del Singleton - Gestor de Impresion
# Configura la codificacion correcta para Windows

$env:PYTHONIOENCODING='utf-8'

Set-Location (Get-Item $PSScriptRoot).FullName

Write-Host "`n"
Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "  DEMOSTRACION: GESTOR DE IMPRESION - SINGLETON vs SIN SINGLETON" -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "`n"

# Ejecutar main.py
python main.py

Write-Host "`n"
Write-Host "Presiona cualquier tecla para continuar..."
$null = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
