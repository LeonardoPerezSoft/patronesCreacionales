"""
Simple Factory Idiom (No es un patrón completo)
================================================
Sistema de delivery de hamburguesas usando Simple Factory.

El Simple Factory es un IDIOM común que encapsula la creación
de objetos, pero NO es un patrón de diseño oficial porque:
- La fábrica sigue abierta para modificación
- No usa herencia para delegar la creación

Es un paso intermedio hacia el Factory Method Pattern.
"""


# ============================================
# PRODUCTO ABSTRACTO (Interfaz común)
# ============================================

class Burger:
    """
    Clase base para todas las hamburguesas.
    
    Abstrae los productos en una sola clase/interfaz y
    extrae los comportamientos comunes.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.ingredients = []
    
    def prepare(self) -> str:
        """Preparar la hamburguesa con sus ingredientes"""
        return f"🍔 Preparando {self.name} con: {', '.join(self.ingredients)}"
    
    def cook(self) -> str:
        """Cocinar la hamburguesa"""
        return f"🔥 Cocinando {self.name}..."
    
    def box(self) -> str:
        """Empacar la hamburguesa"""
        return f"📦 Empacando {self.name} para delivery..."
    
    def serve(self) -> str:
        """Entregar la hamburguesa"""
        return f"✅ {self.name} lista para entregar!"


# ============================================
# PRODUCTOS CONCRETOS
# ============================================

class BeefBurger(Burger):
    """Hamburguesa de carne de res"""
    
    def __init__(self):
        super().__init__("Beef Burger")
        self.ingredients = ["pan", "carne de res", "lechuga", "tomate", "queso cheddar"]
    
    def cook(self) -> str:
        return f"🔥 Asando carne de res a la parrilla por 8 minutos..."


class VeggieBurger(Burger):
    """Hamburguesa vegetariana"""
    
    def __init__(self):
        super().__init__("Veggie Burger")
        self.ingredients = ["pan integral", "hamburguesa de lentejas", "aguacate", "espinaca"]
    
    def cook(self) -> str:
        return f"🔥 Cocinando hamburguesa de lentejas por 6 minutos..."


class ChickenBurger(Burger):
    """Hamburguesa de pollo"""
    
    def __init__(self):
        super().__init__("Chicken Burger")
        self.ingredients = ["pan brioche", "pechuga empanizada", "mayonesa", "pepinillos"]
    
    def cook(self) -> str:
        return f"🔥 Friendo pechuga de pollo empanizada por 10 minutos..."


# ============================================
# SIMPLE FACTORY (El Idiom)
# ============================================

class BurgerFactory:
    """
    Simple Factory: Encapsula la lógica de creación.
    
    ✓ VENTAJA: Centraliza la creación en un solo lugar
    ✓ VENTAJA: Sigue el Principio de Responsabilidad Única
    
    ⚠️ PROBLEMA: Sigue abierta para modificación
    ⚠️ PROBLEMA: Cada nuevo tipo requiere modificar create_burger()
    """
    
    @staticmethod
    def create_burger(burger_type: str) -> Burger:
        """
        Crea y retorna la hamburguesa solicitada.
        
        ⚠️ Este método sigue violando el Principio Abierto/Cerrado
        porque cada nuevo tipo de hamburguesa requiere un nuevo elif.
        """
        if burger_type == "beef":
            return BeefBurger()
        elif burger_type == "veggie":
            return VeggieBurger()
        elif burger_type == "chicken":
            return ChickenBurger()
        # ⚠️ PROBLEMA: Agregar nuevos tipos requiere modificar esta clase
        # elif burger_type == "fish":
        #     return FishBurger()
        else:
            raise ValueError(f"Tipo de hamburguesa '{burger_type}' no disponible")


# ============================================
# RESTAURANTE (Cliente de la Factory)
# ============================================

class Restaurant:
    """
    Restaurante que usa el Simple Factory.
    
    ✓ Ya no conoce los tipos concretos de hamburguesas
    ✓ Solo depende de la interfaz Burger
    ✓ Puede usar cualquier hamburguesa que implemente Burger
    """
    
    def __init__(self, name: str):
        self.name = name
        self.factory = BurgerFactory()  # ← Usa la fábrica
    
    def order_burger(self, burger_type: str) -> Burger:
        """
        El método ya no conoce los tipos concretos.
        Delega la creación a la fábrica.
        """
        # Delega la creación a la fábrica
        burger = self.factory.create_burger(burger_type)
        
        # Trabaja con la interfaz abstracta (Burger)
        print(burger.prepare())
        print(burger.cook())
        print(burger.box())
        print(burger.serve())
        
        return burger
    
    def order_combo(self, burger_type: str) -> Burger:
        """
        ✓ Ya no hay código duplicado de creación
        """
        burger = self.factory.create_burger(burger_type)
        
        print(f"\n🍟 COMBO: {burger.name} + Papas Fritas + Bebida")
        print(burger.prepare())
        print(burger.cook())
        print(burger.box())
        print(burger.serve())
        
        return burger


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  SIMPLE FACTORY IDIOM - RESTAURANTE DE HAMBURGUESAS")
    print("=" * 60)
    
    restaurant = Restaurant("Burger Palace")
    
    print(f"\n🏪 Bienvenido a {restaurant.name}")
    
    # Pedido 1: Hamburguesa de carne
    print("\n" + "-" * 40)
    print(">>> Cliente pide: Beef Burger")
    print("-" * 40)
    restaurant.order_burger("beef")
    
    # Pedido 2: Hamburguesa vegetariana
    print("\n" + "-" * 40)
    print(">>> Cliente pide: Veggie Burger")
    print("-" * 40)
    restaurant.order_burger("veggie")
    
    # Pedido 3: Combo de pollo
    print("\n" + "-" * 40)
    print(">>> Cliente pide: Combo de Chicken Burger")
    print("-" * 40)
    restaurant.order_combo("chicken")
