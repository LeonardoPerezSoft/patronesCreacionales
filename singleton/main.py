# -*- coding: utf-8 -*-
"""
Script principal para demostrar el Gestor de Impresion
Compara: SIN Singleton vs CON Singleton
"""

import sys
from pathlib import Path
import os

# Agregar la raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent))


def ejecutar_demostracion():
    """Ejecuta la demostración comparativa"""
    
    print("\n")
    print("=" * 80)
    print("DEMOSTRACIÓN: GESTOR DE IMPRESION - SINGLETON vs SIN SINGLETON".center(80))
    print("=" * 80)
    
    print("""
    Este programa demuestra por que el patron Singleton es NECESARIO
    para un Gestor de Impresion.
    
    Veremos:
    1. Los PROBLEMAS sin Singleton
    2. La SOLUCION con Singleton
    """)
    
    input("\nPresiona Enter para empezar con el CONTRAEJEMPLO (Sin Singleton)...")
    
    # Ejecutar el contraejemplo (sin singleton)
    print("\n" + "=" * 80)
    print("PARTE 1: CONTRAEJEMPLO - GESTOR DE IMPRESION SIN SINGLETON".center(80))
    print("=" * 80)
    print("""
    Este programa muestra los CONFLICTOS que ocurren cuando NO usamos Singleton.
    Veras 4 problemas principales:
    1. Multiples colas independientes
    2. Referencias independientes
    3. Estado inconsistente
    4. Race conditions
    """)
    
    os.system("python examples/ejemplo_gestor_impresion_sin_singleton.py")
    
    input("\n\nPresiona Enter para ver la SOLUCION (Con Singleton)...")
    
    # Ejecutar el ejemplo con singleton
    print("\n" + "=" * 80)
    print("PARTE 2: SOLUCION - GESTOR DE IMPRESION CON SINGLETON".center(80))
    print("=" * 80)
    print("""
    Este programa muestra como el Singleton RESUELVE todos los problemas.
    Veras:
    1. Una unica cola coordinada
    2. Un punto de acceso global
    3. Estado centralizado y consistente
    4. Thread-safety garantizado
    """)
    
    os.system("python examples/ejemplo_gestor_impresion.py")
    
    # Mostrar conclusión
    print("\n" + "=" * 80)
    print("CONCLUSIÓN".center(80))
    print("=" * 80)
    print("""
    COMPARACIÓN:
    ═══════════════════════════════════════════════════════════════════════════
    
    SIN SINGLETON (Contraejemplo):
    ────────────────────────────────────────────────────────────────────────────
    ❌ Multiples colas independientes
    ❌ Cada instancia tiene su propio estado
    ❌ Imposible coordinacion central
    ❌ Race conditions en threads
    ❌ Trabajos pueden perderse o mezclarse
    ❌ Auditoría imposible
    ❌ Caos total en la impresora
    
    
    CON SINGLETON (Solucion):
    ────────────────────────────────────────────────────────────────────────────
    ✓ Una unica cola coordinada
    ✓ Estado centralizado
    ✓ Punto de acceso global garantizado
    ✓ Thread-safe con locks
    ✓ Trabajos procesados en orden FIFO
    ✓ Auditoría completa
    ✓ Orden y seguridad garantizados
    
    
    POR QUE EL SINGLETON ES NECESARIO:
    ════════════════════════════════════════════════════════════════════════════
    
    Existe UNA sola impresora fisica.
    
    Una sola impresora SOLO puede procesar UN trabajo a la vez.
    
    Los trabajos DEBEN procesarse en orden.
    
    Sin Singleton → multiples colas → conflicto → caos
    Con Singleton → una cola → orden → seguridad
    
    El Singleton es la GARANTIA de que una unica recurso (impresora)
    es accedido de forma segura y coordinada.
    
    ═════════════════════════════════════════════════════════════════════════════
    """)


if __name__ == "__main__":
    try:
        ejecutar_demostracion()
    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
