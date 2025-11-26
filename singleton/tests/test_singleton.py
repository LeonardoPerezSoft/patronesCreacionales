# -*- coding: utf-8 -*-
"""
Tests unitarios para el patron Singleton - Decorador
Enfoque: Decorador Singleton para Gestor de Impresion
"""

import unittest
from src.singleton_decorator import singleton


@singleton
class TestLogger:
    """Clase de prueba: Logger Singleton"""
    def __init__(self):
        self.logs = []
    
    def log(self, message):
        self.logs.append(message)
        return message


@singleton
class TestCache:
    """Clase de prueba: Cache Singleton"""
    def __init__(self):
        self.data = {}
    
    def set(self, key, value):
        self.data[key] = value
    
    def get(self, key):
        return self.data.get(key)


class TestSingletonDecorator(unittest.TestCase):
    """Tests para implementacion con Decorador"""
    
    def test_1_logger_singleton_identity(self):
        """Verificar que Logger es singleton"""
        TestLogger._instances = {}
        logger1 = TestLogger()
        logger2 = TestLogger()
        
        self.assertIs(logger1, logger2, "Logger debe ser singleton")
    
    def test_2_cache_singleton_identity(self):
        """Verificar que Cache es singleton"""
        TestCache._instances = {}
        cache1 = TestCache()
        cache2 = TestCache()
        
        self.assertIs(cache1, cache2, "Cache debe ser singleton")
    
    def test_3_state_persistence(self):
        """Verificar que el estado persiste"""
        TestLogger._instances = {}
        logger1 = TestLogger()
        logger1.log("msg1")
        logger1.log("msg2")
        
        logger2 = TestLogger()
        
        self.assertEqual(len(logger2.logs), 2, "Estado debe persistir")
    
    def test_4_cache_persistence(self):
        """Verificar que el cache persiste"""
        TestCache._instances = {}
        cache1 = TestCache()
        cache1.set("clave", "valor")
        
        cache2 = TestCache()
        self.assertEqual(cache2.get("clave"), "valor", "Cache debe persistir")
    
    def test_5_different_classes_independent(self):
        """Verificar que clases diferentes son instancias independientes"""
        TestLogger._instances = {}
        TestCache._instances = {}
        logger = TestLogger()
        cache = TestCache()
        
        self.assertNotEqual(id(logger), id(cache), "Clases diferentes")
    
    def test_6_multiple_accesses_same_instance(self):
        """Verificar que multiples accesos devuelven la misma instancia"""
        TestLogger._instances = {}
        instances = [TestLogger() for _ in range(5)]
        
        for i in range(1, len(instances)):
            self.assertIs(instances[0], instances[i], "Deben ser identicas")


if __name__ == "__main__":
    unittest.main(verbosity=2)
