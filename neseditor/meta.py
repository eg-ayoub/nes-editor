"""Meta classes."""

class SingletonMeta(type):
    """Singleton Metaclass."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Only call class when it hasn't been isntanciated"""
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


