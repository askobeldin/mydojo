# -*- coding: utf-8 -*-
#
################################################################################
from bottle import Bottle, run
from bottle import template

app = Bottle()

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

# @app.route('/hello')
# def hello():
    # return "Hello World!"

run(app, host='localhost', port=8080, debug=False)
