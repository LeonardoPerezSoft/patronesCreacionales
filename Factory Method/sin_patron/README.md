# Sin Patrón - Código Acoplado

## Descripción

Este ejemplo muestra el código de una aplicación de delivery de hamburguesas **SIN aplicar ningún patrón de diseño**. El código tiene problemas de acoplamiento y viola varios principios SOLID.

## Problema

Imagina que tienes un restaurante de hamburguesas y creaste una aplicación de delivery. El código que respalda la entrega y producción de estas hamburguesas se escribe de la siguiente manera:

1. Después de recibir la solicitud del cliente, la aplicación identifica el tipo de comida que necesita preparar
2. Basado en esta información, procede a crear el objeto correspondiente al tipo de hamburguesa
3. Lo prepara y lo devuelve al usuario

## Estructura del Código

```
Restaurant
    └── order_burger(burger_type)
            ├── if "beef" → BeefBurger()
            ├── if "veggie" → VeggieBurger()
            └── if "chicken" → ChickenBurger()
```

## Problemas Identificados

### 1. Viola el Principio Abierto/Cerrado (OCP)
```python
# Cada nuevo tipo = nuevo elif
if burger_type == "beef":
    burger = BeefBurger()
elif burger_type == "veggie":
    burger = VeggieBurger()
elif burger_type == "chicken":  # ← Agregado después
    burger = ChickenBurger()
# elif burger_type == "fish":    # ← Futuro cambio
#     burger = FishBurger()
```

### 2. Viola el Principio de Responsabilidad Única (SRP)
La clase `Restaurant` tiene múltiples responsabilidades:
- Crear hamburguesas (debería estar separado)
- Procesar pedidos
- Manejar la lógica de negocio

### 3. Código Duplicado
```python
def order_burger(self, burger_type):
    # Lógica de creación aquí...
    
def order_combo(self, burger_type):
    # MISMA lógica de creación duplicada aquí...
```

### 4. Alto Acoplamiento
- `Restaurant` conoce **TODOS** los tipos concretos
- Difícil de testear (no se pueden inyectar mocks)
- Difícil de reutilizar en otros contextos

## Ejecución

```bash
python sin_patron.py
```

## ¿Cuándo se vuelve problemático?

Cuando el restaurante crece y cambia con el tiempo:
- Agregar nuevas recetas al menú
- Eliminar productos del menú
- Diferentes estilos de preparación (Italian, Mexican, etc.)

**El código que varía (la creación de hamburguesas) está mezclado con el código estable (la lógica de negocio).**

## Siguiente Paso

Ver la carpeta `antipatron/` para entender el **Simple Factory Idiom** (que aunque mejora la situación, aún no es un patrón completo).
