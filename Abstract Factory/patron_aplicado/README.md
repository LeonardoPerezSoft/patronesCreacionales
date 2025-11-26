# ✅ Patrón Aplicado Correctamente - Abstract Factory

## Descripción

Este directorio contiene una implementación **correcta** del patrón Abstract Factory aplicado a un sistema de creación de interfaces gráficas multiplataforma.

## Caso de uso

Se simula la creación de componentes de UI (Botones, Checkboxes, Inputs de texto) para diferentes sistemas operativos:
- **Windows**: Componentes con estilo Windows
- **macOS**: Componentes con estilo macOS

## Estructura del código

```
patron_aplicado/
├── README.md              # Este archivo
└── abstract_factory.py    # Implementación del patrón
```

## Componentes implementados

### Productos Abstractos (Interfaces)

```python
class Button(ABC):
    @abstractmethod
    def render(self) -> str: pass
    
    @abstractmethod
    def on_click(self, callback: str) -> str: pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: pass
    
    @abstractmethod
    def toggle(self) -> str: pass

class TextInput(ABC):
    @abstractmethod
    def render(self) -> str: pass
    
    @abstractmethod
    def set_value(self, value: str) -> str: pass
```

### Fábrica Abstracta

```python
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox: pass
    
    @abstractmethod
    def create_text_input(self) -> TextInput: pass
```

### Fábricas Concretas

- `WindowsFactory`: Crea componentes estilo Windows
- `MacOSFactory`: Crea componentes estilo macOS

### Productos Concretos

| Tipo | Windows | macOS |
|------|---------|-------|
| Button | `WindowsButton` | `MacOSButton` |
| Checkbox | `WindowsCheckbox` | `MacOSCheckbox` |
| TextInput | `WindowsTextInput` | `MacOSTextInput` |

## Principios SOLID aplicados

| Principio | Cómo se aplica |
|-----------|----------------|
| **SRP** | Cada clase tiene una única responsabilidad |
| **OCP** | Agregar nuevas familias no modifica código existente |
| **LSP** | Las clases concretas son sustituibles por sus abstracciones |
| **ISP** | Las interfaces son específicas y cohesivas |
| **DIP** | El cliente depende de abstracciones, no de concretas |

## Instrucciones de ejecución

### Requisitos previos

- Python 3.7 o superior
- No requiere dependencias externas

### Ejecutar el ejemplo

```bash
# Navegar al directorio
cd "Abstract Factory/patron_aplicado"

# Ejecutar el script
python abstract_factory.py
```

### Salida esperada

```
============================================================
  DEMOSTRACIÓN DEL PATRÓN ABSTRACT FACTORY
============================================================

>>> Creando aplicación para WINDOWS:
==================================================
INTERFAZ DE USUARIO
==================================================
Botón: [====== Botón Windows ======]
Checkbox: ☐ Checkbox Windows
Input: |____| (Windows Input)
==================================================

--- Interacción con componentes ---
Windows: Ejecutando 'guardar_datos' con efecto Aero
Windows Checkbox: activado
Windows Input: valor establecido a 'Hola Mundo'
...
```

## Cómo extender el código

### Agregar un nuevo sistema operativo (Linux)

1. **Crear productos concretos** para Linux:

```python
class LinuxButton(Button):
    def render(self) -> str:
        return "< Linux Button >"
    
    def on_click(self, callback: str) -> str:
        return f"Linux: Ejecutando '{callback}' con GTK"
```

2. **Crear la fábrica concreta**:

```python
class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()
    
    def create_text_input(self) -> TextInput:
        return LinuxTextInput()
```

3. **Registrar la fábrica**:

```python
factories = {
    "windows": WindowsFactory,
    "macos": MacOSFactory,
    "linux": LinuxFactory  # ✅ Solo agregar esta línea
}
```

### Agregar un nuevo tipo de producto

Si necesitas agregar un nuevo componente (ej: `Slider`):

1. Crear interfaz abstracta `Slider`
2. Crear implementaciones concretas para cada SO
3. Agregar método `create_slider()` a `GUIFactory`
4. Implementar el método en cada fábrica concreta

## Beneficios demostrados

- ✅ El cliente (`Application`) no conoce clases concretas
- ✅ Garantiza que todos los componentes pertenezcan a la misma familia
- ✅ Fácil de testear con mock factories
- ✅ Cumple principios SOLID
