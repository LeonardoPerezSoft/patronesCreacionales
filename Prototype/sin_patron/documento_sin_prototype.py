from dataclasses import dataclass

@dataclass
class DocumentoSimple:
    tipo_documento: str
    formato_fuente: str
    tiene_logo: bool
    margen_superior: int
    margen_inferior: int
    titulo: str
    cuerpo: str
    destinatario: str
    fecha: str


def demo_sin_prototype():
    print("=== Sin Prototype (todo a mano) ===")

    contrato_ana = DocumentoSimple(
        tipo_documento="Contrato estándar",
        formato_fuente="Arial 11",
        tiene_logo=True,
        margen_superior=3,
        margen_inferior=3,
        titulo="Contrato de servicios - Ana",
        cuerpo="Texto del contrato para Ana...",
        destinatario="Ana Gómez",
        fecha="2025-11-20"
    )

    contrato_luis = DocumentoSimple(
        tipo_documento="Contrato estándar",
        formato_fuente="Arial 11",
        tiene_logo=True,
        margen_superior=3,
        margen_inferior=3,
        titulo="Contrato de servicios - Luis",
        cuerpo="Texto del contrato para Luis...",
        destinatario="Luis Pérez",
        fecha="2025-11-21"
    )

    print(contrato_ana)
    print(contrato_luis)


if __name__ == "__main__":
    demo_sin_prototype()
