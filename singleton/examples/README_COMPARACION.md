# 🖨️ Ejemplo Completo: Gestor de Impresión

## 📖 Introducción

Este ejemplo demuestra **POR QUÉ** el patrón Singleton es **NECESARIO** (no opcional) para un Gestor de Impresión mediante una comparación directa:

1. **SIN Singleton** → Muestra los **4 conflictos principales**
2. **CON Singleton** → Demuestra la **solución elegante**

---

## 🎯 Objetivo Pedagógico

**Pregunta**: ¿Es el Singleton esencial para una cola de impresión?

**Respuesta**: **SÍ, porque existe UNA sola impresora física.**

Una sola impresora **SOLO puede procesar UN trabajo a la vez**, por lo que su acceso **DEBE coordinarse por un punto único**. El Singleton es la garantía de esa coordinación central.

---

## 📂 Archivos Incluidos

| Archivo | Propósito |
|---------|-----------|
| `ejemplo_gestor_impresion_sin_singleton.py` | Demuestra los CONFLICTOS sin Singleton |
| `ejemplo_gestor_impresion.py` | Demuestra la SOLUCIÓN con Singleton |
| `MAPAS_MENTALES_SINGLETON.md` | Visualización de ambos enfoques |

---

## ⚠️ PARTE 1: SIN SINGLETON (El Problema)

### Archivo: `ejemplo_gestor_impresion_sin_singleton.py`

Este archivo demuestra **4 conflictos principales** que ocurren sin Singleton:

#### Conflicto #1: Múltiples Colas Independientes
```
GestorA → Cola_A: [Trabajo1, Trabajo2]
GestorB → Cola_B: [Trabajo3]
GestorC → Cola_C: [Trabajo4, Trabajo5]

❌ PROBLEMA: ¿Cuál es la "verdadera" cola de impresión?
   La impresora NO SABE de dónde sacar trabajos.
```

#### Conflicto #2: Referencias Independientes
```python
gestor_a = GestorImpresion()
gestor_b = GestorImpresion()

gestor_a is gestor_b  # → False ❌

❌ PROBLEMA: Dos "gestores" pero son objetos DIFERENTES.
   Los cambios en A no se ven en B.
```

#### Conflicto #3: Estado Inconsistente
```python
gestor_a.trabajos = [Trabajo1, Trabajo2]  # 2 trabajos según A
gestor_b.trabajos = [Trabajo3]            # 1 trabajo según B
gestor_c.trabajos = []                    # 0 trabajos según C

❌ PROBLEMA: ¿Cuántos trabajos hay REALMENTE en la impresora?
   Cada parte del sistema ve una realidad DIFERENTE.
```

#### Conflicto #4: Race Conditions
```python
Thread-1: gestor_a.enviar_trabajo("Doc1")
Thread-2: gestor_b.enviar_trabajo("Doc2")
Thread-3: gestor_c.procesar_cola()

❌ PROBLEMA: Múltiples threads acceden a recursos SIN coordinación.
   Pueden enviar comandos conflictivos a la impresora → CRASH.
```

### Ejecutar el Contraejemplo

```bash
python ejemplo_gestor_impresion_sin_singleton.py
```

**Salida**: Demuestra interactivamente cada uno de los 4 conflictos.

---

## ✅ PARTE 2: CON SINGLETON (La Solución)

### Archivo: `ejemplo_gestor_impresion.py`

Este archivo implementa **GestorImpresion como Singleton** y demuestra cómo se resuelven todos los problemas.

### Características

```python
@singleton  # ← El decorador garantiza instancia única
class GestorImpresion:
    def enviar_trabajo(self, empleado: str, documento: str, paginas: int):
        # Una única cola compartida
        self.cola_trabajos.append(trabajo)
    
    def procesar_cola(self):
        # Procesa en orden FIFO (First In, First Out)
        while self.cola_trabajos:
            trabajo = self.cola_trabajos.popleft()
            self._imprimir(trabajo)
    
    def obtener_reporte(self):
        # Auditoría centralizada
        return self.reporte_trabajos
```

### Soluciones Demostradas

#### Solución #1: Instancia Única
```python
gestor_1 = GestorImpresion()
gestor_2 = GestorImpresion()
gestor_3 = GestorImpresion()

gestor_1 is gestor_2  # → True ✓
gestor_2 is gestor_3  # → True ✓

✓ SOLUCION: Todos obtienen el MISMO objeto.
  Punto de acceso global garantizado.
```

#### Solución #2: Cola Centralizada
```python
# Todos envían a LA MISMA cola
GestorImpresion().enviar_trabajo("Juan", "Reporte", 5)
GestorImpresion().enviar_trabajo("María", "Presentación", 3)
GestorImpresion().enviar_trabajo("Pedro", "Contrato", 8)

Cola única: [Reporte(5), Presentación(3), Contrato(8)]

✓ SOLUCION: Una única fuente de verdad.
  Todos los trabajos en un solo lugar.
```

#### Solución #3: Estado Consistente
```python
# Cualquier módulo puede obtener el estado consistente
auditor_1 = GestorImpresion()
auditor_2 = GestorImpresion()

auditor_1.obtener_reporte()  # Ve TODOS los trabajos
auditor_2.obtener_reporte()  # Ve EXACTAMENTE lo mismo

✓ SOLUCION: Estado único y consistente.
  Auditoría centralizada y confiable.
```

#### Solución #4: Thread Safety
```python
# El Singleton usa locks para coordinación
with self._lock:  # ← Protección automática
    self.cola_trabajos.append(trabajo)
    self.trabajos_totales += 1

✓ SOLUCION: Sincronización centralizada.
  Sin condiciones de carrera.
  Sin conflictos entre threads.
```

### Ejecutar la Solución

```bash
python ejemplo_gestor_impresion.py
```

**Salida**: Simulación completa de oficina con empleados, documentos, y procesamiento ordenado.

---

## 🗺️ MAPAS MENTALES

Para visualizar las diferencias entre ambos enfoques, consulta:

### 📄 `MAPAS_MENTALES_SINGLETON.md`

Contiene:
- ✅ Mapa Mental #1: SIN Singleton (Caos)
- ✅ Mapa Mental #2: CON Singleton (Orden)
- ✅ Análisis detallado de los 4 conflictos
- ✅ Comparación lado a lado
- ✅ Analogías con mundo real

**Ver**: `MAPAS_MENTALES_SINGLETON.md`

---

## 📊 COMPARACIÓN RÁPIDA

| Aspecto | SIN Singleton ❌ | CON Singleton ✓ |
|---------|-----------------|-----------------|
| **Instancias** | Múltiples | Una única |
| **Colas** | Independientes | Centralizada |
| **Referencias** | `obj1 is not obj2` | `obj1 is obj2` |
| **Estado** | Inconsistente | Consistente |
| **Thread Safety** | Problemático | Garantizado |
| **Orden FIFO** | Imposible | Garantizado |
| **Auditoría** | Imposible | Completa |
| **Escalabilidad** | Falla con threads | Sólida |

---

## 🎓 Flujo de Aprendizaje Recomendado

### Paso 1: Entender el Problema
1. Lee este archivo (README)
2. Ejecuta `python ejemplo_gestor_impresion_sin_singleton.py`
3. Observa cómo falla sin Singleton

### Paso 2: Ver los Mapas
1. Abre `MAPAS_MENTALES_SINGLETON.md`
2. Estudia Mapa #1 (SIN Singleton)
3. Observa los 4 conflictos visualmente

### Paso 3: Conocer la Solución
1. Ejecuta `python ejemplo_gestor_impresion.py`
2. Observa cómo funciona perfectamente
3. Compara con el contraejemplo

### Paso 4: Análisis Comparativo
1. Abre `MAPAS_MENTALES_SINGLETON.md`
2. Estudia Mapa #2 (CON Singleton)
3. Lee la sección "Comparación Visual"

### Paso 5: Conclusión
1. Lee "CONCLUSIONES" en los mapas mentales
2. Entiende POR QUÉ Singleton es necesario
3. Aplica el concepto a otros contextos

---

## 🔗 Conceptos Clave

### 1. Recurso Único
```
Existe UNA impresora física
      ↓
Solo puede procesar UN trabajo a la vez
      ↓
Necesita UN punto de control → SINGLETON
```

### 2. Punto de Acceso Global
```python
from src.singleton_decorator import singleton

@singleton
class GestorImpresion:
    ...

# Desde cualquier parte del código:
GestorImpresion().enviar_trabajo(...)  # ✓ Siempre la misma instancia
```

### 3. Thread Safety
```python
# El Singleton usa locks automáticamente
class SingletonDecorado:
    _lock = Lock()
    
    def __init__(self):
        with self._lock:  # ← Protegido
            self.cola = deque()
```

### 4. Auditoría Centralizada
```python
# Un único lugar para ver TODOS los trabajos
reporte = GestorImpresion().obtener_reporte()
# Contiene histórico completo, consistente y verificable
```

---

## 💡 Aplicaciones Prácticas

El concepto se aplica a muchos contextos:

| Caso | Recurso Único | Solución |
|------|---------------|----------|
| 🖨️ Impresora | Hardware físico | Singleton gestor |
| 🗄️ Base de Datos | Conexión única | Singleton connection pool |
| ⚙️ Configuración | Valores globales | Singleton config |
| 📝 Logger | Salida única | Singleton logger |
| 🔐 Sesiones | Usuario actual | Singleton session |
| 💾 Caché | Datos compartidos | Singleton cache |

---

## ⚡ Ejecución Completa (main.py)

El archivo `main.py` en la raíz ejecuta AMBOS ejemplos en secuencia:

```bash
cd singleton
python main.py
```

Esto:
1. Ejecuta el contraejemplo (SIN Singleton) → Muestra conflictos
2. Pausa para que leas el resultado
3. Ejecuta la solución (CON Singleton) → Muestra orden
4. Pausa para comparación
5. Muestra conclusiones

---

## 📚 Archivos de Implementación

Para entender la implementación del Singleton:

- `src/singleton_decorator.py` - El decorador `@singleton`
- `src/singleton_metaclass.py` - Implementación con metaclase
- `src/singleton_class_method.py` - Implementación con `__new__`
- `tests/test_singleton.py` - Tests unitarios (13 pruebas)

---

## 🎯 Conclusión

### La Pregunta
> ¿Es Singleton necesario para un Gestor de Impresión?

### La Respuesta
> **SÍ, es absolutamente necesario porque:**
> 
> 1. Existe una **única impresora física**
> 2. Solo puede procesar **un trabajo a la vez**
> 3. Los trabajos **deben procesarse en orden**
> 4. Se necesita **un punto de control central**
> 5. Sin Singleton → **conflictos garantizados**
> 6. Con Singleton → **orden y seguridad**

### La Lección
El Singleton no es sobre "conveniencia" o "simplificar código".

Es sobre **garantizar la seguridad y consistencia** cuando un recurso crítico (como una impresora) tiene un acceso que debe ser coordinado centralmente.

---

**Para análisis visual detallado:** Ver `MAPAS_MENTALES_SINGLETON.md`
