from bottle import route, run, request

"""
@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
    return f'<h1>Hello world {nome}</h1>'

"""

@route('/login')
def login():
    return """
        <form action='/login' method='post'>
            username: <input name='username' type='text' />
            password: <input name='password' type='password' />
            <input value='Login' type='submit' />

        </form>


    """


@route('/login', method='POST')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == 'joao' and password == 'joao':
        return '<h1>Validaddo </h1>'



if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
