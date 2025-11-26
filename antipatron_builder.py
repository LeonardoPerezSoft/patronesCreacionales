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
    
    def __str__(self):
        return (f"Casa(puertas={self.puertas}, ventanas={self.ventanas}, "
                f"garaje={self.garaje}, piscina={self.piscina}, "
                f"jardin={self.jardin}, sotano={self.sotano}, "
                f"techo={self.techo}, paredes={self.paredes})")

# PROBLEMA: ¿Qué significa cada True/False? Código confuso y propenso a errores
print("Hola Adriana")
casa1 = Casa(4, 8, True, False, True, False, "teja", "concreto")
print("Casa 1:", casa1)

# ¿Qué pasa si olvidas el orden o te confundes?
casa2 = Casa(piscina=True, garaje=True)  # Otros parámetros por defecto
print("Casa 2:", casa2)

# Difícil de leer y mantener
casa3 = Casa(None, None, True, True, None, False, "pizarra", "ladrillo")
print("Casa 3:", casa3)
