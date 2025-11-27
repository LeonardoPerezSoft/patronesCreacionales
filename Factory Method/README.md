# Factory Method Pattern

## ¿Qué es el Factory Method?

El **Factory Method** es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, pero permite a las subclases alterar el tipo de objetos que se crearán.

> "Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar."

## Caso de Estudio: Restaurante de Hamburguesas

Imagina que tienes un restaurante de hamburguesas y creaste una aplicación de delivery. El código que respalda la entrega y producción de estas hamburguesas evoluciona a través de tres etapas:

## Estructura del Proyecto

```
factory method 2/
├── README.md                 ← Estás aquí
├── infobase.md               ← Transcripción del video explicativo
│
├── sin_patron/               ← ❌ Código problemático
│   ├── sin_patron.py
│   └── README.md
│
├── antipatron/               ← ⚠️ Simple Factory (paso intermedio)
│   ├── antipatron.py
│   └── README.md
│
└── patron_aplicado/          ← ✅ Factory Method correcto
    ├── factory_method.py
    └── README.md
```

## Evolución del Código

### 1️⃣ Sin Patrón ([`sin_patron/`](./sin_patron/))

**Problema**: El código está completamente acoplado.

```python
class Restaurant:
    def order_burger(self, burger_type: str):
        if burger_type == "beef":
            burger = BeefBurger()
        elif burger_type == "veggie":
            burger = VeggieBurger()
        elif burger_type == "chicken":  # ← Nuevo = modificar
            burger = ChickenBurger()
        ...
```

**Violaciones**:
- ❌ Principio Abierto/Cerrado (OCP)
- ❌ Principio de Responsabilidad Única (SRP)
- ❌ Código duplicado en múltiples métodos

---

### 2️⃣ Simple Factory Idiom ([`antipatron/`](./antipatron/))

**Mejora**: Extraemos la creación a una clase `BurgerFactory`.

```python
class BurgerFactory:
    @staticmethod
    def create_burger(burger_type: str) -> Burger:
        if burger_type == "beef":
            return BeefBurger()
        elif burger_type == "veggie":
            return VeggieBurger()
        ...
```

**Ventajas**:
- ✅ Centraliza la creación en un solo lugar
- ✅ Restaurant ya no conoce tipos concretos

**Limitaciones**:
- ⚠️ La fábrica sigue abierta para modificación
- ⚠️ No es un patrón de diseño oficial

---

### 3️⃣ Factory Method Pattern ([`patron_aplicado/`](./patron_aplicado/))

**Solución completa**: Usamos **herencia** para delegar la creación.

```python
class Restaurant(ABC):
    @abstractmethod
    def create_burger(self) -> Burger:  # Factory Method
        pass
    
    def order_burger(self) -> Burger:
        burger = self.create_burger()
        burger.prepare()
        burger.cook()
        return burger

class BeefBurgerRestaurant(Restaurant):
    def create_burger(self) -> Burger:
        return BeefBurger()
```

**Beneficios**:
- ✅ Cerrado para modificación, abierto para extensión (OCP)
- ✅ Las subclases deciden qué crear
- ✅ Agregar nuevos tipos sin tocar código existente


## 🎯 ¿Cuándo Usar Factory Method?

| Situación | Usar Factory Method |
|-----------|---------------------|
| No conoces los tipos exactos de objetos de antemano | ✅ Sí |
| Quieres que usuarios extiendan componentes internos | ✅ Sí |
| Necesitas separar construcción de uso | ✅ Sí |
| Productos son simples y pocos | ❌ Simple Factory basta |
| Necesitas familias de productos relacionados | ❌ Usar Abstract Factory |

### Cómo Identificar el Patrón

1. **Hay herencia** en los creadores
2. **Método abstracto** de creación en la clase base
3. **Subclases implementan** el método fábrica
4. **El creador no conoce** los tipos concretos

## Ejecutar los Ejemplos

```powershell
# Sin patrón
python ".\sin_patron\sin_patron.py"

# Simple Factory (antipatrón)
python ".\antipatron\antipatron.py"

# Factory Method (patrón aplicado)
python ".\patron_aplicado\factory_method.py"
```

## Próximo Paso: Abstract Factory

Cuando necesitas **familias de productos relacionados**, el patrón **Abstract Factory** es la solución. Ver la carpeta [`../Abstract Factory/`](../Abstract%20Factory/).
