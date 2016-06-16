# -*- coding: utf-8 -*-
#
###################################################################
import os.path

from bottle import Bottle, run
from bottle import template, static_file


# html and static dirs
HTML, STATIC = (os.path.abspath(os.path.join(os.path.dirname(__file__),
                             name).replace('\\', '/'))
                for name in ('html', 'static'))

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
THEMES = os.path.abspath(os.path.join(DR, 'dojox'))




##########################################################
# Application
app = Bottle()

@app.route('/')
@app.route('/hd1')
def hello_dojo_1():
    return static_file('hellodojo1.html', HTML)

# /dojo/<path>
@app.route('/dojo/<filename:path>')
def get_dojo(filename):
    # print('filename is {}'.format(filename))
    # print(os.path.abspath(os.path.join(DOJO, os.path.dirname(filename))))
    return static_file(os.path.basename(filename),
                       os.path.abspath(os.path.join(DOJO,
                                                    os.path.dirname(filename))))

# favicon.ico
@app.route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', STATIC)

run(app, host='localhost', port=8080, debug=False)
