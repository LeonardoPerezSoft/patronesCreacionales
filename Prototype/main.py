from aplicado.documento_prototype_correcto import demo_prototype_correcto
from mal_aplicado.documento_prototype_mal_aplicado import demo_prototype_mal_aplicado
from sin_patron.documento_sin_prototype import demo_sin_prototype

def main():
    demo_prototype_correcto()
    print()
    demo_prototype_mal_aplicado()
    print()
    demo_sin_prototype()

if __name__ == "__main__":
    main()
