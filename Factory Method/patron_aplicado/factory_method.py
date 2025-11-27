"""
Factory Method Pattern - Aplicación Correcta
=============================================
Sistema de delivery de hamburguesas usando Factory Method.

El Factory Method es un patrón creacional que:
- Usa HERENCIA para delegar la creación a subclases
- Las subclases deciden qué clase instanciar
- El creador (Restaurant) no conoce los tipos concretos
- Cumple con OCP: cerrado para modificación, abierto para extensión
"""

from abc import ABC, abstractmethod


# ============================================
# PRODUCTO ABSTRACTO (Interfaz)
# ============================================

class Burger(ABC):
    """
    Interfaz del producto: Define el contrato común para
    todas las hamburguesas.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.ingredients = []
    
    @abstractmethod
    def prepare(self) -> str:
        """Preparar la hamburguesa con sus ingredientes"""
        pass
    
    @abstractmethod
    def cook(self) -> str:
        """Cocinar la hamburguesa"""
        pass
    
    def box(self) -> str:
        """Empacar la hamburguesa (comportamiento común)"""
        return f"📦 Empacando {self.name} para delivery..."
    
    def serve(self) -> str:
        """Entregar la hamburguesa (comportamiento común)"""
        return f"✅ {self.name} lista para entregar!"


# ============================================
# PRODUCTOS CONCRETOS
# ============================================

class BeefBurger(Burger):
    """Producto concreto: Hamburguesa de carne de res"""
    
    def __init__(self):
        super().__init__("Beef Burger")
        self.ingredients = ["pan", "carne de res 200g", "lechuga", "tomate", "queso cheddar"]
    
    def prepare(self) -> str:
        return f"🍔 Preparando {self.name} con: {', '.join(self.ingredients)}"
    
    def cook(self) -> str:
        return f"🔥 Asando carne de res a la parrilla por 8 minutos..."


class VeggieBurger(Burger):
    """Producto concreto: Hamburguesa vegetariana"""
    
    def __init__(self):
        super().__init__("Veggie Burger")
        self.ingredients = ["pan integral", "hamburguesa de lentejas", "aguacate", "espinaca", "tomate"]
    
    def prepare(self) -> str:
        return f"🥗 Preparando {self.name} con: {', '.join(self.ingredients)}"
    
    def cook(self) -> str:
        return f"🔥 Cocinando hamburguesa de lentejas por 6 minutos..."


class ChickenBurger(Burger):
    """Producto concreto: Hamburguesa de pollo"""
    
    def __init__(self):
        super().__init__("Chicken Burger")
        self.ingredients = ["pan brioche", "pechuga empanizada", "mayonesa", "pepinillos", "lechuga"]
    
    def prepare(self) -> str:
        return f"🍗 Preparando {self.name} con: {', '.join(self.ingredients)}"
    
    def cook(self) -> str:
        return f"🔥 Friendo pechuga de pollo empanizada por 10 minutos..."


# ============================================
# CREADOR ABSTRACTO (Factory Method Pattern)
# ============================================

class Restaurant(ABC):
    """
    Creador abstracto: Define el Factory Method que las
    subclases deben implementar.
    
    NOTA IMPORTANTE: El creador NO es solo una fábrica.
    También contiene la lógica de negocio (order_burger)
    que USA los productos creados por el factory method.
    """
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def create_burger(self) -> Burger:
        """
        FACTORY METHOD: Las subclases implementan este método
        para crear el tipo específico de hamburguesa.
        
        Este es el corazón del patrón.
        """
        pass
    
    def order_burger(self) -> Burger:
        """
        Lógica de negocio que USA el Factory Method.
        
        Este método NO sabe qué tipo concreto de hamburguesa
        se creará - solo trabaja con la interfaz Burger.
        """
        # Llama al Factory Method (implementado por subclases)
        burger = self.create_burger()
        
        # Usa el producto a través de su interfaz abstracta
        print(burger.prepare())
        print(burger.cook())
        print(burger.box())
        print(burger.serve())
        
        return burger


# ============================================
# CREADORES CONCRETOS
# ============================================

class BeefBurgerRestaurant(Restaurant):
    """
    Creador concreto: Restaurante especializado en Beef Burgers.
    Implementa el Factory Method para crear BeefBurger.
    """
    
    def __init__(self):
        super().__init__("Beef Burger Palace")
    
    def create_burger(self) -> Burger:
        """Implementación del Factory Method"""
        return BeefBurger()


class VeggieBurgerRestaurant(Restaurant):
    """
    Creador concreto: Restaurante especializado en Veggie Burgers.
    Implementa el Factory Method para crear VeggieBurger.
    """
    
    def __init__(self):
        super().__init__("Green Veggie House")
    
    def create_burger(self) -> Burger:
        """Implementación del Factory Method"""
        return VeggieBurger()


class ChickenBurgerRestaurant(Restaurant):
    """
    Creador concreto: Restaurante especializado en Chicken Burgers.
    Implementa el Factory Method para crear ChickenBurger.
    """
    
    def __init__(self):
        super().__init__("Chicken Corner")
    
    def create_burger(self) -> Burger:
        """Implementación del Factory Method"""
        return ChickenBurger()


# ============================================
# CÓDIGO CLIENTE
# ============================================

def client_code(restaurant: Restaurant):
    """
    Función cliente que trabaja con cualquier restaurante.
    
    No conoce los tipos concretos de hamburguesas ni restaurantes.
    Solo depende de las abstracciones (Restaurant, Burger).
    """
    print(f"\n🏪 Ordenando en: {restaurant.name}")
    print("-" * 40)
    restaurant.order_burger()


# ============================================
# EXTENSIBILIDAD: Agregar nuevo tipo SIN modificar código existente
# ============================================

class FishBurger(Burger):
    """
    NUEVO producto: Agregado SIN modificar las clases existentes.
    """
    
    def __init__(self):
        super().__init__("Fish Burger")
        self.ingredients = ["pan de sésamo", "filete de pescado empanizado", "salsa tártara", "lechuga"]
    
    def prepare(self) -> str:
        return f"🐟 Preparando {self.name} con: {', '.join(self.ingredients)}"
    
    def cook(self) -> str:
        return f"🔥 Friendo filete de pescado por 7 minutos..."


class FishBurgerRestaurant(Restaurant):
    """
    NUEVO creador: Agregado SIN modificar las clases existentes.
    
    ✓ Esto demuestra el Principio Abierto/Cerrado (OCP):
      - Abierto para EXTENSIÓN (agregamos nuevas clases)
      - Cerrado para MODIFICACIÓN (no tocamos código existente)
    """
    
    def __init__(self):
        super().__init__("Ocean Fish & Chips")
    
    def create_burger(self) -> Burger:
        return FishBurger()


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  FACTORY METHOD PATTERN - RESTAURANTE DE HAMBURGUESAS")
    print("=" * 60)
    
    # El cliente puede usar cualquier restaurante sin conocer
    # los tipos concretos de hamburguesas
    
    print("\n>>> Pedido 1: Beef Burger")
    beef_restaurant = BeefBurgerRestaurant()
    client_code(beef_restaurant)
    
    print("\n>>> Pedido 2: Veggie Burger")
    veggie_restaurant = VeggieBurgerRestaurant()
    client_code(veggie_restaurant)
    
    print("\n>>> Pedido 3: Chicken Burger")
    chicken_restaurant = ChickenBurgerRestaurant()
    client_code(chicken_restaurant)
    
    print("\n>>> Pedido 4: Fish Burger (NUEVO - agregado sin modificar código)")
    fish_restaurant = FishBurgerRestaurant()
    client_code(fish_restaurant)
