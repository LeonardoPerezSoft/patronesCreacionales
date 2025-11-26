# Patrón Creacional: Singleton

## Descripción

El patrón **Singleton** es un patrón de diseño creacional que asegura que una clase tenga solo una instancia y proporciona un punto de acceso global a esa instancia.

## Problema que resuelve

En algunas aplicaciones, necesitamos que ciertos objetos existan en una única instancia:
- **Conexiones a BD**: Solo una conexión activa
- **Logger**: Un único punto de registro de eventos
- **Caché**: Compartir datos entre toda la aplicación
- **Configuración**: Una sola configuración para toda la app
- **Sesión de usuario**: Solo un usuario autenticado actualmente

## Estructura del Proyecto

```
singleton/
├── src/
│   ├── __init__.py
│   ├── singleton_metaclass.py      # Implementación con Metaclase
│   ├── singleton_decorator.py      # Implementación con Decorador
│   └── singleton_class_method.py   # Implementación con Método de Clase
├── examples/
│   ├── ejemplo_metaclase.py        # Ejemplos de uso con metaclase
│   ├── ejemplo_decorador.py        # Ejemplos de uso con decorador
│   ├── ejemplo_class_method.py     # Ejemplos de uso con método de clase
│   └── ejemplo_comparativo.py      # Comparación de enfoques
├── tests/
│   └── test_singleton.py           # Tests unitarios
└── README.md                       # Este archivo
```

## Implementaciones

### 1. Metaclase (Recomendado para control máximo)

```python
class SingletonMeta(type):
    _instances = {}
    _lock = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock[cls]:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]
```

**Ventajas:**
- Control total sobre la creación de instancias
- Thread-safe
- Explícito

**Desventajas:**
- Más complejo
- Requiere comprender metaclases

**Uso:**
```python
class DatabaseConnection(metaclass=SingletonMeta):
    pass

db1 = DatabaseConnection()
db2 = DatabaseConnection()
assert db1 is db2  # ✓ Misma instancia
```

---

### 2. Decorador (Recomendado para nuevas aplicaciones)

```python
def singleton(cls):
    instances = {}
    lock = Lock()
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance
```

**Ventajas:**
- Simple y pythónico
- Fácil de entender
- Thread-safe
- Reutilizable

**Desventajas:**
- Requiere `()` al instanciar
- Modifica la clase

**Uso:**
```python
@singleton
class Logger:
    pass

logger1 = Logger()
logger2 = Logger()
assert logger1 is logger2  # ✓ Misma instancia
```

---

### 3. Método de Clase (Recomendado para herencia)

```python
class SingletonClassMethod:
    _instance = None
    _lock = Lock()
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

**Ventajas:**
- Enfoque clásico
- Permite herencia
- Thread-safe
- Control explícito

**Desventajas:**
- Requiere heredar
- Control de reinicialización manual

**Uso:**
```python
class SessionManager(SingletonClassMethod):
    pass

session1 = SessionManager()
session2 = SessionManager()
assert session1 is session2  # ✓ Misma instancia
```

---

## Ejemplos Incluidos

### Metaclase
- **DatabaseConnection**: Conexión única a base de datos
- **ConfigurationManager**: Gestor de configuración global

### Decorador
- **Logger**: Logger único para toda la aplicación
- **CacheManager**: Gestor de caché centralizado

### Método de Clase
- **SessionManager**: Gesión de sesión de usuario
- **EmailService**: Servicio de envío de correos

## Ejecutar los Ejemplos

```bash
# Ejecutar ejemplo de metaclase
python examples/ejemplo_metaclase.py

# Ejecutar ejemplo de decorador
python examples/ejemplo_decorador.py

# Ejecutar ejemplo de método de clase
python examples/ejemplo_class_method.py

# Ver comparación de enfoques
python examples/ejemplo_comparativo.py
```

## Ejecutar los Tests

```bash
# Ejecutar todos los tests
python -m pytest tests/test_singleton.py -v

# O usando unittest directamente
python -m unittest tests.test_singleton -v
```

## Cuándo Usar Singleton

✓ **Usar Singleton cuando:**
- Necesitas una única instancia (BD, Logger, Config)
- Quieres un punto de acceso global
- Los recursos son limitados

✗ **NO usar Singleton cuando:**
- Necesitas múltiples instancias independientes
- Quieres facilitar tests unitarios
- La clase es stateless (sin estado)

## Consideraciones Importantes

### Thread-Safety
Todas las implementaciones incluyen locks para ser thread-safe:
```python
# Las tres implementaciones son seguras en ambientes multi-hilo
```

### Testing
Para testing, considera usar inyección de dependencias en lugar de Singleton:
```python
# Mejor que Singleton para testing
def procesar_datos(logger: Logger, db: Database):
    logger.info("Procesando...")
    db.conectar()
```

### Alternativas Modernas
- **Inyección de Dependencias**: Más testeable
- **Módulos Python**: Para datos globales
- **Context Managers**: Para manejo de recursos

## Comparación de Enfoques

| Característica | Metaclase | Decorador | Método de Clase |
|---|---|---|---|
| Complejidad | Alta | Baja | Media |
| Pythónico | No | Sí | Medio |
| Thread-safe | Sí | Sí | Sí |
| Herencia | Limitada | No | Sí |
| Reutilizable | No | Sí | No |
| Curva aprendizaje | Empinada | Plana | Media |

## Recomendaciones

1. **Para aplicaciones nuevas**: Usa **DECORADOR** (más simple)
2. **Para control absoluto**: Usa **METACLASE** (máximo poder)
3. **Para herencia**: Usa **MÉTODO DE CLASE** (permite subclases)
4. **En duda**: Usa **DECORADOR** (más pythónico)

## Recursos Adicionales

- [Refactoring Guru - Singleton](https://refactoring.guru/es/design-patterns/singleton)
- [Python Design Patterns](https://python-patterns.guide/python/singleton/)
- [Design Patterns in Python](https://www.patterns.dev/posts/singleton-pattern/)

## Autor

Patrón Singleton - Ejemplos educativos para aprender diseño de software
