from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):
    @abstractmethod
    def descricao(self):
        pass


class SecaoPessoal(Secao):
    def descricao(self):
        print('seção pessoal')


class SecaoAlbum(Secao):
    def descricao(self):
        print('seção de fotos')


class SecaoPatente(Secao):
    def descricao(self):
        print('seção de patentes')


class SecaoPublicacao(Secao):
    def descricao(self):
        print('seção de publicação')


class Perfil(metaclass=ABCMeta):
    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def obter_secoes(self):
        return self.secoes

    def add_secoes(self, secao):
        self.secoes.append(secao)


class Facebook(Perfil):
    def criar_perfil(self):
        self.add_secoes(SecaoPessoal())
        self.add_secoes(SecaoPatente())
        self.add_secoes(SecaoPublicacao())


class Twitter(Perfil):
    def criar_perfil(self):
        self.add_secoes(SecaoPessoal())
        self.add_secoes(SecaoAlbum())


if __name__ == '__main__':
    tipo_perfil = 'Twitter'
    perfil = eval(tipo_perfil)()
    print(perfil.obter_secoes)
