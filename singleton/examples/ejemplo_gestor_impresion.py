# -*- coding: utf-8 -*-
"""
Ejemplo Práctico: Gestor de Impresión con Singleton

Escenario:
    Una oficina con múltiples empleados que necesitan imprimir documentos.
    Solo hay UNA impresora física que procesa trabajos de manera ordenada.
    
Problema sin Singleton:
    Si cada empleado crea su propia "cola de impresión", los trabajos se pierden
    o se sobrescriben, causando caos.
    
Solución con Singleton:
    Un único Gestor de Impresión (Singleton) que garantiza:
    • Una sola cola de impresión
    • Procesamiento ordenado de todos los trabajos
    • Punto de acceso global desde cualquier empleado
    • Seguimiento completo de todos los trabajos
"""

import sys
from pathlib import Path
from datetime import datetime
from time import sleep

# Agregar la raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.singleton_decorator import singleton


@singleton
class GestorImpresion:
    """
    Singleton que gestiona la cola de impresión de toda la oficina.
    
    Garantiza que:
    ✓ Solo existe una única cola de impresión
    ✓ Todos los empleados comparten la misma cola
    ✓ Los trabajos se procesan en orden FIFO (First In, First Out)
    ✓ No hay pérdida de trabajos
    ✓ Se mantiene un registro de todos los trabajos
    """
    
    def __init__(self):
        self.cola_trabajos = []
        self.trabajos_procesados = []
        self.trabajo_actual = None
        self.impresora_ocupada = False
    
    def enviar_trabajo(self, empleado: str, documento: str, paginas: int) -> int:
        """
        Un empleado envía un trabajo a la impresora.
        
        Args:
            empleado: Nombre del empleado que solicita la impresión
            documento: Nombre/descripción del documento
            paginas: Número de páginas a imprimir
        
        Returns:
            ID del trabajo en la cola
        """
        # Crear trabajo
        trabajo = {
            "id": len(self.cola_trabajos) + 1,
            "empleado": empleado,
            "documento": documento,
            "paginas": paginas,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "estado": "en_cola"
        }
        
        # Agregar a la cola
        self.cola_trabajos.append(trabajo)
        
        print(f"[{trabajo['timestamp']}] ✉️  {empleado} envía '{documento}' ({paginas} pág.)")
        print(f"            └─ ID: {trabajo['id']} | Posición en cola: {len(self.cola_trabajos)}")
        
        return trabajo["id"]
    
    def procesar_cola(self) -> bool:
        """
        Procesa el siguiente trabajo en la cola.
        Simula el tiempo de impresión basado en el número de páginas.
        
        Returns:
            True si se procesó un trabajo, False si la cola está vacía
        """
        if not self.cola_trabajos:
            return False
        
        # Obtener el primer trabajo de la cola
        trabajo = self.cola_trabajos.pop(0)
        self.trabajo_actual = trabajo
        self.impresora_ocupada = True
        
        # Simular tiempo de impresión (0.2 segundos por página)
        tiempo_impresion = trabajo["paginas"] * 0.2
        
        print(f"\n[🖨️  IMPRIMIENDO] {trabajo['empleado']} - '{trabajo['documento']}'")
        print(f"    Páginas: {trabajo['paginas']} | Tiempo estimado: {tiempo_impresion:.1f}s")
        
        # Simular impresión
        sleep(tiempo_impresion)
        
        # Marcar como procesado
        trabajo["estado"] = "completado"
        trabajo["timestamp_completado"] = datetime.now().strftime("%H:%M:%S")
        self.trabajos_procesados.append(trabajo)
        
        print(f"[✅ LISTO] {trabajo['documento']} impreso para {trabajo['empleado']}")
        
        self.trabajo_actual = None
        self.impresora_ocupada = False
        
        return True
    
    def obtener_estado_cola(self) -> dict:
        """Retorna el estado actual de la cola"""
        return {
            "trabajos_en_cola": len(self.cola_trabajos),
            "trabajos_procesados": len(self.trabajos_procesados),
            "trabajo_actual": self.trabajo_actual,
            "impresora_ocupada": self.impresora_ocupada
        }
    
    def obtener_reporte(self) -> str:
        """Genera un reporte completo de todos los trabajos"""
        reporte = "=" * 70 + "\n"
        reporte += "REPORTE DE IMPRESIÓN\n"
        reporte += "=" * 70 + "\n\n"
        
        # Trabajos procesados
        reporte += f"✅ TRABAJOS COMPLETADOS ({len(self.trabajos_procesados)}):\n"
        reporte += "-" * 70 + "\n"
        
        if self.trabajos_procesados:
            for i, trabajo in enumerate(self.trabajos_procesados, 1):
                reporte += f"{i}. [{trabajo['timestamp']}] {trabajo['empleado']}\n"
                reporte += f"   └─ Documento: {trabajo['documento']}\n"
                reporte += f"   └─ Páginas: {trabajo['paginas']}\n"
                reporte += f"   └─ Completado: {trabajo.get('timestamp_completado', 'N/A')}\n\n"
        else:
            reporte += "No hay trabajos completados aún.\n\n"
        
        # Trabajos en cola
        reporte += f"⏳ TRABAJOS EN COLA ({len(self.cola_trabajos)}):\n"
        reporte += "-" * 70 + "\n"
        
        if self.cola_trabajos:
            for i, trabajo in enumerate(self.cola_trabajos, 1):
                reporte += f"{i}. [{trabajo['timestamp']}] {trabajo['empleado']}\n"
                reporte += f"   └─ Documento: {trabajo['documento']}\n"
                reporte += f"   └─ Páginas: {trabajo['paginas']}\n\n"
        else:
            reporte += "No hay trabajos en espera.\n\n"
        
        reporte += "=" * 70 + "\n"
        return reporte


def simular_oficina_sin_singleton():
    """
    ESCENARIO PROBLEMÁTICO: Sin Singleton
    (Ilustración del problema - no es código real)
    """
    print("\n" + "=" * 70)
    print("ESCENARIO SIN SINGLETON (¿QUÉ PASARÍA?)")
    print("=" * 70)
    print("""
    Cada empleado crearía su propia "cola":
    
    cola_juan = ColasDeImpresion()        # 🚨 Su propia cola
    cola_maria = ColasDeImpresion()       # 🚨 Su propia cola
    cola_pedro = ColasDeImpresion()       # 🚨 Su propia cola
    
    PROBLEMAS:
    ❌ Múltiples colas incompatibles
    ❌ Trabajos pueden perderse o duplicarse
    ❌ No hay control sobre el orden de impresión
    ❌ La impresora recibe comandos conflictivos
    ❌ Imposible seguimiento centralizado
    
    RESULTADO: 📄 CAOS EN LA OFICINA 📄
    """)


def simular_oficina_con_singleton():
    """
    ESCENARIO CON SINGLETON: Correcto y ordenado
    """
    print("\n" + "=" * 70)
    print("SIMULACIÓN: OFICINA CON GESTOR DE IMPRESIÓN (SINGLETON)")
    print("=" * 70)
    print("\n▶ ESCENARIO: 3 Empleados, 1 Impresora, 1 Cola (Singleton)\n")
    
    # Obtener la instancia ÚNICA del gestor
    gestor = GestorImpresion()
    
    # Simular que 3 empleados envían trabajos
    print("📝 FASE 1: Empleados envían trabajos a imprimir")
    print("-" * 70)
    
    # Empleado 1
    gestor.enviar_trabajo("Juan García", "Reporte Trimestral 2025", paginas=5)
    
    # Empleado 2
    gestor.enviar_trabajo("María López", "Presentación Clientes", paginas=3)
    
    # Empleado 3
    gestor.enviar_trabajo("Pedro Ruiz", "Contrato Proveedor", paginas=8)
    
    # Empleado 1 envía otro trabajo
    gestor.enviar_trabajo("Juan García", "Factura #001", paginas=2)
    
    # Empleado 2 envía otro trabajo
    gestor.enviar_trabajo("María López", "Email Confirmación", paginas=1)
    
    # Mostrar estado de la cola
    print("\n📊 FASE 2: Estado de la Cola")
    print("-" * 70)
    estado = gestor.obtener_estado_cola()
    print(f"Trabajos en cola: {estado['trabajos_en_cola']}")
    print(f"Trabajos procesados: {estado['trabajos_procesados']}")
    print(f"¿Impresora ocupada?: {'Sí' if estado['impresora_ocupada'] else 'No'}")
    
    # Procesar todos los trabajos
    print("\n🖨️  FASE 3: Procesamiento de trabajos")
    print("-" * 70)
    
    trabajo_num = 1
    while gestor.procesar_cola():
        trabajo_num += 1
    
    # Mostrar reporte final
    print("\n" + gestor.obtener_reporte())


def demostrar_punto_acceso_global():
    """
    Demuestra que múltiples referencias acceden al MISMO gestor
    """
    print("\n" + "=" * 70)
    print("PRUEBA: PUNTO DE ACCESO GLOBAL")
    print("=" * 70)
    print("\n✓ Verificación de que el Singleton funciona correctamente:\n")
    
    # Obtener instancia desde 3 "empleados" diferentes
    gestor1 = GestorImpresion()  # Juan accede al gestor
    gestor2 = GestorImpresion()  # María accede al gestor
    gestor3 = GestorImpresion()  # Pedro accede al gestor
    
    # Verificar que son la MISMA instancia
    print(f"¿gestor1 es gestor2?: {gestor1 is gestor2}")
    print(f"¿gestor2 es gestor3?: {gestor2 is gestor3}")
    print(f"¿gestor1 es gestor3?: {gestor1 is gestor3}")
    
    print(f"\nID de gestor1: {id(gestor1)}")
    print(f"ID de gestor2: {id(gestor2)}")
    print(f"ID de gestor3: {id(gestor3)}")
    
    print("\n✅ CONFIRMADO: Todos los empleados acceden a la MISMA instancia")
    print("   Esto garantiza una única cola de impresión para toda la oficina.")
    
    # Enviar trabajo desde diferentes referencias
    print("\n📝 Prueba de funcionamiento:")
    gestor1.enviar_trabajo("Juan (ref1)", "Documento 1", 2)
    gestor2.enviar_trabajo("María (ref2)", "Documento 2", 3)
    gestor3.enviar_trabajo("Pedro (ref3)", "Documento 3", 1)
    
    print(f"\n✓ Total de trabajos en cola: {len(gestor1.cola_trabajos)}")
    print("  (Verificado desde todas las referencias - misma cola)")


def demostrar_ventajas_singleton():
    """
    Explica las ventajas del Singleton en este contexto
    """
    print("\n" + "=" * 70)
    print("VENTAJAS DEL SINGLETON: GESTOR DE IMPRESIÓN")
    print("=" * 70)
    print("""
    1. ✅ INSTANCIA ÚNICA
       • Solo 1 gestión de impresión en toda la oficina
       • Imposible crear colas duplicadas accidentalmente
       • Garantiza un único punto de control

    2. ✅ COLA ORDENADA
       • Los trabajos se procesan en orden FIFO (primero en llegar, primero en salir)
       • No hay pérdida de trabajos
       • Todos los empleados saben que sus trabajos serán procesados

    3. ✅ PUNTO DE ACCESO GLOBAL
       • Cualquier empleado (parte del programa) accede al mismo gestor
       • No necesita pasar referencias entre módulos
       • Código más limpio: GestorImpresion().enviar_trabajo(...)

    4. ✅ SEGUIMIENTO CENTRALIZADO
       • Historial completo de todos los trabajos
       • Reporte de impresiones procesadas
       • Auditoría y control de impresión

    5. ✅ SINCRONIZACIÓN
       • Los trabajos no se sobrescriben
       • La impresora no recibe comandos contradictorios
       • Orden garantizado de ejecución

    6. ✅ ESCALABILIDAD
       • Si agregas 100 empleados, siguen usando la MISMA cola
       • El código no cambia
       • Sin problemas de concurrencia

    EJEMPLO REAL: Impresoras en Red
    ───────────────────────────────
    En una oficina real:
    • 50 empleados compartiendo 3 impresoras
    • Un Gestor de Impresión (Singleton) por cada impresora
    • Sistema operativo garantiza que solo existe 1 por cada impresora
    • Todos los trabajos se procesan en orden y sin conflictos
    """)


if __name__ == "__main__":
    print("\n")
    print("=" * 70)
    print("EJEMPLO: GESTOR DE IMPRESION CON SINGLETON".center(70))
    print("Una oficina, una impresora, una cola, un Singleton".center(70))
    print("=" * 70)
    
    # Mostrar el problema sin singleton
    simular_oficina_sin_singleton()
    
    # Demostrar el singleton
    simular_oficina_con_singleton()
    
    # Verificar punto de acceso global
    demostrar_punto_acceso_global()
    
    # Mostrar ventajas
    demostrar_ventajas_singleton()
    
    print("\n✅ Ejemplo completado exitosamente\n")
