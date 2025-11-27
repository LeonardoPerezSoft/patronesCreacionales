# ANTIPATRÓN: Constructor gigante con muchos parámetros
# Este tipo de clase es difícil de usar porque requiere recordar
# el ORDEN y el SIGNIFICADO de muchos parámetros.

class Casa:
    def __init__(self, puertas=None, ventanas=None, garaje=None, 
                 piscina=None, jardin=None, sotano=None, 
                 techo=None, paredes=None):
        # Se asignan valores por defecto si no se pasan argumentos.
        # PERO este enfoque hace el código confuso y propenso a errores.
        self.puertas = puertas or 4
        self.ventanas = ventanas or 8
        self.garaje = garaje or False
        self.piscina = piscina or False
        self.jardin = jardin or False
        self.sotano = sotano or False
        self.techo = techo or "teja"
        self.paredes = paredes or "concreto"
    
    def __str__(self):
        # Representación de la casa
        return (f"Casa(puertas={self.puertas}, ventanas={self.ventanas}, "
                f"garaje={self.garaje}, piscina={self.piscina}, "
                f"jardin={self.jardin}, sotano={self.sotano}, "
                f"techo={self.techo}, paredes={self.paredes})")


# === EJEMPLOS DE POR QUÉ ESTO ES UN ANTIPATRÓN ===

print("Hola Adriana")

# Problema 1: Llamada llena de parámetros
# Aquí hay muchos valores True/False seguidos. A simple vista,
# NO se entiende cuál corresponde a qué.
casa1 = Casa(4, 8, True, False, True, False, "teja", "concreto")
print("Casa 1:", casa1)

# Problema 2: Si cambias el orden, rompes todo.
# Aquí usamos solo algunos parámetros por nombre.
# El resto quedan por defecto.
# Parece útil, pero causa inconsistencias porque los defaults
# se mezclan con valores explícitos.
casa2 = Casa(piscina=True, garaje=True)
print("Casa 2:", casa2)

# Problema 3: Código difícil de leer.
# ¿Qué es cada None? ¿Qué significa ese True? ¿Qué significa ese False?
# Un desarrollador NO PUEDE leer esto rápido.
casa3 = Casa(None, None, True, True, None, False, "pizarra", "ladrillo")
print("Casa 3:", casa3)
