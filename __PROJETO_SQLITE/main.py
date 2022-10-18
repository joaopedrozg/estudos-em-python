from database import BancoDeDados

if __name__ == '__main__':
    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()
    #banco.remover_cliente('09981849936')
    banco.buscar_cliente('09981849936')


    banco.desconecta()
