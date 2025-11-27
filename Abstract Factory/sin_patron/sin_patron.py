"""
Sin Patrón - Código sin aplicar Abstract Factory
=================================================
Este código muestra cómo se vería la misma funcionalidad
SIN usar el patrón Abstract Factory.
"""


# ============================================
# CREACIÓN DIRECTA DE OBJETOS
# Sin abstracción, el cliente crea todo directamente
# ============================================

class WindowsButton:
    """Botón de Windows - clase concreta"""
    
    def render(self):
        return "[====== Botón Windows ======]"
    
    def on_click(self, callback):
        return f"Windows: Ejecutando '{callback}'"


class WindowsCheckbox:
    """Checkbox de Windows - clase concreta"""
    
    def __init__(self):
        self._checked = False
    
    def render(self):
        mark = "☑" if self._checked else "☐"
        return f"{mark} Checkbox Windows"
    
    def toggle(self):
        self._checked = not self._checked
        return f"Windows Checkbox: {'activado' if self._checked else 'desactivado'}"


class WindowsTextInput:
    """Input de Windows - clase concreta"""
    
    def __init__(self):
        self._value = ""
    
    def render(self):
        return f"|____{self._value}____| (Windows)"
    
    def set_value(self, value):
        self._value = value
        return f"Windows Input: '{value}'"


class MacOSButton:
    """Botón de macOS - clase concreta"""
    
    def render(self):
        return "( ●  Botón macOS  ● )"
    
    def on_click(self, callback):
        return f"macOS: Ejecutando '{callback}'"


class MacOSCheckbox:
    """Checkbox de macOS - clase concreta"""
    
    def __init__(self):
        self._checked = False
    
    def render(self):
        mark = "✓" if self._checked else "○"
        return f"({mark}) Checkbox macOS"
    
    def toggle(self):
        self._checked = not self._checked
        return f"macOS Checkbox: {'activado' if self._checked else 'desactivado'}"


class MacOSTextInput:
    """Input de macOS - clase concreta"""
    
    def __init__(self):
        self._value = ""
    
    def render(self):
        return f"⌜ {self._value} ⌟ (macOS)"
    
    def set_value(self, value):
        self._value = value
        return f"macOS Input: '{value}'"


# ============================================
# CÓDIGO CLIENTE SIN PATRÓN
# El cliente está acoplado a clases concretas
# ============================================

class ApplicationWindows:
    """
    Aplicación específica para Windows.
    
    PROBLEMA: Si queremos soportar macOS, necesitamos 
    DUPLICAR toda esta clase o llenarla de condicionales.
    """
    
    def __init__(self):
        # Creación directa - alto acoplamiento
        self._button = WindowsButton()
        self._checkbox = WindowsCheckbox()
        self._text_input = WindowsTextInput()
    
    def render_ui(self):
        output = []
        output.append("=" * 50)
        output.append("APLICACIÓN WINDOWS (SIN PATRÓN)")
        output.append("=" * 50)
        output.append(f"Botón: {self._button.render()}")
        output.append(f"Checkbox: {self._checkbox.render()}")
        output.append(f"Input: {self._text_input.render()}")
        output.append("=" * 50)
        return "\n".join(output)
    
    def interact(self):
        output = []
        output.append("\n--- Interacción ---")
        output.append(self._button.on_click("guardar"))
        output.append(self._checkbox.toggle())
        output.append(self._text_input.set_value("Hola"))
        return "\n".join(output)


class ApplicationMacOS:
    """
    Aplicación específica para macOS.
    
    PROBLEMA: Es casi idéntica a ApplicationWindows.
    ¡Código duplicado!
    """
    
    def __init__(self):
        # Creación directa - alto acoplamiento
        self._button = MacOSButton()
        self._checkbox = MacOSCheckbox()
        self._text_input = MacOSTextInput()
    
    def render_ui(self):
        output = []
        output.append("=" * 50)
        output.append("APLICACIÓN MACOS (SIN PATRÓN)")
        output.append("=" * 50)
        output.append(f"Botón: {self._button.render()}")
        output.append(f"Checkbox: {self._checkbox.render()}")
        output.append(f"Input: {self._text_input.render()}")
        output.append("=" * 50)
        return "\n".join(output)
    
    def interact(self):
        output = []
        output.append("\n--- Interacción ---")
        output.append(self._button.on_click("guardar"))
        output.append(self._checkbox.toggle())
        output.append(self._text_input.set_value("Hola"))
        return "\n".join(output)


# ============================================
# ALTERNATIVA CON CONDICIONALES (También mala)
# ============================================

class ApplicationWithConditionals:
    """
    Intento de hacer una aplicación "flexible" sin usar el patrón.
    
    PROBLEMAS:
    - Condicionales por todos lados
    - Difícil de mantener
    - Viola el Principio Abierto/Cerrado
    """
    
    def __init__(self, os_type: str):
        self._os_type = os_type
        self._button = None
        self._checkbox = None
        self._text_input = None
        self._create_components()
    
    def _create_components(self):
        """
        Método lleno de condicionales.
        Cada nuevo SO = más condicionales.
        """
        if self._os_type == "windows":
            self._button = WindowsButton()
            self._checkbox = WindowsCheckbox()
            self._text_input = WindowsTextInput()
        elif self._os_type == "macos":
            self._button = MacOSButton()
            self._checkbox = MacOSCheckbox()
            self._text_input = MacOSTextInput()
        # Agregar Linux?
        # elif self._os_type == "linux":
        #     self._button = LinuxButton()  # No existe
        #     ... y así sucesivamente
        else:
            raise ValueError(f"SO no soportado: {self._os_type}")
    
    def render_ui(self):
        output = []
        output.append("=" * 50)
        output.append(f"APLICACIÓN {self._os_type.upper()} (CONDICIONALES)")
        output.append("=" * 50)
        output.append(f"Botón: {self._button.render()}")
        output.append(f"Checkbox: {self._checkbox.render()}")
        output.append(f"Input: {self._text_input.render()}")
        output.append("=" * 50)
        return "\n".join(output)
    
    def interact(self):
        output = []
        output.append("\n--- Interacción ---")
        output.append(self._button.on_click("guardar"))
        output.append(self._checkbox.toggle())
        output.append(self._text_input.set_value("Hola"))
        return "\n".join(output)


# ============================================
# FUNCIÓN DE CREACIÓN PROCEDURAL (También mala)
# ============================================

def create_ui_components(os_type: str):
    """
    Función procedural para crear componentes.
    
    PROBLEMAS:
    - No es orientada a objetos
    - Difícil de extender
    - No permite inyección de dependencias
    - Difícil de testear
    """
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
    """Función procedural para renderizar"""
    print("=" * 50)
    print("COMPONENTES (PROCEDURAL)")
    print("=" * 50)
    print(f"Botón: {components['button'].render()}")
    print(f"Checkbox: {components['checkbox'].render()}")
    print(f"Input: {components['text_input'].render()}")
    print("=" * 50)


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  CÓDIGO SIN EL PATRÓN ABSTRACT FACTORY")
    print("=" * 60)
    
    # Opción 1: Clases duplicadas
    print("\n>>> OPCIÓN 1: Clases específicas (duplicación)")
    print("-" * 50)
    
    win_app = ApplicationWindows()
    print(win_app.render_ui())
    print(win_app.interact())
    
    print("\n")
    mac_app = ApplicationMacOS()
    print(mac_app.render_ui())
    print(mac_app.interact())
    
    # Opción 2: Condicionales
    print("\n\n>>> OPCIÓN 2: Una clase con condicionales")
    print("-" * 50)
    
    app_cond = ApplicationWithConditionals("windows")
    print(app_cond.render_ui())
    
    # Opción 3: Procedural
    print("\n\n>>> OPCIÓN 3: Funciones procedurales")
    print("-" * 50)
    
    components = create_ui_components("macos")
    render_components(components)
    
    # Mostrar problemas
    print("\n" + "=" * 60)
    print("  PROBLEMAS DE NO USAR EL PATRÓN")
    print("=" * 60)
    print("""
    OPCIÓN 1 (Clases duplicadas):
    ✗ Código duplicado entre ApplicationWindows y ApplicationMacOS
    ✗ Cambios deben replicarse en múltiples lugares
    ✗ Número de clases crece exponencialmente
    
    OPCIÓN 2 (Condicionales):
    ✗ Cada nuevo SO requiere modificar la clase existente
    ✗ Viola el Principio Abierto/Cerrado
    ✗ La clase crece indefinidamente
    
    OPCIÓN 3 (Procedural):
    ✗ No aprovecha la orientación a objetos
    ✗ Difícil de extender
    ✗ No permite inyección de dependencias
    ✗ Difícil de testear unitariamente
    
    COMÚN A TODAS:
    ✗ Alto acoplamiento a clases concretas
    ✗ Difícil de mockear en tests
    ✗ No garantiza consistencia entre productos
    """)
    
    print("\n" + "=" * 60)
    print("  CUÁNDO NECESITAS ABSTRACT FACTORY")
    print("=" * 60)
    print("""
    Considera usar Abstract Factory cuando:
    
    ✓ Tu código necesita trabajar con familias de productos relacionados
    ✓ Quieres que el código cliente sea independiente de las clases concretas
    ✓ Necesitas garantizar que los productos de una familia sean compatibles
    ✓ Quieres facilitar la adición de nuevas familias de productos
    ✓ Necesitas que el sistema sea fácil de testear con mocks
    """)
