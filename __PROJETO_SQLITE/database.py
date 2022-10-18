import sqlite3

class BancoDeDados:
    """Classe que representa o banco de dados da aplicação """

    def __init__(self, nome='banco.db'):
        self.nome = nome
        self.conexao = nome, None

    def conecta(self):
        """ Conecta passando o nome do arquivo """

        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """ Desconecta do Banco """

        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criar_tabelas(self):
        """ Cria as tabelas do banco """
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                email TEXT NOT NULL
            )
            """)
        except AttributeError:
            print("Faça a conexao antes de criar tabelas")


    def inserir_clientes(self, nome, cpf, email):
        """ Insere clientes no banco """

        try:
            cursor = self.conexao.cursor()
            try:
                cursor.execute("""
                    INSERT INTO clientes (nome, cpf, email) values (?,?,?)""", (nome, cpf, email)
                    )
            except sqlite3.IntegrityError:
                print(f'O cpf {cpf} ja existe')
            self.conexao.commit()

        except AttributeError:
            print('Faça a conexão antes de inserir clientes')



    def buscar_cliente(self, cpf):
        """ Busca um cliente pelo cpf"""

        try:
            cursor = self.conexao.cursor()
            cursor.execute("""SELECT * FROM clientes;""")
            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print(f'Clinte {linha[1]} encontrado')
                    break

        except AttributeError:
            print("Faça a conexão antes de buscar um cliente")



    def remover_cliente(self, cpf):
        """ Remove um clinte pelo cpf """
        try:
            cursor = self.conexao.cursor()
            cursor.execute(f"""DELETE FROM clientes WHERE cpf={cpf};""")


        except AttributeError:
            print("Faça a conexão antes de remover um cliente")

        self.conexao.commit()
