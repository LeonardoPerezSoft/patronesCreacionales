from Prototype.aplicado.documento_prototype_correcto import demo_prototype_correcto
from Prototype.mal_aplicado.documento_prototype_mal_aplicado import demo_prototype_mal_aplicado
from Prototype.sin_patron.documento_sin_prototype import demo_sin_prototype

def main():
    print("=== Ejecutando Prototype aplicado correctamente ===")
    demo_prototype_correcto()
    print("\n")

    print("=== Ejecutando Prototype mal aplicado ===")
    demo_prototype_mal_aplicado()
    print("\n")

    print("=== Ejecutando sin patrón Prototype ===")
    demo_sin_prototype()

if __name__ == "__main__":
    main()