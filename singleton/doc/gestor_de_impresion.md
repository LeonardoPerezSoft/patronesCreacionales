# Nuevo Ejemplo: Gestor de Impresión con Singleton

## Descripción

El archivo `ejemplo_gestor_impresion.py` presenta un caso práctico muy realista del patrón Singleton en una oficina moderna.

## Escenario

Imagina una oficina con:
- ✅ **3 empleados** (Juan, María, Pedro) que necesitan imprimir documentos
- ✅ **1 impresora física** compartida en la red
- ✅ **1 cola de impresión centralizada** (Singleton)

## El Problema sin Singleton

Si cada empleado creara su propia cola de impresión:
```python
cola_juan = ColasDeImpresion()    # ❌ Su propia cola
cola_maria = ColasDeImpresion()   # ❌ Su propia cola
cola_pedro = ColasDeImpresion()   # ❌ Su propia cola
```

**Problemas que ocurrirían:**
- 📄 Trabajos se pierden o se duplican
- 🔀 No hay orden de procesamiento
- ⚡ La impresora recibe comandos conflictivos
- 📋 Imposible seguimiento centralizado

## La Solución: Singleton

```python
@singleton
class GestorImpresion:
    def enviar_trabajo(self, empleado, documento, paginas):
        # Una única cola para toda la oficina
        self.cola_trabajos.append(...)
```

**Ventajas:**
- ✅ Una sola cola de impresión
- ✅ Todos los empleados usan la MISMA instancia
- ✅ Trabajos procesados en orden FIFO
- ✅ Seguimiento completo de todos los trabajos

## Características del Ejemplo

### 1. Clase GestorImpresion (Singleton con Decorador)

```python
@singleton
class GestorImpresion:
    def enviar_trabajo(self, empleado: str, documento: str, paginas: int) -> int
    def procesar_cola(self) -> bool
    def obtener_estado_cola(self) -> dict
    def obtener_reporte(self) -> str
```

### 2. Métodos Principales

| Método | Descripción |
|--------|-------------|
| `enviar_trabajo()` | Añade un trabajo a la cola |
| `procesar_cola()` | Procesa el siguiente trabajo (simula tiempo de impresión) |
| `obtener_estado_cola()` | Retorna el estado actual |
| `obtener_reporte()` | Genera un reporte de todos los trabajos |

### 3. Simulaciones Incluidas

El ejemplo contiene varias demostraciones:

1. **Escenario SIN Singleton** - Muestra los problemas
2. **Simulación Completa** - 5 empleados, 5 trabajos, procesamiento ordenado
3. **Verificación de Punto de Acceso Global** - Demuestra que `gestor1 is gestor2 is gestor3`
4. **Ventajas del Singleton** - Explicación detallada

## Ejecutar el Ejemplo

```bash
cd singleton
python examples/ejemplo_gestor_impresion.py
```

### Salida Esperada

```
======================================================================
              EJEMPLO: GESTOR DE IMPRESION CON SINGLETON
          Una oficina, una impresora, una cola, un Singleton
======================================================================

[...contenido simulado de la oficina...]

PRUEBA: PUNTO DE ACCESO GLOBAL
======================================================================

¿gestor1 es gestor2?: True
¿gestor2 es gestor3?: True
¿gestor1 es gestor3?: True

ID de gestor1: 2305171006160
ID de gestor2: 2305171006160
ID de gestor3: 2305171006160

✅ CONFIRMADO: Todos los empleados acceden a la MISMA instancia
```

## Conceptos Clave Demostrados

### 1. Instancia Única
```python
gestor1 = GestorImpresion()
gestor2 = GestorImpresion()
assert gestor1 is gestor2  # ✓ MISMO objeto
```

### 2. Cola Ordenada (FIFO)
Los trabajos se procesan en el orden en que fueron enviados:
1. Juan envía "Reporte" (5 pág) → Posición 1
2. María envía "Presentación" (3 pág) → Posición 2
3. Pedro envía "Contrato" (8 pág) → Posición 3

La impresora procesa: Reporte → Presentación → Contrato

### 3. Punto de Acceso Global
Cualquier parte del programa accede al MISMO gestor:
```python
# En módulo de autenticación
logger = GestorImpresion()
logger.enviar_trabajo(...)

# En módulo de base de datos
gestor = GestorImpresion()  # ← MISMO que arriba
gestor.procesar_cola()

# En módulo de notificaciones
gestor = GestorImpresion()  # ← SIGUE SIENDO el mismo
```

### 4. Seguimiento Centralizado
Todos los trabajos están en un único lugar:
```python
reporte = gestor.obtener_reporte()
# Contiene:
# - Trabajos completados (5)
# - Trabajos en cola (0)
# - Histórico completo
```

## Ventajas Demostradas

| Ventaja | Descripción |
|---------|-------------|
| **Instancia Única** | Solo 1 gestión de impresión en la oficina |
| **Cola Ordenada** | Los trabajos se procesan en orden FIFO |
| **Punto Global** | Acceso desde cualquier módulo |
| **Seguimiento** | Historial completo de todos los trabajos |
| **Sincronización** | No hay conflictos ni sobrescrituras |
| **Escalabilidad** | Funciona con 3 o 100 empleados |

## Caso Real: Impresoras en Red

En una oficina real:
- 50 empleados compartiendo 3 impresoras
- 1 Gestor de Impresión Singleton **por cada impresora**
- El sistema operativo garantiza una instancia por impresora
- Todos los trabajos se procesan sin conflictos

## Cómo Adaptar Este Patrón a Tus Proyectos

### 1. Conexión a Base de Datos
```python
@singleton
class DatabaseConnection:
    def connect(self): ...
    def execute_query(self): ...
```

### 2. Configuración Global
```python
@singleton
class Config:
    def set(self, key, value): ...
    def get(self, key): ...
```

### 3. Logger Centralizado
```python
@singleton
class Logger:
    def info(self, msg): ...
    def error(self, msg): ...
```

### 4. Servicio de Email
```python
@singleton
class EmailService:
    def send_email(self, to, subject, body): ...
```

## Comparación con Otras Soluciones

### SIN Singleton (Pasar parámetros)
```python
def procesar_datos(gestor: GestorImpresion):
    gestor.enviar_trabajo(...)

# ❌ Necesitas pasar el parámetro en cada función
```

### CON Singleton
```python
def procesar_datos():
    GestorImpresion().enviar_trabajo(...)

# ✅ Acceso directo, sin parámetros
```

## Notas Importantes

1. **Thread-Safe**: El decorador `@singleton` usa locks para ser seguro en ambientes multi-hilo
2. **Único por Clase**: Cada clase decorada con `@singleton` tiene su propia instancia única
3. **Inyección de Dependencias**: Para testing, considera inyectar en lugar de usar Singleton
4. **No Abuses**: No hagas Singleton a TODO, úsalo donde realmente sea necesario

## Archivos Relacionados

- `src/singleton_decorator.py` - Implementación del decorador
- `ejemplo_real.py` - Otro caso práctico (Logger centralizado)
- `tests/test_singleton.py` - Tests unitarios

## Conclusión

El Gestor de Impresión es un ejemplo **perfecto del mundo real** que demuestra:
- ✅ La necesidad real del Singleton
- ✅ Cómo evita problemas de conflictos
- ✅ Cómo proporciona un único punto de control
- ✅ Cómo simplifica el código de la aplicación

Este patrón es especialmente útil en:
- 🖨️ Sistemas de impresión
- 🗄️ Conexiones a base de datos
- ⚙️ Configuración global
- 📝 Logging
- 🔐 Gestión de sesiones
- 💾 Cachés
