import json

class Contato:
    def __init__(self, primerio_nome, sobrenome):
        self.primerio_nome = primerio_nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return ('{} {}'.format(self.primerio_nome, self.sobrenome))



c = Contato('joao', 'pedro')
print(json.dumps(c.__dict__))
