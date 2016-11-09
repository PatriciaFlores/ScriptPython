from bottle import route, run, template

@route('/Hola/<name>')
def hola(name):
    return template('<b>Hola {{name}}</b>!', name=Michelle)
'''
@route('/')
def index(name):
    return template('<b>Hola mundo</b>!', name=name)
'''
run(host='localhost', port=9000)