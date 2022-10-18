from bottle import route, run, request, template, static_file, get

"""
@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
    return f'<h1>Hello world {nome}</h1>'

"""
# statics routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')


@route('/login')
def login():
    return template('login')


def check_login(username, password):
    d = {'marcos':'python', 'joao':'java', 'pedro':'go'}
    if username in d.keys() and d[username] == password:
        return True
    return False

@route('/login', method='POST')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login',sucesso=check_login(username, password))







if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
