Patrón Creacional: Builder
Descripción

El patrón Builder es un patrón de diseño creacional que permite construir objetos complejos paso a paso, usando un proceso claro, legible y flexible.
Evita constructores gigantes y difíciles de leer, y permite crear objetos con muchas variaciones sin caer en código caótico.

❗ Problema que resuelve

Cuando un objeto tiene muchos atributos opcionales, los constructores tradicionales empiezan a volverse:

Muy largos

Difíciles de leer

Fácilmente confundibles

Frágiles cuando cambian los requisitos

Ejemplos típicos:

Construcción de casas con múltiples características

Creación de personajes en videojuegos

Configuración de pedidos, autos, computadores, reportes, etc.

Objetos con decenas de parámetros

El constructor clásico termina siendo un antipatrón llamado constructor telescópico.

✔️ Solución

Builder propone:

Crear un objeto constructor separado (Builder)

Métodos encadenados (fluent interface)

Un método final build() que retorna el objeto completo

Código legible, claro y fácil de extender

🗂️ Estructura del Proyecto
builder/
├── src/
│   ├── __init__.py
│   ├── patron_builder.py          # Implementación del patrón Builder
│   └── antipatron_builder.py      # Implementación del antipatrón (constructor gigante)
├── examples/
│   ├── ejemplo_builder.py         # Ejemplos de uso del patrón
│   └── ejemplo_antipatron.py      # Ejemplo del antipatrón
├── tests/
│   └── test_builder.py            # Tests unitarios
└── README.md                      # Este archivo

🧱 Implementación del Patrón Builder
Builder (Recomendado)
# PATRÓN BUILDER: Construcción paso a paso
class CasaBuilder:
    def __init__(self):
        # Inicializar con valores por defecto razonables
        self.puertas = 4
        self.ventanas = 8
        self.garaje = False
        self.piscina = False
        self.jardin = False
        self.sotano = False
        self.techo = "teja"
        self.paredes = "concreto"
    
    # Cada método permite ajustar un atributo
    # Y devuelve self para permitir encadenamiento
    def con_puertas(self, cantidad):
        self.puertas = cantidad
        return self

    def con_ventanas(self, cantidad):
        self.ventanas = cantidad
        return self
    
    def con_garaje(self, tiene=True):
        self.garaje = tiene
        return self
    
    def con_piscina(self, tiene=True):
        self.piscina = tiene
        return self
    
    def con_jardin(self, tiene=True):
        self.jardin = tiene
        return self

    def con_sotano(self, tiene=True):
        self.sotano = tiene
        return self
    
    def con_techo(self, tipo):
        self.techo = tipo
        return self
    
    def con_paredes(self, material):
        self.paredes = material
        return self
    
    def build(self):
        return Casa(
            self.puertas, self.ventanas, self.garaje,
            self.piscina, self.jardin, self.sotano,
            self.techo, self.paredes
        )


class Casa:
    def __init__(self, puertas, ventanas, garaje, piscina,
                 jardin, sotano, techo, paredes):
        self.puertas = puertas
        self.ventanas = ventanas
        self.garaje = garaje
        self.piscina = piscina
        self.jardin = jardin
        self.sotano = sotano
        self.techo = techo
        self.paredes = paredes


👉 Ventajas del Builder

Código súper legible

Puedes construir solo lo que necesitas

No hay riesgo de confundir parámetros

Muy fácil de extender

No requiere constructores gigantes

❌ Antipatrón: Constructor Telescópico
# ANTIPATRÓN: Constructor gigante con muchos parámetros
class Casa:
    def __init__(self, puertas=None, ventanas=None, garaje=None, 
                 piscina=None, jardin=None, sotano=None, 
                 techo=None, paredes=None):

        self.puertas = puertas or 4
        self.ventanas = ventanas or 8
        self.garaje = garaje or False
        self.piscina = piscina or False
        self.jardin = jardin or False
        self.sotano = sotano or False
        self.techo = techo or "teja"
        self.paredes = paredes or "concreto"


👉 Desventajas

Difícil de leer

Fácil de equivocarse

No escalable

No autoexplicativo

Causa bugs fácilmente

Ejemplos Incluidos
Builder

Casa de lujo

Casa moderna

Casa simple

Construcción paso a paso con claridad

Antipatrón

Constructor gigante

Parámetros desordenados

Bugs por confusión de argumentos

Ejecutar los Ejemplos
python examples/ejemplo_builder.py
python examples/ejemplo_antipatron.py

Cuándo Usar Builder

✓ Usar Builder cuando:

Tienes muchos parámetros opcionales

Quieres un código legible

Necesitas muchas combinaciones de configuración

Quieres evitar constructores gigantes

✗ NO usar Builder cuando:

El objeto es muy simple

Solo tiene 1–3 atributos

No necesitas configuraciones diferentes

Consideraciones Importantes
Legibilidad / Mantenibilidad

Builder mejora dramáticamente la claridad del código.

Extensibilidad

Agregar nuevos atributos es muy fácil — no rompes nada.

Fluent Interface

Los métodos encadenados hacen el código natural:

casa = (CasaBuilder()
        .con_piscina()
        .con_garaje()
        .con_techo("metal")
        .build())

Comparación: Patrón vs Antipatrón
Aspecto	Antipatrón (Constructor Gigante)	Builder
Legibilidad	❌ Mala	✅ Alta
Riesgo de errores	❌ Alto	✅ Bajo
Mantenimiento	❌ Difícil	✅ Fácil
Parámetros opcionales	❌ Caos	✅ Ordenados
Extensibilidad	❌ Baja	✅ Alta
