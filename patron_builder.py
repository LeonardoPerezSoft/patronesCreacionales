# PATRÓN BUILDER: Construcción paso a paso, clara e intuitiva
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
    
    # Cada método devuelve self para encadenamiento
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
        # Retorna la Casa construida
        return Casa(self.puertas, self.ventanas, self.garaje, 
                   self.piscina, self.jardin, self.sotano, 
                   self.techo, self.paredes)

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
    
    def __str__(self):
        return (f"Casa(puertas={self.puertas}, ventanas={self.ventanas}, "
                f"garaje={self.garaje}, piscina={self.piscina}, "
                f"jardin={self.jardin}, sotano={self.sotano}, "
                f"techo={self.techo}, paredes={self.paredes})")

# VENTAJA: Código claro, legible y fácil de mantener
print("=== PATRÓN BUILDER ===")

# Casa de lujo: clara e intuitiva
casa_lujo = (CasaBuilder()
             .con_puertas(6)
             .con_ventanas(12)
             .con_garaje()
             .con_piscina()
             .con_jardin()
             .con_techo("pizarra")
             .con_paredes("ladrillo")
             .build())
print("Casa Lujo:", casa_lujo)

# Casa simple: solo lo necesario
casa_simple = (CasaBuilder()
               .con_puertas(3)
               .con_ventanas(5)
               .build())
print("Casa Simple:", casa_simple)

# Casa moderna
casa_moderna = (CasaBuilder()
                .con_garaje()
                .con_sotano()
                .con_techo("metal")
                .build())
print("Casa Moderna:", casa_moderna)
