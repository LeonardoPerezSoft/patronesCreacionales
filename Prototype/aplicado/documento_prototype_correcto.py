from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass

@dataclass
class Documento:
    # Parte de la PLANTILLA (no cambia casi nunca)
    tipo_documento: str        # ej: "Contrato estándar", "Acta de reunión"
    formato_fuente: str        # ej: "Arial 11"
    tiene_logo: bool
    margen_superior: int
    margen_inferior: int

    # Parte que cambia por cada instancia concreta
    titulo: str
    cuerpo: str
    destinatario: str
    fecha: str

    def clonar(self,
               titulo: str,
               cuerpo: str,
               destinatario: str,
               fecha: str) -> Documento:
        """
        Prototype aplicado correctamente:
        - Copiamos todo el formato y configuración de la PLANTILLA.
        - Cambiamos sólo los datos específicos.
        """
        nuevo_doc = deepcopy(self)
        nuevo_doc.titulo = titulo
        nuevo_doc.cuerpo = cuerpo
        nuevo_doc.destinatario = destinatario
        nuevo_doc.fecha = fecha
        return nuevo_doc


def demo_prototype_correcto():
    # Creamos una PLANTILLA de documento (como en Word/Google Docs)
    plantilla_contrato = Documento(
        tipo_documento="Contrato estándar",
        formato_fuente="Arial 11",
        tiene_logo=True,
        margen_superior=3,
        margen_inferior=3,
        titulo="(TÍTULO PENDIENTE)",
        cuerpo="(CUERPO DEL CONTRATO PENDIENTE)",
        destinatario="(DESTINATARIO)",
        fecha="(FECHA)"
    )

    # Clonamos la plantilla para distintos clientes
    contrato_cliente_ana = plantilla_contrato.clonar(
        titulo="Contrato de servicios - Ana",
        cuerpo="Texto del contrato para Ana...",
        destinatario="Ana Gómez",
        fecha="2025-11-20"
    )

    contrato_cliente_luis = plantilla_contrato.clonar(
        titulo="Contrato de servicios - Luis",
        cuerpo="Texto del contrato para Luis...",
        destinatario="Luis Pérez",
        fecha="2025-11-21"
    )

    print("=== Prototype aplicado correctamente (plantillas de documentos) ===")
    print(contrato_cliente_ana)
    print(contrato_cliente_luis)


if __name__ == "__main__":
    demo_prototype_correcto()
