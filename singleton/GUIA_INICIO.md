# Guía de Inicio Rápido - Patrón Singleton (versión actual del proyecto)

Este repositorio contiene una versión pedagógica y simplificada del patrón Singleton. Se eliminó el soporte para las implementaciones por metaclase y por método de clase; la implementación activa es la basada en **decorador**.

**Estructura actual (resumen):**

```
singleton/
├── src/
│   ├── singleton_decorator.py   # Implementación usada en el proyecto
│   └── __init__.py
├── examples/
│   ├── ejemplo_gestor_impresion.py            # Gestor de impresión (Singleton)
│   ├── ejemplo_gestor_impresion_sin_singleton.py  # Contrajemplo sin Singleton
│   ├── DIAGRAMA_SECUENCIA_SINGLETON.MD        # Explicación + referencia a imagen
│   ├── diagrama_secuencia_singleton.png       # Diagrama (imagen embebible)
│   ├── MAPAS_MENTALES_SINGLETON.md
│   ├── README_COMPARACION.md
│   └── README_GESTOR_IMPRESION.md
├── tests/
│   └── test_singleton.py
├── main.py
├── quick_start.py
├── ejecutar.bat
├── ejecutar.ps1
├── COMO_EJECUTAR.md
├── README.md
└── RESUMEN_GESTOR_IMPRESION.md
```

La imagen del diagrama se encuentra en `examples/diagrama_secuencia_singleton.png`.

## Ejecución rápida

- Ejecutar el ejemplo del Gestor (Singleton):
```
python examples/ejemplo_gestor_impresion.py
```

- Ejecutar el contrajemplo (sin Singleton):
```
python examples/ejemplo_gestor_impresion_sin_singleton.py
```

- Ejecutar el `main` (script que coordina la demo):
```
python main.py
```

- En Windows, para asegurar salida UTF-8 y entorno correcto, usa los scripts:
```
.\ejecutar.bat
# o
#.\ejecutar.ps1
```
Los scripts establecen `PYTHONIOENCODING=utf-8` antes de ejecutar `main.py`.

## Tests

Ejecuta la suite de tests (implementación del decorador):
```
python -m unittest tests.test_singleton -v
```

Actualmente las pruebas están orientadas al enfoque por decorador (tests locales en `tests/test_singleton.py`).

## Qué quedó y qué se eliminó

- Queda: implementación por **decorador** (`src/singleton_decorator.py`), ejemplos centrados en el **Gestor de Impresión**, documentación y tests.
- Se eliminaron: implementaciones por **metaclase** y **método de clase** (líneas, ejemplos y archivos asociados fueron retirados para simplificar la demo).

## Recomendaciones rápidas

- Si quieres que la documentación incluya la imagen dentro del Markdown, puedo incrustarla en Base64 en `DIAGRAMA_SECUENCIA_SINGLETON.MD`.
- Si prefieres mantener una sola imagen embebida en Markdown, puedo convertir la imagen a Base64 e insertarla en `DIAGRAMA_SECUENCIA_SINGLETON.MD`.
- Para experimentar: abre `examples/ejemplo_gestor_impresion.py` y `examples/ejemplo_gestor_impresion_sin_singleton.py` y modifica los hilos/colas para ver comportamientos diferentes.

## Recursos

- Código principal del patrón: `src/singleton_decorator.py`
- Ejemplos: `examples/ejemplo_gestor_impresion.py`, `examples/ejemplo_gestor_impresion_sin_singleton.py`
- Tests: `tests/test_singleton.py`

Si quieres, puedo también renombrar el archivo de la imagen y actualizar las referencias en `DIAGRAMA_SECUENCIA_SINGLETON.MD`. ¿Lo hago ahora?
