# 🏭 Abstract Factory Pattern

## Índice

1. [¿Qué es Abstract Factory?](#qué-es-abstract-factory)
2. [Problema que resuelve](#problema-que-resuelve)
3. [Estructura del patrón](#estructura-del-patrón)
4. [¿Cuándo usar Abstract Factory?](#cuándo-usar-abstract-factory)
5. [Ejemplos de código](#ejemplos-de-código)
6. [Ventajas y Desventajas](#ventajas-y-desventajas)
7. [Relación con otros patrones](#relación-con-otros-patrones)

---

## ¿Qué es Abstract Factory?

**Abstract Factory** es un patrón de diseño **creacional** que proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.

En otras palabras, es una "fábrica de fábricas" que permite crear objetos que pertenecen a una misma familia (por ejemplo, componentes de UI para Windows vs macOS) de manera consistente.

### Analogía del mundo real

Imagina una fábrica de muebles que produce diferentes estilos: **Moderno**, **Victoriano**, y **Art Deco**. Cada estilo tiene su propia línea de productos: sillas, mesas y sofás.

- Una **fábrica Moderna** produce: silla moderna + mesa moderna + sofá moderno
- Una **fábrica Victoriana** produce: silla victoriana + mesa victoriana + sofá victoriano

El cliente (la tienda) no necesita saber cómo se fabrican los muebles, solo necesita pedir productos a la fábrica correcta para garantizar que todos los muebles combinen entre sí.

---

## Problema que resuelve

### El problema

Supongamos que estás desarrollando una aplicación que debe funcionar en múltiples sistemas operativos (Windows, macOS, Linux). Cada SO tiene su propio estilo de componentes de interfaz gráfica.

**Sin el patrón**, tendrías que:

```python
# ❌ Código problemático
def crear_interfaz(sistema_operativo):
    if sistema_operativo == "windows":
        boton = BotonWindows()
        checkbox = CheckboxWindows()
        input = InputWindows()
    elif sistema_operativo == "macos":
        boton = BotonMacOS()
        checkbox = CheckboxMacOS()
        input = InputMacOS()
    elif sistema_operativo == "linux":
        boton = BotonLinux()
        checkbox = CheckboxLinux()
        input = InputLinux()
    # ... y así sucesivamente
```

### Problemas de este enfoque:

1. **Violación del Principio Abierto/Cerrado**: Cada nuevo SO requiere modificar el código existente
2. **Alto acoplamiento**: El código cliente conoce todas las clases concretas
3. **Riesgo de inconsistencia**: Podrías mezclar un botón de Windows con un checkbox de macOS
4. **Difícil de mantener**: Los condicionales crecen exponencialmente

### La solución

Abstract Factory resuelve esto creando una **interfaz abstracta** para la fábrica y **fábricas concretas** para cada familia de productos:

```python
# ✅ Con Abstract Factory
factory = obtener_fabrica(sistema_operativo)  # Retorna WindowsFactory o MacOSFactory
boton = factory.crear_boton()      # El tipo correcto automáticamente
checkbox = factory.crear_checkbox()
input = factory.crear_input()
```

---

## Estructura del patrón

> 📊 **RECOMENDACIÓN DE DIAGRAMA**: Aquí se recomienda incluir un **diagrama de clases UML** que muestre la estructura del patrón Abstract Factory.

### Componentes principales:

```
┌─────────────────────────────────────────────────────────────────┐
│                     ABSTRACT FACTORY                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────┐         ┌──────────────────┐              │
│  │  <<interface>>   │         │  <<interface>>   │              │
│  │  GUIFactory      │         │  Button          │              │
│  ├──────────────────┤         ├──────────────────┤              │
│  │ +createButton()  │────────▶│ +render()        │              │
│  │ +createCheckbox()│         │ +onClick()       │              │
│  │ +createInput()   │         └────────┬─────────┘              │
│  └────────┬─────────┘                  │                        │
│           │                            │                        │
│     ┌─────┴─────┐              ┌───────┴───────┐                │
│     │           │              │               │                │
│  ┌──▼───┐   ┌───▼──┐      ┌────▼───┐    ┌─────▼────┐           │
│  │Windows│   │macOS │      │Windows │    │  macOS   │           │
│  │Factory│   │Factor│      │ Button │    │  Button  │           │
│  └───────┘   └──────┘      └────────┘    └──────────┘           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Participantes:

| Componente | Descripción |
|------------|-------------|
| **Abstract Factory** | Interfaz que declara métodos para crear cada tipo de producto abstracto |
| **Concrete Factory** | Implementa los métodos de creación para una familia específica |
| **Abstract Product** | Interfaz para un tipo de producto |
| **Concrete Product** | Implementación específica de un producto para una familia |
| **Client** | Usa las interfaces abstractas, sin conocer las clases concretas |

---

## ¿Cuándo usar Abstract Factory?

### ✅ Usa Abstract Factory cuando:

1. **Tu código necesita trabajar con varias familias de productos relacionados**
   - Ejemplo: UI para diferentes SO, temas de aplicación, conexiones a diferentes BD

2. **Quieres asegurar que los productos de una familia sean compatibles entre sí**
   - Ejemplo: No mezclar botones de Windows con menús de macOS

3. **Quieres ocultar las implementaciones concretas del código cliente**
   - El cliente solo conoce interfaces abstractas

4. **Anticipas agregar nuevas familias de productos en el futuro**
   - Agregar "LinuxFactory" sin modificar código existente

5. **Quieres proporcionar una biblioteca de productos sin exponer su implementación**

### ❌ No uses Abstract Factory cuando:

1. Solo tienes un tipo de producto (usa Factory Method en su lugar)
2. Las familias de productos no tienen relación entre sí
3. El sistema es simple y no se espera que crezca
4. Solo necesitas crear objetos una vez (considera Singleton o Prototype)

---

## Ejemplos de código

Este repositorio incluye tres implementaciones que demuestran diferentes enfoques:

### 📁 Estructura del proyecto

```
Abstract Factory/
├── README.md                          # Este archivo
├── patron_aplicado/
│   ├── README.md                      # Explicación del patrón aplicado
│   └── abstract_factory.py            # ✅ Implementación correcta
├── antipatron/
│   ├── README.md                      # Explicación del antipatrón
│   └── antipatron.py                  # ❌ Mala implementación
└── sin_patron/
    ├── README.md                      # Explicación sin patrón
    └── sin_patron.py                  # ⚠️ Código sin el patrón
```

### 1. ✅ Patrón aplicado correctamente

📂 **Ubicación**: [`patron_aplicado/abstract_factory.py`](patron_aplicado/abstract_factory.py)

Implementación completa del patrón usando un sistema de UI multiplataforma:

- **Productos abstractos**: `Button`, `Checkbox`, `TextInput`
- **Productos concretos**: `WindowsButton`, `MacOSButton`, etc.
- **Fábrica abstracta**: `GUIFactory`
- **Fábricas concretas**: `WindowsFactory`, `MacOSFactory`

> 📊 **RECOMENDACIÓN DE DIAGRAMA**: Diagrama de secuencia mostrando cómo el cliente interactúa con la fábrica.

### 2. ❌ Antipatrón (mala implementación)

📂 **Ubicación**: [`antipatron/antipatron.py`](antipatron/antipatron.py)

Ejemplos de qué **NO** hacer:

- Fábrica con condicionales en lugar de polimorfismo
- Productos sin interfaz común
- Cliente acoplado a implementaciones concretas
- Fábrica "God Class" con demasiadas responsabilidades

### 3. ⚠️ Código sin el patrón

📂 **Ubicación**: [`sin_patron/sin_patron.py`](sin_patron/sin_patron.py)

Muestra cómo se vería el código sin usar el patrón:

- Clases de aplicación duplicadas por cada SO
- Creación directa de objetos concretos
- Enfoque procedural con funciones

---

## Diagrama de flujo

> 📊 **RECOMENDACIÓN DE DIAGRAMA**: Diagrama de flujo mostrando el proceso de creación de objetos.

```
┌─────────────────┐
│     Cliente     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│ ¿Qué familia    │────▶│ Obtener fábrica │
│ de productos?   │     │ correspondiente │
└─────────────────┘     └────────┬────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ WindowsFactory  │     │  MacOSFactory   │     │  LinuxFactory   │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Crea productos  │     │ Crea productos  │     │ Crea productos  │
│ Windows         │     │ macOS           │     │ Linux           │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## Ventajas y Desventajas

### ✅ Ventajas

| Ventaja | Descripción |
|---------|-------------|
| **Consistencia** | Garantiza que los productos de una familia sean compatibles |
| **Aislamiento** | El código cliente no conoce las clases concretas |
| **Intercambiabilidad** | Fácil cambiar familias de productos en tiempo de ejecución |
| **Principio OCP** | Agregar nuevas familias sin modificar código existente |
| **Testabilidad** | Fácil usar mocks y fábricas de prueba |

### ❌ Desventajas

| Desventaja | Descripción |
|------------|-------------|
| **Complejidad** | Introduce muchas interfaces y clases nuevas |
| **Rigidez de productos** | Agregar nuevos tipos de productos requiere modificar todas las fábricas |
| **Sobrecarga** | Puede ser excesivo para sistemas simples |

---

## Relación con otros patrones

> 📊 **RECOMENDACIÓN DE DIAGRAMA**: Diagrama comparativo entre patrones creacionales.

| Patrón | Relación con Abstract Factory |
|--------|-------------------------------|
| **Factory Method** | Abstract Factory usa Factory Method internamente. Factory Method crea un producto, Abstract Factory crea familias |
| **Singleton** | Las fábricas concretas suelen implementarse como Singleton |
| **Prototype** | Alternativa cuando las familias de productos son muy variadas |
| **Builder** | Builder crea objetos paso a paso; Abstract Factory crea objetos de una vez |

### Cuándo usar cada uno:

```
┌────────────────────┬─────────────────────────────────────────┐
│ Patrón             │ Usar cuando...                          │
├────────────────────┼─────────────────────────────────────────┤
│ Factory Method     │ Un solo tipo de producto                │
│ Abstract Factory   │ Familias de productos relacionados      │
│ Builder            │ Objetos complejos con muchos pasos      │
│ Prototype          │ Clonación es más eficiente que creación │
│ Singleton          │ Solo una instancia debe existir         │
└────────────────────┴─────────────────────────────────────────┘
```

---

## Recomendaciones para diagramas

Para complementar esta documentación, se recomienda incluir los siguientes diagramas:

### 1. 📊 Diagrama de clases UML
**Ubicación sugerida**: Sección "Estructura del patrón"
- Muestra las interfaces y clases del patrón
- Relaciones entre Abstract Factory, Concrete Factories y Products

### 2. 📊 Diagrama de secuencia
**Ubicación sugerida**: Sección "Patrón aplicado correctamente"
- Flujo de creación de objetos
- Interacción Cliente → Factory → Products

### 3. 📊 Diagrama comparativo
**Ubicación sugerida**: Sección "Relación con otros patrones"
- Tabla visual comparando Abstract Factory vs Factory Method vs Builder

### 4. 📊 Diagrama de componentes
**Ubicación sugerida**: Antes de "Ejemplos de código"
- Muestra la estructura del proyecto y cómo se relacionan los módulos

### Herramientas recomendadas para crear diagramas:
- [draw.io](https://app.diagrams.net/) - Gratuito y fácil de usar
- [PlantUML](https://plantuml.com/) - Diagramas como código
- [Mermaid](https://mermaid.js.org/) - Integración con Markdown
- [Lucidchart](https://www.lucidchart.com/) - Profesional

---

## Referencias

- **Gang of Four** - "Design Patterns: Elements of Reusable Object-Oriented Software"
- **Refactoring Guru** - [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)
- **Python Design Patterns** - Brandon Rhodes

---

## Ejecución de ejemplos

Cada carpeta contiene su propio README con instrucciones específicas. Para ejecutar cualquier ejemplo:

```bash
# Navegar a la carpeta del ejemplo
cd "Abstract Factory/patron_aplicado"

# Ejecutar el script
python abstract_factory.py
```

---

**Autor**: Documentación creada como material educativo sobre patrones de diseño.

**Licencia**: MIT
