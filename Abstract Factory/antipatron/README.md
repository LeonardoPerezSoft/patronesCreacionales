# ❌ Antipatrón - Mala Aplicación del Abstract Factory

## Descripción

Este directorio contiene ejemplos de **malas implementaciones** del patrón Abstract Factory. El código funciona pero viola principios de diseño importantes, lo que resulta en código difícil de mantener y extender.

## Caso de uso

Se intenta crear el mismo sistema de UI multiplataforma, pero con enfoques problemáticos.

## Estructura del código

```
antipatron/
├── README.md          # Este archivo
└── antipatron.py      # Código con malas prácticas
```

## Problemas demostrados

### 1. 🔴 Fábrica con condicionales (Switch/If-Else Factory)

```python
# ❌ MALO: Condicionales en lugar de polimorfismo
class BadGUIFactory:
    def __init__(self, os_type: str):
        self.os_type = os_type
    
    def create_button(self):
        if self.os_type == "windows":
            return BadWindowsButton()
        elif self.os_type == "macos":
            return BadMacOSButton()
        elif self.os_type == "linux":
            return BadLinuxButton()
        # ❌ Cada nuevo SO = más elif
```

**Problemas:**
- Viola el Principio Abierto/Cerrado (OCP)
- Agregar un nuevo SO requiere modificar la fábrica existente
- Propenso a errores al olvidar casos

### 2. 🔴 Productos sin interfaz común

```python
# ❌ MALO: Métodos con nombres inconsistentes
class BadWindowsButton:
    def pintar(self):  # ← Nombre diferente
        return "[Windows]"

class BadMacOSButton:
    def render(self):  # ← Nombre diferente
        return "(macOS)"

class BadLinuxButton:
    def dibujar(self):  # ← Nombre diferente
        return "<Linux>"
```

**Problemas:**
- El cliente debe saber qué método llamar para cada tipo
- No se puede usar polimorfismo
- Violación del Principio de Sustitución de Liskov (LSP)

### 3. 🔴 Cliente acoplado a implementaciones

```python
# ❌ MALO: El cliente conoce los tipos concretos
def render_ui(self):
    if self._factory.os_type == "windows":
        self._button.pintar()
    elif self._factory.os_type == "macos":
        self._button.render()
    elif self._factory.os_type == "linux":
        self._button.dibujar()
```

**Problemas:**
- El cliente está acoplado a cada implementación
- Código frágil que se rompe con cambios
- Difícil de testear

### 4. 🔴 Fábrica "God Class"

```python
# ❌ MALO: Fábrica que hace demasiado
class TerribleFactory:
    def __init__(self, os_type, theme, language):
        self.os_type = os_type
        self.theme = theme
        self.language = language
        self._log_file = None  # ❌ No debería estar aquí
        self._cache = {}       # ❌ No debería estar aquí
    
    def create_button(self):
        self._log("Creando botón...")  # ❌ Logging aquí
        btn = ...
        btn.dark_mode = True  # ❌ Configuración aquí
        self._cache["btn"] = btn  # ❌ Caching aquí
        return btn
```

**Problemas:**
- Viola el Principio de Responsabilidad Única (SRP)
- Mezcla creación con logging, caching, configuración
- Difícil de entender y mantener

## Instrucciones de ejecución

### Requisitos previos

- Python 3.7 o superior
- No requiere dependencias externas

### Ejecutar el ejemplo

```bash
# Navegar al directorio
cd "Abstract Factory/antipatron"

# Ejecutar el script
python antipatron.py
```

### Salida esperada

```
============================================================
  DEMOSTRACIÓN DEL ANTIPATRÓN
============================================================

>>> Usando la fábrica mal diseñada:
==================================================
INTERFAZ (ANTIPATRÓN)
==================================================
...

============================================================
  PROBLEMAS DE ESTE ANTIPATRÓN
============================================================
    ✗ Agregar un nuevo SO requiere modificar MÚLTIPLES clases
    ✗ El código cliente está acoplado a implementaciones concretas
    ✗ Los productos no comparten una interfaz común
    ...
```

## Señales de alerta (Code Smells)

¿Cómo detectar que estás implementando mal el patrón?

| Señal | Descripción |
|-------|-------------|
| `if/elif/else` en fábricas | Usar condicionales para decidir qué crear |
| `isinstance()` o `type()` | Verificar tipos en el cliente |
| Nombres de métodos diferentes | Productos similares con interfaces distintas |
| Fábrica con estado | La fábrica almacena más que lo necesario |
| Cliente modifica productos | El cliente "arregla" los productos después de crearlos |

## Comparación: Antipatrón vs Patrón correcto

| Aspecto | ❌ Antipatrón | ✅ Patrón correcto |
|---------|--------------|-------------------|
| Agregar nuevo SO | Modificar múltiples clases | Agregar nuevas clases |
| Interfaz de productos | Inconsistente | Uniforme |
| Acoplamiento cliente | Alto (conoce concretas) | Bajo (solo abstracciones) |
| Testabilidad | Difícil | Fácil con mocks |
| Mantenibilidad | Baja | Alta |

## Cómo corregir el antipatrón

1. **Crear interfaces abstractas** para todos los productos
2. **Hacer que los productos implementen** las interfaces
3. **Crear una fábrica abstracta** con métodos de creación
4. **Crear fábricas concretas** para cada familia
5. **El cliente solo depende de abstracciones**

Ver [`../patron_aplicado/`](../patron_aplicado/) para la implementación correcta.
