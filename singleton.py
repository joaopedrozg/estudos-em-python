"""
Padrão de projeto Singleton
"""


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)

        return cls.instance


s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)
