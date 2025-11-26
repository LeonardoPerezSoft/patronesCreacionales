# CÓMO EJECUTAR LOS EJEMPLOS

## Opción 1: Script de Ejecución (RECOMENDADO)

### En Windows Command Prompt:
```
ejecutar.bat
```

### En Windows PowerShell:
```
.\ejecutar.ps1
```

## Opción 2: Terminal Directa

### Configurar PYTHONIOENCODING (Importante en Windows):
```
set PYTHONIOENCODING=utf-8
```

### Ejecutar el script principal:
```
python main.py
```

## Opción 3: Ejecutar Ejemplos Individuales

### Ver SIN Singleton (el problema):
```
set PYTHONIOENCODING=utf-8
python examples/ejemplo_gestor_impresion_sin_singleton.py
```

### Ver CON Singleton (la solucion):
```
set PYTHONIOENCODING=utf-8
python examples/ejemplo_gestor_impresion.py
```

## Leer la Documentación

### Comparación completa:
```
examples/README_COMPARACION.md
```

### Mapas mentales visuales:
```
examples/MAPAS_MENTALES_SINGLETON.md
```

### Resumen ejecutivo:
```
RESUMEN_GESTOR_IMPRESION.md
```

---

**NOTA IMPORTANTE**: Si ves caracteres extraños en la consola, es porque falta configurar PYTHONIOENCODING=utf-8.

Los scripts `ejecutar.bat` y `ejecutar.ps1` lo hacen automáticamente.
