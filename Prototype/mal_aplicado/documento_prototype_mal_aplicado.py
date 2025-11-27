from dataclasses import dataclass

@dataclass
class DocumentoMalPrototype:
    # Aquí mezclamos todo sin separar bien qué es PLANTILLA y qué es contenido
    tipo_documento: str
    formato_fuente: str
    tiene_logo: bool
    margen_superior: int
    margen_inferior: int
    titulo: str
    cuerpo: str
    destinatario: str
    fecha: str

    def clonar(self,
               titulo: str,
               cuerpo: str,
               destinatario: str,
               fecha: str) -> DocumentoMalPrototype:
        """
        Anti-patrón:
        - No estamos partiendo de una PLANTILLA clara.
        - Usamos 'clonar' pero en realidad volvemos a crear TODO el documento,
          como si llamáramos al constructor directamente.
        """
        return DocumentoMalPrototype(
            tipo_documento=self.tipo_documento,
            formato_fuente=self.formato_fuente,
            tiene_logo=self.tiene_logo,
            margen_superior=self.margen_superior,
            margen_inferior=self.margen_inferior,
            titulo=titulo,
            cuerpo=cuerpo,
            destinatario=destinatario,
            fecha=fecha
        )


def demo_prototype_mal_aplicado():
    doc_base = DocumentoMalPrototype(
        tipo_documento="Contrato estándar",
        formato_fuente="Arial 11",
        tiene_logo=True,
        margen_superior=3,
        margen_inferior=3,
        titulo="Base",
        cuerpo="Base",
        destinatario="Base",
        fecha="Base"
    )

    # Podríamos llamar al constructor directamente,
    # pero nos hacemos los interesantes usando 'clonar'
    contrato_ana = doc_base.clonar(
        titulo="Contrato Ana",
        cuerpo="Texto para Ana...",
        destinatario="Ana Gómez",
        fecha="2025-11-20"
    )

    contrato_luis = doc_base.clonar(
        titulo="Contrato Luis",
        cuerpo="Texto para Luis...",
        destinatario="Luis Pérez",
        fecha="2025-11-21"
    )

    print("=== Prototype mal aplicado (anti-patrón) ===")
    print(contrato_ana)
    print(contrato_luis)


if __name__ == "__main__":
    demo_prototype_mal_aplicado()
