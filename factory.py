# from abc import ABCMeta, abstractmethod


class Cachorro:
    def som(self):
        print('Au au au')


class Gato:
    def som(self):
        print('Miau miau')


class Fabrica(object):
    def produzir_som(self, object_type):
        return eval(object_type)().som()


if __name__ == '__main__':
    f = Fabrica()
    f.produzir_som('Gato')
