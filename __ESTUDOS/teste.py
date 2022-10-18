def algo():
    print('antes da chamada da funcao')
    algo2()
    print('depois da chamada da funcao')


def algo2():
    raise Exception('excecao em algo2')


algo()
