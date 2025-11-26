# Patrón Creacional: Singleton

## 📖 Descripción

El patrón **Singleton** es un patrón de diseño creacional que asegura que una clase tenga solo una instancia y proporciona un punto de acceso global a esa instancia.

### ¿Por qué es importante?

En aplicaciones reales, algunos recursos **deben ser únicos**:
- 🖨️ **Impresora**: Una sola impresora física compartida
- 🗄️ **Base de datos**: Una única conexión activa
- 📝 **Logger**: Un punto centralizado de registro
- ⚙️ **Configuración**: Una sola configuración global
- 🔐 **Sesión**: Un usuario autenticado actualmente

---

## 📂 Estructura del Proyecto

```
singleton/
├── patron/
│   ├── ejemplo_gestor_impresion.py      # ✅ Ejemplo CON Singleton
│   └── singleton_decorator.py           # ✅ Implementación del patrón
│
├── antipatron/
│   └── ejemplo_gestor_impresion_sin_singleton.py  # ❌ Ejemplo SIN Singleton
│
├── doc/
│   ├── README_COMPARACION.md            # 📊 Análisis detallado sin vs con
│   ├── README_GESTOR_IMPRESION.md       # 🔧 Detalles técnicos del ejemplo
│   ├── MAPAS_MENTALES_SINGLETON.md      # 🧠 Visualización ASCII
│   ├── diagrama_secuencia_singleton.md  # 📋 Secuencia UML
│   ├── diagrama_secuencia_singleton.png # 🖼️ Imagen del diagrama
│   └── Ejemplo_practico.png             # 🖼️ Imagen del ejemplo
│
└── README.md                            # Este archivo
```

---

## 🚀 Inicio Rápido

### Ejecutar TODO (recomendado)
```bash
cd singleton
python main.py
```
Esto ejecuta:
1. ❌ Contraejemplo sin Singleton (demuestra problemas)
2. ✅ Solución con Singleton (demuestra ventajas)
3. 📊 Comparación y conclusiones

### Ejecutar por separado

**Ver el problema (sin Singleton):**
```bash
python antipatron/ejemplo_gestor_impresion_sin_singleton.py
```

**Ver la solución (con Singleton):**
```bash
python patron/ejemplo_gestor_impresion.py
```

---

## 🔍 Ejemplo Práctico: Gestor de Impresión

### El Caso de Uso

Una oficina con:
- **3 empleados** (Juan, María, Pedro) que necesitan imprimir
- **1 impresora física** compartida en la red
- **1 cola de impresión** (¿con o sin Singleton?)

### ❌ SIN Singleton (El Problema)

Cada empleado crea su propia cola:
```python
cola_juan = GestorImpresion()    # 🚨 Cola #1
cola_maria = GestorImpresion()   # 🚨 Cola #2
cola_pedro = GestorImpresion()   # 🚨 Cola #3
```

**Conflictos que ocurren:**
1. **Múltiples colas** - ¿Cuál es la "verdadera" cola?
2. **Referencias independientes** - `cola_juan is not cola_maria`
3. **Estado inconsistente** - Cada uno ve diferente cantidad de trabajos
4. **Race conditions** - Comandos conflictivos a la impresora

**Resultado:** 💥 CAOS

---

### ✅ CON Singleton (La Solución)

```python
@singleton
class GestorImpresion:
    def enviar_trabajo(self, empleado, documento, paginas):
        self.cola_trabajos.append(...)
```

Todos usan LA MISMA instancia:
```python
gestor_juan = GestorImpresion()    # Instancia #1
gestor_maria = GestorImpresion()   # Instancia #1 (misma!)
gestor_pedro = GestorImpresion()   # Instancia #1 (misma!)

gestor_juan is gestor_maria  # True ✅
```

**Ventajas:**
- ✅ Una sola cola coordinada
- ✅ Acceso global garantizado
- ✅ Estado consistente
- ✅ Thread-safe
- ✅ Procesamiento FIFO

**Resultado:** ✨ ORDEN Y SEGURIDAD

---

## 📚 Implementación del Patrón

### Decorador Singleton

```python
from functools import wraps
from threading import Lock

def singleton(cls):
    """Decorador que convierte una clase en Singleton"""
    instances = {}
    lock = Lock()
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:  # ← Thread-safe
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance
```

**Características:**
- ✅ **Simple**: Fácil de entender
- ✅ **Pythónico**: Usa decoradores
- ✅ **Thread-safe**: Usa locks
- ✅ **Reutilizable**: Aplica a cualquier clase

### Uso en el Proyecto

```python
# patron/singleton_decorator.py
@singleton
class GestorImpresion:
    def __init__(self):
        self.cola_trabajos = []
    
    def enviar_trabajo(self, empleado, documento, paginas):
        # Agregar a la única cola
        self.cola_trabajos.append({...})
```

---

## 📊 Comparación Visual

| Aspecto | SIN Singleton ❌ | CON Singleton ✅ |
|---------|-----------------|-----------------|
| **Instancias** | Múltiples (3+) | Una única |
| **Colas** | Independientes | Centralizada |
| **Identidad** | `obj1 is not obj2` | `obj1 is obj2` |
| **Estado** | Inconsistente | Consistente |
| **Thread Safety** | Problemático | Garantizado |
| **Orden FIFO** | Imposible | Garantizado |
| **Auditoría** | Imposible | Completa |

---

## 📖 Documentación Detallada

Para profundizar, consulta estos archivos:

### `doc/README_COMPARACION.md`
- Análisis lado a lado sin vs con Singleton
- Ejemplos de código
- Tabla comparativa

### `doc/MAPAS_MENTALES_SINGLETON.md`
- Visualización ASCII de los conflictos
- Mapa mental del problema
- Mapa mental de la solución
- Analogías del mundo real

### `doc/diagrama_secuencia_singleton.md`
- Secuencia UML del patrón
- Flujo de getInstance()
- Mecanismo de sincronización
- Thread-safety explicado

---

## 🎯 Cuándo Usar Singleton

### ✅ Usar Singleton cuando:
- Existe un recurso **único** (impresora, BD, logger)
- Necesitas un **punto de acceso global**
- El recurso es **costoso** de crear
- Necesitas **coordinación centralizada**

### ❌ NO usar Singleton cuando:
- Necesitas **múltiples instancias** independientes
- Quieres facilitar **tests unitarios**
- La clase es **stateless** (sin estado)
- Prefieres **inyección de dependencias**

---

## ⚡ Puntos Clave

1. **Recurso Único** → Necesita Singleton
   ```
   UNA impresora física
           ↓
   UN punto de control (Singleton)
   ```

2. **Instancia Única**
   ```python
   g1 = GestorImpresion()
   g2 = GestorImpresion()
   g1 is g2  # True
   ```

3. **Thread-Safe**
   ```python
   # El decorador usa Lock automáticamente
   with lock:  # ← Protección incluida
       if not existe:
           crear_instancia()
   ```

4. **Acceso Global**
   ```python
   # Desde cualquier módulo
   GestorImpresion().enviar_trabajo(...)  # Siempre la misma
   ```

---

## 🔗 Referencias

- [Refactoring Guru - Singleton](https://refactoring.guru/es/design-patterns/singleton)
- [Python Design Patterns](https://python-patterns.guide/python/singleton/)
- [Design Patterns in Python](https://www.patterns.dev/posts/singleton-pattern/)

---

## 📝 Nota Importante

Este proyecto es **EDUCATIVO** y demuestra:
- Por qué el Singleton es necesario en ciertos casos
- Cómo implementarlo de forma correcta
- Los problemas que resuelve
- Las ventajas sobre el enfoque sin Singleton

**Objetivo:** Aprender cuándo y cómo usar el patrón Singleton en Python.
