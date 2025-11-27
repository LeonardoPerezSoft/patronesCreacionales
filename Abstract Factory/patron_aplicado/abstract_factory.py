"""
Abstract Factory Pattern - Aplicación Correcta
==============================================
Sistema de creación de interfaces gráficas multiplataforma.

Este ejemplo demuestra el patrón Abstract Factory creando familias
de componentes UI (botones, checkboxes, inputs) para diferentes 
sistemas operativos (Windows, macOS).
"""

from abc import ABC, abstractmethod


# ============================================
# PRODUCTOS ABSTRACTOS
# ============================================

class Button(ABC):
    """Producto abstracto: Botón"""
    
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def on_click(self, callback: str) -> str:
        pass


class Checkbox(ABC):
    """Producto abstracto: Checkbox"""
    
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def toggle(self) -> str:
        pass


class TextInput(ABC):
    """Producto abstracto: Campo de texto"""
    
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def set_value(self, value: str) -> str:
        pass


# ============================================
# PRODUCTOS CONCRETOS - WINDOWS
# ============================================

class WindowsButton(Button):
    """Botón estilo Windows"""
    
    def render(self) -> str:
        return "[====== Botón Windows ======]"
    
    def on_click(self, callback: str) -> str:
        return f"Windows: Ejecutando '{callback}' con efecto Aero"


class WindowsCheckbox(Checkbox):
    """Checkbox estilo Windows"""
    
    def __init__(self):
        self._checked = False
    
    def render(self) -> str:
        mark = "☑" if self._checked else "☐"
        return f"{mark} Checkbox Windows"
    
    def toggle(self) -> str:
        self._checked = not self._checked
        return f"Windows Checkbox: {'activado' if self._checked else 'desactivado'}"


class WindowsTextInput(TextInput):
    """Campo de texto estilo Windows"""
    
    def __init__(self):
        self._value = ""
    
    def render(self) -> str:
        return f"|____{self._value}____| (Windows Input)"
    
    def set_value(self, value: str) -> str:
        self._value = value
        return f"Windows Input: valor establecido a '{value}'"


# ============================================
# PRODUCTOS CONCRETOS - MACOS
# ============================================

class MacOSButton(Button):
    """Botón estilo macOS"""
    
    def render(self) -> str:
        return "( ●  Botón macOS  ● )"
    
    def on_click(self, callback: str) -> str:
        return f"macOS: Ejecutando '{callback}' con animación suave"


class MacOSCheckbox(Checkbox):
    """Checkbox estilo macOS"""
    
    def __init__(self):
        self._checked = False
    
    def render(self) -> str:
        mark = "✓" if self._checked else "○"
        return f"({mark}) Checkbox macOS"
    
    def toggle(self) -> str:
        self._checked = not self._checked
        return f"macOS Checkbox: {'activado' if self._checked else 'desactivado'}"


class MacOSTextInput(TextInput):
    """Campo de texto estilo macOS"""
    
    def __init__(self):
        self._value = ""
    
    def render(self) -> str:
        return f"⌜ {self._value} ⌟ (macOS Input)"
    
    def set_value(self, value: str) -> str:
        self._value = value
        return f"macOS Input: valor establecido a '{value}'"


# ============================================
# FÁBRICA ABSTRACTA
# ============================================

class GUIFactory(ABC):
    """
    Fábrica Abstracta: Define la interfaz para crear familias
    de productos relacionados (componentes UI).
    """
    
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
    
    @abstractmethod
    def create_text_input(self) -> TextInput:
        pass


# ============================================
# FÁBRICAS CONCRETAS
# ============================================

class WindowsFactory(GUIFactory):
    """Fábrica concreta: Crea componentes estilo Windows"""
    
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()
    
    def create_text_input(self) -> TextInput:
        return WindowsTextInput()


class MacOSFactory(GUIFactory):
    """Fábrica concreta: Crea componentes estilo macOS"""
    
    def create_button(self) -> Button:
        return MacOSButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()
    
    def create_text_input(self) -> TextInput:
        return MacOSTextInput()


# ============================================
# CÓDIGO CLIENTE
# ============================================

class Application:
    """
    Código cliente: Trabaja con fábricas y productos a través
    de interfaces abstractas, sin conocer las clases concretas.
    """
    
    def __init__(self, factory: GUIFactory):
        self._factory = factory
        self._button = None
        self._checkbox = None
        self._text_input = None
    
    def create_ui(self):
        """Crea todos los componentes UI usando la fábrica"""
        self._button = self._factory.create_button()
        self._checkbox = self._factory.create_checkbox()
        self._text_input = self._factory.create_text_input()
    
    def render_ui(self) -> str:
        """Renderiza todos los componentes"""
        output = []
        output.append("=" * 50)
        output.append("INTERFAZ DE USUARIO")
        output.append("=" * 50)
        output.append(f"Botón: {self._button.render()}")
        output.append(f"Checkbox: {self._checkbox.render()}")
        output.append(f"Input: {self._text_input.render()}")
        output.append("=" * 50)
        return "\n".join(output)
    
    def interact(self):
        """Simula interacción con los componentes"""
        output = []
        output.append("\n--- Interacción con componentes ---")
        output.append(self._button.on_click("guardar_datos"))
        output.append(self._checkbox.toggle())
        output.append(self._text_input.set_value("Hola Mundo"))
        output.append(f"\nEstado actualizado:")
        output.append(f"Checkbox: {self._checkbox.render()}")
        output.append(f"Input: {self._text_input.render()}")
        return "\n".join(output)


def get_factory(os_type: str) -> GUIFactory:
    """
    Función que determina qué fábrica usar según el sistema operativo.
    En una aplicación real, esto detectaría el SO automáticamente.
    """
    factories = {
        "windows": WindowsFactory,
        "macos": MacOSFactory
    }
    
    factory_class = factories.get(os_type.lower())
    if factory_class is None:
        raise ValueError(f"Sistema operativo '{os_type}' no soportado")
    
    return factory_class()


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  DEMOSTRACIÓN DEL PATRÓN ABSTRACT FACTORY")
    print("=" * 60)
    
    # Demostración con Windows
    print("\n>>> Creando aplicación para WINDOWS:")
    windows_factory = get_factory("windows")
    windows_app = Application(windows_factory)
    windows_app.create_ui()
    print(windows_app.render_ui())
    print(windows_app.interact())
    
    # Demostración con macOS
    print("\n\n>>> Creando aplicación para macOS:")
    macos_factory = get_factory("macos")
    macos_app = Application(macos_factory)
    macos_app.create_ui()
    print(macos_app.render_ui())
    print(macos_app.interact())

