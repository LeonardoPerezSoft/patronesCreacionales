# ⚠️ Sin Patrón - Código sin Abstract Factory

## Descripción

Este directorio contiene código que implementa la misma funcionalidad **sin usar el patrón Abstract Factory**. El código funciona pero presenta problemas de diseño que se vuelven evidentes a medida que el sistema crece.

## Caso de uso

Se crea el mismo sistema de UI multiplataforma pero usando enfoques "inocentes" que parecen más simples inicialmente.

## Estructura del código

```
sin_patron/
├── README.md          # Este archivo
└── sin_patron.py      # Código sin el patrón
```

## Enfoques demostrados

### 1. 📁 Clases duplicadas por plataforma

```python
class ApplicationWindows:
    def __init__(self):
        self._button = WindowsButton()      # Acoplamiento directo
        self._checkbox = WindowsCheckbox()
        self._text_input = WindowsTextInput()
    
    def render_ui(self):
        # ... código para renderizar
    
    def interact(self):
        # ... código para interactuar

class ApplicationMacOS:
    def __init__(self):
        self._button = MacOSButton()        # Acoplamiento directo
        self._checkbox = MacOSCheckbox()
        self._text_input = MacOSTextInput()
    
    def render_ui(self):
        # ... CÓDIGO DUPLICADO
    
    def interact(self):
        # ... CÓDIGO DUPLICADO
```

**Problemas:**
- Código duplicado entre clases
- Cambios deben replicarse en múltiples lugares
- Número de clases crece con cada nuevo SO

### 2. 🔀 Una clase con condicionales

```python
class ApplicationWithConditionals:
    def __init__(self, os_type: str):
        self._os_type = os_type
        self._create_components()
    
    def _create_components(self):
        if self._os_type == "windows":
            self._button = WindowsButton()
            self._checkbox = WindowsCheckbox()
        elif self._os_type == "macos":
            self._button = MacOSButton()
            self._checkbox = MacOSCheckbox()
        # elif os_type == "linux":  ← Agregar más aquí
        else:
            raise ValueError(f"SO no soportado: {self._os_type}")
```

**Problemas:**
- Viola el Principio Abierto/Cerrado
- La clase crece indefinidamente
- Alto acoplamiento con clases concretas

### 3. 🔧 Enfoque procedural con funciones

```python
def create_ui_components(os_type: str):
    if os_type == "windows":
        return {
            "button": WindowsButton(),
            "checkbox": WindowsCheckbox(),
            "text_input": WindowsTextInput()
        }
    elif os_type == "macos":
        return {
            "button": MacOSButton(),
            "checkbox": MacOSCheckbox(),
            "text_input": MacOSTextInput()
        }
    else:
        raise ValueError(f"SO no soportado: {os_type}")

def render_components(components: dict):
    print(components['button'].render())
    print(components['checkbox'].render())
```

**Problemas:**
- No aprovecha la orientación a objetos
- Difícil de extender
- No permite inyección de dependencias
- Difícil de testear unitariamente

## Instrucciones de ejecución

### Requisitos previos

- Python 3.7 o superior
- No requiere dependencias externas

### Ejecutar el ejemplo

```bash
# Navegar al directorio
cd "Abstract Factory/sin_patron"

# Ejecutar el script
python sin_patron.py
```

### Salida esperada

```
============================================================
  CÓDIGO SIN EL PATRÓN ABSTRACT FACTORY
============================================================

>>> OPCIÓN 1: Clases específicas (duplicación)
--------------------------------------------------
==================================================
APLICACIÓN WINDOWS (SIN PATRÓN)
==================================================
Botón: [====== Botón Windows ======]
...

>>> OPCIÓN 2: Una clase con condicionales
--------------------------------------------------
...

>>> OPCIÓN 3: Funciones procedurales
--------------------------------------------------
...

============================================================
  PROBLEMAS DE NO USAR EL PATRÓN
============================================================
```

## Comparación de enfoques

| Criterio | Clases duplicadas | Condicionales | Procedural | Abstract Factory |
|----------|-------------------|---------------|------------|------------------|
| Duplicación de código | 🔴 Alta | 🟡 Media | 🟡 Media | 🟢 Ninguna |
| Acoplamiento | 🔴 Alto | 🔴 Alto | 🔴 Alto | 🟢 Bajo |
| Extensibilidad | 🔴 Baja | 🔴 Baja | 🔴 Baja | 🟢 Alta |
| Testabilidad | 🟡 Media | 🔴 Baja | 🔴 Baja | 🟢 Alta |
| Complejidad inicial | 🟢 Baja | 🟢 Baja | 🟢 Baja | 🟡 Media |
| Complejidad a largo plazo | 🔴 Alta | 🔴 Alta | 🔴 Alta | 🟢 Controlada |

## ¿Cuándo es aceptable NO usar el patrón?

El código sin patrón puede ser aceptable cuando:

| Situación | ¿Sin patrón? |
|-----------|--------------|
| Prototipo rápido o POC | ✅ Aceptable |
| Solo 2 familias y no crecerá | ✅ Posible |
| Proyecto pequeño y simple | ✅ Posible |
| Sistema en producción que crecerá | ❌ No recomendado |
| Múltiples desarrolladores | ❌ No recomendado |
| Necesidad de tests unitarios | ❌ No recomendado |

## Evolución del código

```
Sin Patrón (inicio)
    │
    ├─► Crece el sistema
    │       │
    │       ▼
    │   Código duplicado aumenta
    │       │
    │       ▼
    │   Condicionales se multiplican
    │       │
    │       ▼
    │   Bugs difíciles de rastrear
    │       │
    │       ▼
    │   Refactoring costoso
    │
    └─► Con patrón desde el inicio
            │
            ▼
        Agregar familias es simple
            │
            ▼
        Código organizado
            │
            ▼
        Fácil de mantener
```

## Refactoring hacia Abstract Factory

Si tienes código sin el patrón y necesitas refactorizarlo:

1. **Identificar productos** - ¿Qué objetos se crean?
2. **Identificar familias** - ¿Qué variantes existen?
3. **Extraer interfaces** - Crear clases abstractas para productos
4. **Crear fábrica abstracta** - Definir métodos de creación
5. **Implementar fábricas concretas** - Una por familia
6. **Actualizar cliente** - Usar abstracciones

Ver [`../patron_aplicado/`](../patron_aplicado/) para la implementación correcta.
