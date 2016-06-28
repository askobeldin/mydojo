# -*- coding: utf-8 -*-
#
###################################################################
# Try to config Dojo
#
#
import os.path

from bottle import Bottle, run
from bottle import template, static_file


# html and static dirs
HTML, STATIC, APP = (os.path.abspath(os.path.join(os.path.dirname(__file__),
                             name).replace('\\', '/'))
                for name in ('html', 'static', 'app'))

############################################################
# Dojo paths
#
# Release dir
DR = os.path.abspath(os.path.join('..',
                                  os.path.dirname(__file__),
                                  'dojo-release-1.11.2'))
# dojo dir
DOJO = os.path.abspath(os.path.join(DR, 'dojo'))
# dijit dir
DIJIT = os.path.abspath(os.path.join(DR, 'dijit'))
# dojox dir
DOJOX = os.path.abspath(os.path.join(DR, 'dojox'))
# themes dir
THEMES = os.path.abspath(os.path.join(DR, 'themes'))




##########################################################
# Application
app = Bottle()

@app.route('/')
def simple_example():
    return static_file('index.html', HTML)

@app.route('/btn1')
def simple_btn1():
    return static_file('btn1.html', HTML)

@app.route('/app/<filename:path>')
def get_app(filename):
    return static_file(os.path.basename(filename),
                       os.path.abspath(os.path.join(APP,
                                                    os.path.dirname(filename))))


###########################################################
# /dojo/<path>
@app.route('/dojo/<filename:path>')
def get_dojo(filename):
    return static_file(os.path.basename(filename),
                       os.path.abspath(os.path.join(DOJO,
                                                    os.path.dirname(filename))))

# /dijit/<path>
@app.route('/dijit/<filename:path>')
def get_dijit(filename):
    return static_file(os.path.basename(filename),
                       os.path.abspath(os.path.join(DIJIT,
                                                    os.path.dirname(filename))))

# /dojox/<path>
@app.route('/dojox/<filename:path>')
def get_dojox(filename):
    return static_file(os.path.basename(filename),
                       os.path.abspath(os.path.join(DOJOX,
                                                    os.path.dirname(filename))))
# /themes/<path>
@app.route('/themes/<filename:path>')
def get_themes(filename):
    return static_file(os.path.basename(filename),
                       os.path.abspath(os.path.join(THEMES,
                                                    os.path.dirname(filename))))

# /static/<path>
@app.route('/static/<filename:path>')
def get_static_file(filename):
    return static_file(os.path.basename(filename),
                       os.path.abspath(os.path.join(STATIC,
                                                    os.path.dirname(filename))))
# favicon.ico
@app.route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', STATIC)

run(app, host='localhost', port=8080, debug=False)
