# Simple Factory Idiom (No es un Patrón Completo)

## Descripción

El **Simple Factory** es un idiom común en programación que encapsula la creación de objetos en una clase separada llamada "Factory". Sin embargo, **NO es un patrón de diseño oficial** porque la fábrica sigue abierta para modificación.

## ¿Por qué se llama "Factory"?

Porque es una clase cuya **única responsabilidad** es crear hamburguesas - es una **fábrica de hamburguesas**.

## Estructura

```
┌─────────────────┐
│   Restaurant    │ (Cliente)
│─────────────────│
│ + order_burger()│
└────────┬────────┘
         │ usa
         ▼
┌─────────────────┐
│  BurgerFactory  │ (Simple Factory)
│─────────────────│
│ + create_burger()│  ← Único lugar donde se conocen los tipos concretos
└────────┬────────┘
         │ crea
         ▼
┌─────────────────┐
│     Burger      │ (Producto Abstracto)
└────────┬────────┘
         │
    ┌────┼────┐
    ▼    ▼    ▼
  Beef Veggie Chicken
```

## Ventajas sobre el Código Sin Patrón

### 1. Separación de Responsabilidades
```python
# ANTES: Restaurant creaba hamburguesas directamente
class Restaurant:
    def order_burger(self, type):
        if type == "beef":
            burger = BeefBurger()  # ← Acoplado
        ...

# DESPUÉS: Delega a la fábrica
class Restaurant:
    def order_burger(self, type):
        burger = self.factory.create_burger(type)  # ← Desacoplado
```

### 2. Un Solo Lugar para la Creación
```python
class BurgerFactory:
    @staticmethod
    def create_burger(burger_type: str) -> Burger:
        # Toda la lógica de creación está aquí
        if burger_type == "beef":
            return BeefBurger()
        elif burger_type == "veggie":
            return VeggieBurger()
        ...
```

### 3. El Cliente No Conoce Tipos Concretos
```python
def order_burger(self, burger_type: str) -> Burger:
    burger = self.factory.create_burger(burger_type)
    
    # Solo usa la interfaz Burger
    burger.prepare()  # No sabe si es Beef, Veggie, o Chicken
    burger.cook()
    burger.serve()
```

## Limitaciones

### La Fábrica Sigue Abierta para Modificación

```python
class BurgerFactory:
    def create_burger(self, burger_type: str) -> Burger:
        if burger_type == "beef":
            return BeefBurger()
        elif burger_type == "veggie":
            return VeggieBurger()
        elif burger_type == "chicken":  # ← Nuevo tipo = modificar código
            return ChickenBurger()
        # elif burger_type == "fish":   # ← Futuro cambio
        #     return FishBurger()
```

**Cada nuevo tipo de hamburguesa requiere agregar un nuevo `elif`.**

Esto viola el **Principio Abierto/Cerrado (OCP)**:
> "Las entidades de software deben estar abiertas para extensión, pero cerradas para modificación."

## Ejecución

```bash
python antipatron.py
```

## ¿Cuándo Usar Simple Factory?

- Cuando la cantidad de productos es **pequeña y estable**
- Cuando la simplicidad es más importante que la extensibilidad
- Como paso intermedio antes de implementar Factory Method

## Siguiente Paso

Para resolver la limitación del Simple Factory, aplicamos el **Factory Method Pattern** que usa **herencia** para delegar la creación a subclases.

Ver la carpeta `patron_aplicado/` para la implementación completa.
