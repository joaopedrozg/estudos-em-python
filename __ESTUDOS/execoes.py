def algo():
    raise Exception('excecao')


try:
    algo()

except:
    print('eu peguei uma excecao')
    print('executando apos a excecao')
