class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        
        
    @classmethod
    def outro_construtor(cls, nome):
        return cls(nome)
    
"""
p = Pessoa('Joao')
print(p.nome)
"""

p = Pessoa.outro_construtor('Joao')
print(p.nome)