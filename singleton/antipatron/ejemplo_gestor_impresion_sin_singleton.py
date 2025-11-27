# -*- coding: utf-8 -*-
"""
CONTRAEJEMPLO: Gestor de Impresion SIN Singleton
=================================================

Este archivo demuestra EXACTAMENTE POR QUE el Singleton es necesario.
Aqui vemos los CONFLICTOS que ocurren cuando NO se usa Singleton.

Escenario: 3 empleados intentan imprimir simultaneamente sin Singleton
Resultado: CAOS - trabajos pierden, se sobrescriben, la impresora recibe comandos conflictivos
"""

import sys
from pathlib import Path
from datetime import datetime
from time import sleep
from threading import Thread, Lock

sys.path.insert(0, str(Path(__file__).parent.parent))


class GestorImpresionSinSingleton:
    """
    CONTRAEJEMPLO: Clase que SIMULA un Gestor de Impresion
    pero SIN aplicar el patron Singleton.
    
    Cada vez que se crea una instancia, es INDEPENDIENTE.
    Esto causa CONFLICTOS cuando multiples empleados la usan.
    """
    
    def __init__(self, id_gestor: int):
        self.id_gestor = id_gestor
        self.cola_trabajos = []
        self.trabajos_procesados = []
        self.estado_impresora = "disponible"
        self.contador_llamadas = 0
    
    def enviar_trabajo(self, empleado: str, documento: str, paginas: int):
        """Envia un trabajo a ESTA instancia"""
        self.contador_llamadas += 1
        trabajo = {
            "id": len(self.cola_trabajos) + 1,
            "empleado": empleado,
            "documento": documento,
            "paginas": paginas,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "gestor_id": self.id_gestor
        }
        self.cola_trabajos.append(trabajo)
        
        print(f"[Gestor #{self.id_gestor}] {empleado} envio '{documento}'")
        print(f"  └─ Cola del gestor #{self.id_gestor}: {len(self.cola_trabajos)} trabajos")
        
        return trabajo["id"]
    
    def procesar_cola(self):
        """Procesa UNA SOLA cola (la de ESTE gestor)"""
        if not self.cola_trabajos:
            return False
        
        trabajo = self.cola_trabajos.pop(0)
        self.estado_impresora = "ocupada"
        
        print(f"\n[IMPRIMIENDO en Gestor #{self.id_gestor}] {trabajo['documento']}")
        sleep(trabajo["paginas"] * 0.2)
        
        self.trabajos_procesados.append(trabajo)
        self.estado_impresora = "disponible"
        
        print(f"[LISTO en Gestor #{self.id_gestor}] {trabajo['documento']}")
        
        return True
    
    def obtener_estado(self):
        """Obtiene el estado SOLO de esta instancia"""
        return {
            "gestor_id": self.id_gestor,
            "cola": len(self.cola_trabajos),
            "procesados": len(self.trabajos_procesados),
            "estado": self.estado_impresora
        }


def demo_conflicto_basico():
    """
    Demuestra el PROBLEMA BASICO: multiples colas independientes
    """
    print("\n" + "=" * 80)
    print("CONFLICTO 1: MULTIPLES COLAS INDEPENDIENTES")
    print("=" * 80)
    print("""
    El problema fundamental: cada gestor es INDEPENDIENTE
    
    Empleado 1 → Gestor #1 → Cola propia
    Empleado 2 → Gestor #2 → Cola propia
    Empleado 3 → Gestor #3 → Cola propia
    
    RESULTADO: 3 colas separadas, NINGUNA coordinada
    """)
    
    # Crear 3 gestores INDEPENDIENTES (como si cada empleado tuviera el suyo)
    gestor_juan = GestorImpresionSinSingleton(1)
    gestor_maria = GestorImpresionSinSingleton(2)
    gestor_pedro = GestorImpresionSinSingleton(3)
    
    print("Empleados enviando trabajos...\n")
    
    # Juan envia a SU gestor
    gestor_juan.enviar_trabajo("Juan", "Reporte", 3)
    gestor_juan.enviar_trabajo("Juan", "Factura", 1)
    
    # Maria envia a SU gestor
    gestor_maria.enviar_trabajo("Maria", "Presentacion", 2)
    
    # Pedro envia a SU gestor
    gestor_pedro.enviar_trabajo("Pedro", "Contrato", 5)
    
    print("\n" + "-" * 80)
    print("ESTADO DE LAS COLAS (sin sincronizacion):")
    print("-" * 80)
    
    print(f"Gestor #1 (Juan):  {gestor_juan.obtener_estado()}")
    print(f"Gestor #2 (Maria): {gestor_maria.obtener_estado()}")
    print(f"Gestor #3 (Pedro): {gestor_pedro.obtener_estado()}")
    
    print("\n❌ PROBLEMA: La impresora no sabe cual cola procesar primero!")
    print("❌ PROBLEMA: Los trabajos se pueden perder o procesar en orden incorrecto!")
    print("❌ PROBLEMA: No hay un punto central de control!")


def demo_conflicto_referencia():
    """
    Demuestra el PROBLEMA DE REFERENCIA: cambiar una instancia NO afecta a otras
    """
    print("\n" + "=" * 80)
    print("CONFLICTO 2: REFERENCIAS INDEPENDIENTES")
    print("=" * 80)
    print("""
    Aunque dos variables se llamen igual, si no usan Singleton,
    estan APUNTANDO A DIFERENTES OBJETOS
    """)
    
    # Dos "referencias" al "mismo" gestor (pero NO es lo mismo)
    gestor_1 = GestorImpresionSinSingleton(1)
    gestor_2 = GestorImpresionSinSingleton(2)  # ← DIFERENTE instancia!
    
    print(f"\n¿gestor_1 es gestor_2?: {gestor_1 is gestor_2}")
    print(f"ID de gestor_1: {id(gestor_1)}")
    print(f"ID de gestor_2: {id(gestor_2)}")
    
    print("\nEnviando trabajo desde gestor_1...")
    gestor_1.enviar_trabajo("Juan", "Documento", 2)
    
    print("\nIntentando acceder desde gestor_2...")
    print(f"Cola de gestor_1: {len(gestor_1.cola_trabajos)} trabajos")
    print(f"Cola de gestor_2: {len(gestor_2.cola_trabajos)} trabajos")
    
    print("\n❌ PROBLEMA: gestor_2 NO ve el trabajo que envio gestor_1!")
    print("❌ PROBLEMA: Estan usando diferentes colas aunque sea 'el mismo gestor'!")


def demo_conflicto_estado():
    """
    Demuestra el PROBLEMA DE ESTADO: estados inconsistentes
    """
    print("\n" + "=" * 80)
    print("CONFLICTO 3: ESTADO INCONSISTENTE")
    print("=" * 80)
    print("""
    Sin Singleton, cada instancia tiene su PROPIO estado.
    Esto lleva a inconsistencias en toda la aplicacion.
    """)
    
    # Crear gestores
    gestor_1 = GestorImpresionSinSingleton(1)
    gestor_2 = GestorImpresionSinSingleton(2)
    
    print("\nGestor #1 envia 5 trabajos...")
    for i in range(5):
        gestor_1.enviar_trabajo(f"Empleado{i}", f"Doc{i}", 1)
    
    print("\nGestor #2 envia 0 trabajos...")
    
    print("\n" + "-" * 80)
    print("ESTADOS INCONSISTENTES:")
    print("-" * 80)
    
    estado1 = gestor_1.obtener_estado()
    estado2 = gestor_2.obtener_estado()
    
    print(f"Gestor #1: {estado1['cola']} en cola")
    print(f"Gestor #2: {estado2['cola']} en cola")
    print(f"TOTAL: {estado1['cola'] + estado2['cola']} trabajos en el sistema")
    
    print("\n❌ PROBLEMA: Informacion esparcida en multiples objetos!")
    print("❌ PROBLEMA: Es imposible obtener un REPORTE UNIFICADO!")
    print("❌ PROBLEMA: Auditar es imposible!")


def demo_conflicto_concurrencia():
    """
    Demuestra el PEOR PROBLEMA: condiciones de carrera (race conditions)
    """
    print("\n" + "=" * 80)
    print("CONFLICTO 4: CONDICIONES DE CARRERA (RACE CONDITIONS)")
    print("=" * 80)
    print("""
    Cuando multiples threads acceden a diferentes gestores simultaneamente,
    la impresora podria recibir comandos CONTRADICTORIOS.
    """)
    
    gestor_1 = GestorImpresionSinSingleton(1)
    gestor_2 = GestorImpresionSinSingleton(2)
    
    print("\nEscenario:")
    print("- Juan (Gestor #1) intenta imprimir")
    print("- Maria (Gestor #2) intenta imprimir")
    print("- Al MISMO TIEMPO\n")
    
    def juan_imprime():
        print("[Juan] Enviando trabajo...")
        gestor_1.enviar_trabajo("Juan", "ReporteJuan", 2)
        print("[Juan] Procesar cola...")
        gestor_1.procesar_cola()
    
    def maria_imprime():
        sleep(0.1)  # Pequeno delay para que se vean los conflictos
        print("[Maria] Enviando trabajo...")
        gestor_2.enviar_trabajo("Maria", "ReporteMaria", 2)
        print("[Maria] Procesar cola...")
        gestor_2.procesar_cola()
    
    print("Ejecutando simultaneamente...\n")
    
    thread_juan = Thread(target=juan_imprime, daemon=True)
    thread_maria = Thread(target=maria_imprime, daemon=True)
    
    thread_juan.start()
    thread_maria.start()
    
    thread_juan.join()
    thread_maria.join()
    
    print("\n❌ PROBLEMA: La impresora podria recibir ambos comandos!")
    print("❌ PROBLEMA: Quien gana? Juan o Maria?")
    print("❌ PROBLEMA: Los documentos podrian mezclarse!")
    print("❌ PROBLEMA: Sin Singleton NO hay coordinacion!")


def resumen_conflictos():
    """
    Resume todos los conflictos encontrados
    """
    print("\n" + "=" * 80)
    print("RESUMEN: POR QUE EL SINGLETON ES NECESARIO")
    print("=" * 80)
    
    conflictos = """
    CONFLICTO 1: Multiples Colas Independientes
    ════════════════════════════════════════════════════════════
    SIN Singleton:
        Gestor #1 → Cola #1
        Gestor #2 → Cola #2
        Gestor #3 → Cola #3
    
    RESULTADO: La impresora no sabe cual procesar → CAOS
    
    CON Singleton:
        Gestor #1 → \
        Gestor #2 → ├─→ UNA SOLA COLA
        Gestor #3 → /
    
    RESULTADO: Ordenamiento garantizado
    
    
    CONFLICTO 2: Referencias Independientes
    ════════════════════════════════════════════════════════════
    SIN Singleton:
        gestor_1 → Objeto #1 (id: 12345)
        gestor_2 → Objeto #2 (id: 67890)  ← DIFERENTE!
    
    RESULTADO: gestores_1.cola != gestores_2.cola
    
    CON Singleton:
        gestor_1 → Objeto UNICO (id: 12345)
        gestor_2 → Objeto UNICO (id: 12345)  ← MISMO!
    
    RESULTADO: Siempre ven la misma cola
    
    
    CONFLICTO 3: Estado Inconsistente
    ════════════════════════════════════════════════════════════
    SIN Singleton:
        Gestor #1: 5 trabajos
        Gestor #2: 3 trabajos
        Gestor #3: 2 trabajos
        TOTAL: ???  (disperso, imposible de auditar)
    
    RESULTADO: No hay visibilidad global
    
    CON Singleton:
        Gestor UNICO: 10 trabajos
        TOTAL: 10  (centralizazo, facil de auditar)
    
    RESULTADO: Visibilidad completa
    
    
    CONFLICTO 4: Race Conditions
    ════════════════════════════════════════════════════════════
    SIN Singleton (threads):
        Thread 1 (Juan)  → intenta usar Gestor #1
        Thread 2 (Maria) → intenta usar Gestor #2
        LA IMPRESORA REAL → recibe comandos CONFLICTIVOS
    
    RESULTADO: Documentos perdidos, mezclados, corruptos
    
    CON Singleton (threads):
        Thread 1 (Juan)  → \
        Thread 2 (Maria) → ├─→ Lock en Singleton
        LA IMPRESORA REAL → recibe comandos ORDENADOS
    
    RESULTADO: Sin conflictos, seguro en threads
    
    
    CONCLUSION
    ════════════════════════════════════════════════════════════
    El Singleton NO es opcional en este caso.
    Es ESENCIAL porque:
    
    1. Existe UNA SOLA impresora fisica
    2. Solo ELLA puede processar UN trabajo a la vez
    3. Los trabajos DEBEN procesarse en orden
    4. Sin Singleton → multiples colas → CONFLICTO
    5. Con Singleton → una cola → ORDEN y SEGURIDAD
    
    El Singleton garantiza:
    ✓ Una unica cola
    ✓ Acceso coordinado
    ✓ Ordenamiento FIFO
    ✓ Thread-safety
    ✓ Visibilidad global
    ✓ Auditoría completa
    """
    
    print(conflictos)


if __name__ == "__main__":
    print("\n")
    print("=" * 80)
    print("CONTRAEJEMPLO: GESTOR DE IMPRESION SIN SINGLETON")
    print("=" * 80)
    print("""
    Este programa demuestra EXACTAMENTE POR QUE el patron Singleton
    es NECESARIO para el Gestor de Impresion.
    
    Veras 4 CONFLICTOS principales que ocurren sin Singleton:
    """)
    
    # Ejecutar demostraciones
    demo_conflicto_basico()
    demo_conflicto_referencia()
    demo_conflicto_estado()
    demo_conflicto_concurrencia()
    
    # Mostrar resumen
    resumen_conflictos()
    
    print("\n" + "=" * 80)
    print("CONCLUSION: El Singleton RESUELVE TODOS estos problemas")
    print("=" * 80)
    print("""
    Ahora ejecuta: python examples/ejemplo_gestor_impresion.py
    
    Para ver como el Singleton SOLUCIONA cada conflicto presentado aqui.
    """)
