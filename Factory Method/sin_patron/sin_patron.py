"""
Sin Patrón - Código Acoplado
============================
Sistema de delivery de hamburguesas SIN aplicar ningún patrón.

Este código tiene todos los problemas típicos:
- Viola el Principio Abierto/Cerrado (OCP)
- Viola el Principio de Responsabilidad Única (SRP)
- Alto acoplamiento
- Difícil de mantener y extender
"""


# ============================================
# PRODUCTOS (Hamburguesas)
# ============================================

class BeefBurger:
    """Hamburguesa de carne de res"""
    
    def __init__(self):
        self.name = "Beef Burger"
        self.ingredients = ["pan", "carne de res", "lechuga", "tomate", "queso"]
    
    def prepare(self) -> str:
        return f"🍔 Preparando {self.name} con: {', '.join(self.ingredients)}"
    
    def cook(self) -> str:
        return f"🔥 Cocinando la carne de res a la parrilla..."
    
    def serve(self) -> str:
        return f"📦 {self.name} lista para entregar!"


class VeggieBurger:
    """Hamburguesa vegetariana"""
    
    def __init__(self):
        self.name = "Veggie Burger"
        self.ingredients = ["pan integral", "hamburguesa de lentejas", "aguacate", "tomate", "espinaca"]
    
    def prepare(self) -> str:
        return f"🥗 Preparando {self.name} con: {', '.join(self.ingredients)}"
    
    def cook(self) -> str:
        return f"🔥 Cocinando la hamburguesa de lentejas..."
    
    def serve(self) -> str:
        return f"📦 {self.name} lista para entregar!"


class ChickenBurger:
    """Hamburguesa de pollo"""
    
    def __init__(self):
        self.name = "Chicken Burger"
        self.ingredients = ["pan", "pechuga de pollo", "mayonesa", "lechuga", "pepinillos"]
    
    def prepare(self) -> str:
        return f"🍗 Preparando {self.name} con: {', '.join(self.ingredients)}"
    
    def cook(self) -> str:
        return f"🔥 Cocinando la pechuga de pollo..."
    
    def serve(self) -> str:
        return f"📦 {self.name} lista para entregar!"


# ============================================
# RESTAURANTE (Código Cliente Problemático)
# ============================================

class Restaurant:
    """
    Restaurante con código acoplado.
    
    PROBLEMAS:
    - El método order_burger conoce TODOS los tipos concretos
    - Cada nuevo tipo de hamburguesa requiere modificar este código
    - Viola OCP: abierto para modificación
    - Viola SRP: hace demasiadas cosas
    - Código duplicado si necesitamos crear hamburguesas en otros lugares
    """
    
    def __init__(self, name: str):
        self.name = name
    
    def order_burger(self, burger_type: str):
        """
        ⚠️ PROBLEMA: Este método tiene toda la lógica de creación
        mezclada con la lógica de negocio.
        
        Cada vez que agreguemos un nuevo tipo de hamburguesa,
        tenemos que modificar este método.
        """
        burger = None
        
        # ⚠️ PROBLEMA: Cadena de if-else que crece con cada nuevo producto
        if burger_type == "beef":
            burger = BeefBurger()
        elif burger_type == "veggie":
            burger = VeggieBurger()
        elif burger_type == "chicken":
            burger = ChickenBurger()
        # ⚠️ Cada nuevo tipo = nuevo elif aquí
        # elif burger_type == "fish":
        #     burger = FishBurger()
        # elif burger_type == "bbq":
        #     burger = BBQBurger()
        else:
            raise ValueError(f"Tipo de hamburguesa '{burger_type}' no disponible")
        
        # Lógica de negocio mezclada con creación
        print(burger.prepare())
        print(burger.cook())
        print(burger.serve())
        
        return burger
    
    def order_combo(self, burger_type: str):
        """
        ⚠️ PROBLEMA: Código duplicado de creación en otro método.
        Si agregamos un nuevo tipo, hay que modificar AMBOS métodos.
        """
        burger = None
        
        # ⚠️ MISMO código de creación duplicado
        if burger_type == "beef":
            burger = BeefBurger()
        elif burger_type == "veggie":
            burger = VeggieBurger()
        elif burger_type == "chicken":
            burger = ChickenBurger()
        else:
            raise ValueError(f"Tipo de hamburguesa '{burger_type}' no disponible")
        
        print(f"\n🍟 COMBO: {burger.name} + Papas + Bebida")
        print(burger.prepare())
        print(burger.cook())
        print(burger.serve())
        
        return burger


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  EJEMPLO SIN PATRÓN - RESTAURANTE DE HAMBURGUESAS")
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

