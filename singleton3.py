class MinhaClasse:
    __estado_compartilhado = {'1': 2}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__estado_compartilhado


b1 = MinhaClasse()
b2 = MinhaClasse()
b1.x = 5

print('b1: ', b1)
print('b2: ', b2)

print(b1.__dict__)
print(b2.__dict__)
