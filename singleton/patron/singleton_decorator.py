"""
Implementación del patrón Singleton usando Decorador
"""

from functools import wraps
from threading import Lock


def singleton(cls):
    """
    Decorador que convierte una clase en Singleton.
     Asegura que solo exista una instancia de la clase."""
    instances = {}
    lock = Lock()
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton
class Logger:
    """
    Ejemplo: Logger singleton.
    Toda la aplicación debe usar el mismo logger.
    """
    
    def __init__(self, log_file: str = "app.log"):
        self.log_file = log_file
        self.logs = []
    
    def info(self, message: str):
        """Registra un mensaje informativo"""
        log_entry = f"[INFO] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def warning(self, message: str):
        """Registra una advertencia"""
        log_entry = f"[WARNING] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def error(self, message: str):
        """Registra un error"""
        log_entry = f"[ERROR] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self):
        """Retorna todos los logs registrados"""
        return self.logs.copy()


@singleton
class CacheManager:
    """
    Ejemplo: Gestor de cache singleton.
    Proporciona un único punto de acceso al cache de la aplicación.
    """
    
    def __init__(self):
        self._cache = {}
    
    def set(self, key: str, value):
        """Almacena un valor en el cache"""
        self._cache[key] = value
        print(f"Cache establecido: {key}")
    
    def get(self, key: str, default=None):
        """Obtiene un valor del cache"""
        return self._cache.get(key, default)
    
    def clear(self):
        """Limpia todo el cache"""
        self._cache.clear()
        print("Cache limpiado")
    
    def size(self):
        """Retorna el número de elementos en el cache"""
        return len(self._cache)
