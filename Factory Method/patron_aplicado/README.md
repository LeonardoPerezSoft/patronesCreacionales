# Factory Method Pattern - Aplicación Correcta

## Descripción

El **Factory Method** es un patrón de diseño creacional que:
- Separa el código de construcción del producto del código que lo usa
- Usa **herencia** para delegar la creación a subclases
- Las subclases implementan el método fábrica para crear productos específicos

## Definición Formal

> El Factory Method define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar. Permite a una clase diferir la instanciación a sus subclases.

## Estructura UML

```
┌─────────────────────────┐         ┌─────────────────────┐
│      Restaurant         │         │       Burger        │
│      (Creator)          │         │     (Product)       │
│─────────────────────────│         │─────────────────────│
│ + order_burger()        │────────▶│ + prepare()         │
│ + create_burger() 🔧    │ usa     │ + cook()            │
│   [abstract]            │         │ + serve()           │
└───────────┬─────────────┘         └──────────┬──────────┘
            │                                   │
            │ hereda                            │ hereda
    ┌───────┴───────┐               ┌──────────┴──────────┐
    │               │               │                     │
    ▼               ▼               ▼                     ▼
┌─────────────┐ ┌─────────────┐ ┌───────────┐      ┌───────────┐
│BeefBurger   │ │VeggieBurger │ │BeefBurger │      │VeggieBurger│
│Restaurant   │ │Restaurant   │ └───────────┘      └───────────┘
│─────────────│ │─────────────│
│create_burger│ │create_burger│
│→ BeefBurger │ │→VeggieBurger│
└─────────────┘ └─────────────┘

🔧 = Factory Method
```

## Componentes del Patrón

### 1. Product (Burger)
```python
class Burger(ABC):
    """Interfaz común para todos los productos"""
    
    @abstractmethod
    def prepare(self) -> str:
        pass
    
    @abstractmethod
    def cook(self) -> str:
        pass
```

### 2. Concrete Products (BeefBurger, VeggieBurger, etc.)
```python
class BeefBurger(Burger):
    """Implementación concreta del producto"""
    
    def prepare(self) -> str:
        return "Preparando Beef Burger..."
    
    def cook(self) -> str:
        return "Asando carne a la parrilla..."
```

### 3. Creator (Restaurant)
```python
class Restaurant(ABC):
    """
    Declara el Factory Method.
    También contiene lógica de negocio que usa el producto.
    """
    
    @abstractmethod
    def create_burger(self) -> Burger:
        """Factory Method - las subclases lo implementan"""
        pass
    
    def order_burger(self) -> Burger:
        """Usa el Factory Method"""
        burger = self.create_burger()
        burger.prepare()
        burger.cook()
        return burger
```

### 4. Concrete Creators (BeefBurgerRestaurant, etc.)
```python
class BeefBurgerRestaurant(Restaurant):
    """Implementa el Factory Method para crear BeefBurger"""
    
    def create_burger(self) -> Burger:
        return BeefBurger()
```

## Cómo Identificar el Factory Method

El patrón Factory Method se identifica por:

1. **Herencia**: Hay una clase base abstracta con subclases
2. **Método abstracto de creación**: La clase base declara un método que las subclases implementan
3. **Las subclases deciden**: Cada subclase determina qué tipo concreto crear

## Diferencia con Simple Factory

| Simple Factory | Factory Method |
|----------------|----------------|
| Una clase con método estático | Clase abstracta con subclases |
| Sigue abierto para modificación | Cerrado para modificación |
| No usa herencia | Usa herencia |
| Más simple pero menos flexible | Más complejo pero más flexible |

## Extensibilidad (OCP en Acción)

Para agregar un nuevo tipo de hamburguesa:

```python
# 1. Crear nuevo producto (sin modificar código existente)
class FishBurger(Burger):
    def prepare(self): ...
    def cook(self): ...

# 2. Crear nuevo creador (sin modificar código existente)
class FishBurgerRestaurant(Restaurant):
    def create_burger(self) -> Burger:
        return FishBurger()
```

**¡No modificamos ninguna clase existente!**

## Ejecución

```bash
python factory_method.py
```

## ¿Cuándo Usar Factory Method?

1. **No conoces los tipos exactos** de objetos que tu código necesitará
2. **Quieres extensibilidad**: Que usuarios puedan extender componentes internos
3. **Quieres reutilizar** objetos existentes en lugar de reconstruirlos
4. **Separar construcción de uso** del producto

## Principios SOLID Cumplidos

- ✅ **SRP**: Cada creador tiene una sola responsabilidad
- ✅ **OCP**: Abierto para extensión, cerrado para modificación
- ✅ **LSP**: Las subclases pueden sustituir a la clase base
- ✅ **DIP**: Dependemos de abstracciones, no de clases concretas

## Próximo Paso: Abstract Factory

Cuando necesites **familias de productos relacionados** (ej: hamburguesas estilo Americano vs. Italiano), el patrón Abstract Factory es la solución.
