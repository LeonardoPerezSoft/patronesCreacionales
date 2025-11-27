"""
Antipatrón - Mala aplicación del Abstract Factory
==================================================
Este código muestra una MALA implementación del patrón Abstract Factory.

PROBLEMAS IDENTIFICADOS:
1. Violación del Principio de Responsabilidad Única (SRP)
2. Violación del Principio Abierto/Cerrado (OCP)
3. Uso excesivo de condicionales
4. Alto acoplamiento
5. Difícil de extender y mantener
"""


# ============================================
# PROBLEMA 1: Fábrica con toda la lógica
# ============================================

class BadGUIFactory:
    """
    ANTIPATRÓN: Fábrica que maneja toda la lógica de creación
    con condicionales en lugar de polimorfismo.
    """
    
    def __init__(self, os_type: str):
        # Almacenar el tipo de OS viola el principio de que
        # la fábrica debería ser intercambiable
        self.os_type = os_type
    
    def create_button(self):
        """
        MALO: Usa condicionales para determinar qué crear.
        Cada nuevo SO requiere modificar este método.
        """
        if self.os_type == "windows":
            return BadWindowsButton()
        elif self.os_type == "macos":
            return BadMacOSButton()
        elif self.os_type == "linux":
            return BadLinuxButton()
        # ¡Cada nuevo SO requiere agregar más elif!
        else:
            raise ValueError(f"OS no soportado: {self.os_type}")
    
    def create_checkbox(self):
        """
        MALO: Mismo problema - condicionales repetidos
        """
        if self.os_type == "windows":
            return BadWindowsCheckbox()
        elif self.os_type == "macos":
            return BadMacOSCheckbox()
        elif self.os_type == "linux":
            return BadLinuxCheckbox()
        else:
            raise ValueError(f"OS no soportado: {self.os_type}")
    
    def create_text_input(self):
        """
        MALO: Y otra vez más condicionales...
        """
        if self.os_type == "windows":
            return BadWindowsTextInput()
        elif self.os_type == "macos":
            return BadMacOSTextInput()
        elif self.os_type == "linux":
            return BadLinuxTextInput()
        else:
            raise ValueError(f"OS no soportado: {self.os_type}")


# ============================================
# PROBLEMA 2: Productos sin interfaz común clara
# ============================================

class BadWindowsButton:
    """
    MALO: No implementa ninguna interfaz abstracta.
    Los métodos tienen nombres inconsistentes.
    """
    
    def pintar(self):  # Nombre inconsistente con otras clases
        return "[Windows Button]"
    
    def click_windows(self, callback):  # Método específico de plataforma
        return f"Windows click: {callback}"


class BadMacOSButton:
    """
    MALO: Interfaz diferente a BadWindowsButton
    """
    
    def render(self):  # Nombre diferente a BadWindowsButton
        return "(macOS Button)"
    
    def on_click(self, callback):  # Nombre diferente
        return f"macOS click: {callback}"


class BadLinuxButton:
    """
    MALO: Otra interfaz diferente
    """
    
    def dibujar(self):  # ¡Otro nombre diferente!
        return "<Linux Button>"
    
    def ejecutar_click(self, callback):  # ¡Y otro más!
        return f"Linux click: {callback}"


class BadWindowsCheckbox:
    def pintar(self):
        return "[X] Windows"
    
    def cambiar_estado(self):
        return "Windows checkbox changed"


class BadMacOSCheckbox:
    def render(self):
        return "(✓) macOS"
    
    def toggle(self):
        return "macOS checkbox toggled"


class BadLinuxCheckbox:
    def mostrar(self):
        return "[*] Linux"
    
    def switch(self):
        return "Linux checkbox switched"


class BadWindowsTextInput:
    def pintar(self):
        return "|__Windows__|"
    
    def establecer_valor(self, val):
        return f"Windows: {val}"


class BadMacOSTextInput:
    def render(self):
        return "⌜ macOS ⌟"
    
    def set_value(self, val):
        return f"macOS: {val}"


class BadLinuxTextInput:
    def dibujar(self):
        return "[___Linux___]"
    
    def asignar(self, val):
        return f"Linux: {val}"


# ============================================
# PROBLEMA 3: Cliente acoplado a implementaciones
# ============================================

class BadApplication:
    """
    MALO: El cliente necesita conocer todos los tipos concretos
    y manejar las diferencias de interfaz con condicionales.
    """
    
    def __init__(self, factory: BadGUIFactory):
        self._factory = factory
        self._button = None
        self._checkbox = None
        self._text_input = None
    
    def create_ui(self):
        self._button = self._factory.create_button()
        self._checkbox = self._factory.create_checkbox()
        self._text_input = self._factory.create_text_input()
    
    def render_ui(self):
        """
        MALO: El cliente necesita saber qué tipo de objeto tiene
        para llamar al método correcto. ¡Código frágil!
        """
        output = []
        output.append("=" * 50)
        output.append("INTERFAZ (ANTIPATRÓN)")
        output.append("=" * 50)
        
        # Cada producto tiene métodos diferentes - necesitamos condicionales
        if self._factory.os_type == "windows":
            output.append(f"Botón: {self._button.pintar()}")
            output.append(f"Checkbox: {self._checkbox.pintar()}")
            output.append(f"Input: {self._text_input.pintar()}")
        elif self._factory.os_type == "macos":
            output.append(f"Botón: {self._button.render()}")
            output.append(f"Checkbox: {self._checkbox.render()}")
            output.append(f"Input: {self._text_input.render()}")
        elif self._factory.os_type == "linux":
            output.append(f"Botón: {self._button.dibujar()}")
            output.append(f"Checkbox: {self._checkbox.mostrar()}")
            output.append(f"Input: {self._text_input.dibujar()}")
        
        output.append("=" * 50)
        return "\n".join(output)
    
    def interact(self):
        """
        MALO: Más condicionales para la interacción
        """
        output = []
        output.append("\n--- Interacción (ANTIPATRÓN) ---")
        
        if self._factory.os_type == "windows":
            output.append(self._button.click_windows("accion"))
            output.append(self._checkbox.cambiar_estado())
            output.append(self._text_input.establecer_valor("texto"))
        elif self._factory.os_type == "macos":
            output.append(self._button.on_click("accion"))
            output.append(self._checkbox.toggle())
            output.append(self._text_input.set_value("texto"))
        elif self._factory.os_type == "linux":
            output.append(self._button.ejecutar_click("accion"))
            output.append(self._checkbox.switch())
            output.append(self._text_input.asignar("texto"))
        
        return "\n".join(output)


# ============================================
# PROBLEMA 4: Mezcla de responsabilidades
# ============================================

class TerribleFactory:
    """
    PEOR AÚN: Una fábrica que hace demasiadas cosas.
    Viola SRP completamente.
    """
    
    def __init__(self, os_type: str, theme: str, language: str):
        self.os_type = os_type
        self.theme = theme
        self.language = language
        self._log_file = None
        self._cache = {}
    
    def create_button(self):
        # Mezcla lógica de creación con logging, caching, traducción...
        self._log("Creando botón...")
        
        if self.os_type == "windows":
            btn = BadWindowsButton()
        else:
            btn = BadMacOSButton()
        
        # Aplica tema (no debería estar aquí)
        if self.theme == "dark":
            btn.dark_mode = True  # ¡Esto ni siquiera existe en la clase!
        
        # Cachea (no debería estar aquí)
        self._cache["last_button"] = btn
        
        return btn
    
    def _log(self, message):
        # Logging no debería estar en una fábrica
        print(f"[LOG] {message}")
    
    def translate(self, text):
        # Traducción no debería estar en una fábrica
        translations = {"Botón": {"en": "Button", "es": "Botón"}}
        return translations.get(text, {}).get(self.language, text)


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  DEMOSTRACIÓN DEL ANTIPATRÓN")
    print("=" * 60)
    
    print("\n>>> Usando la fábrica mal diseñada:")
    bad_factory = BadGUIFactory("windows")
    bad_app = BadApplication(bad_factory)
    bad_app.create_ui()
    print(bad_app.render_ui())
    print(bad_app.interact())
    
    print("\n>>> Cambiando a macOS:")
    bad_factory_mac = BadGUIFactory("macos")
    bad_app_mac = BadApplication(bad_factory_mac)
    bad_app_mac.create_ui()
    print(bad_app_mac.render_ui())
    print(bad_app_mac.interact())
    
    print("\n" + "=" * 60)
    print("  PROBLEMAS DE ESTE ANTIPATRÓN")
    print("=" * 60)
    print("""
    ✗ Agregar un nuevo SO requiere modificar MÚLTIPLES clases
    ✗ El código cliente está acoplado a implementaciones concretas
    ✗ Los productos no comparten una interfaz común
    ✗ Difícil de testear (no se pueden usar mocks fácilmente)
    ✗ Viola el Principio Abierto/Cerrado (OCP)
    ✗ Viola el Principio de Sustitución de Liskov (LSP)
    ✗ Alto costo de mantenimiento
    ✗ Código frágil y propenso a errores
    """)
    
    print("\n" + "=" * 60)
    print("  ¿CÓMO DETECTAR ESTE ANTIPATRÓN?")
    print("=" * 60)
    print("""
    Señales de alerta:
    
    1. if/elif/else para decidir qué objeto crear
    2. El cliente necesita saber el tipo concreto de los objetos
    3. Agregar nuevos tipos requiere modificar código existente
    4. Métodos con nombres inconsistentes entre clases similares
    5. isinstance() o type() para determinar comportamiento
    6. Fábricas que hacen más que solo crear objetos
    """)
