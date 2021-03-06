# -*- coding: utf-8 -*-
#
###################################################################
# Try to work with dom functions
#
#
import os.path
import types

from bottle import Bottle, run
from bottle import template, static_file



def mkabspath(*chunks):
    items = list(chunks)
    return os.path.abspath(os.path.join(*items))

def mkstaticfilepath(root, path):
    return (os.path.basename(path),
            os.path.abspath(os.path.join(root, os.path.dirname(path))))

def getstaticfile(root, path):
    return static_file(*mkstaticfilepath(root, path))

def printinfo(ns):
    for k in vars(ns):
        print('{:<10}{}'.format(k, getattr(ns, k)))


pathways = types.SimpleNamespace()

CURDIR = os.path.dirname(__file__)

# html folder
pathways.html = mkabspath(CURDIR, 'html')
# static folder
pathways.static = mkabspath(CURDIR, 'static')
# app folder
pathways.app = mkabspath(CURDIR, 'app')


# Dojo release directory
pathways.dr = mkabspath('..', CURDIR, 'dojo-release-1.11.2')
# dojo directory
pathways.dojo = mkabspath(pathways.dr, 'dojo')
# dijit directory
pathways.dijit = mkabspath(pathways.dr, 'dijit')
# dojox directory
pathways.dojox = mkabspath(pathways.dr, 'dojox')
# Dojo themes directory
pathways.themes = mkabspath(pathways.dr, 'themes')


##########################################################
# Application
app = Bottle()

@app.route('/')
def dom1():
    return static_file('dom1.html', pathways.html)

@app.route('/place')
def place():
    return static_file('place.html', pathways.html)

@app.route('/destroy')
def destroy():
    return static_file('destroy.html', pathways.html)


# routing for `app` folder for Dojo application
@app.route('/app/<filename:path>')
def get_app(filename):
    return getstaticfile(pathways.app, filename)


###########################################################
# /dojo/<path>
@app.route('/dojo/<filename:path>')
def get_dojo(filename):
    return getstaticfile(pathways.dojo, filename)

# /dijit/<path>
@app.route('/dijit/<filename:path>')
def get_dijit(filename):
    return getstaticfile(pathways.dijit, filename)

# /dojox/<path>
@app.route('/dojox/<filename:path>')
def get_dojox(filename):
    return getstaticfile(pathways.dojox, filename)

# /themes/<path>
@app.route('/themes/<filename:path>')
def get_themes(filename):
    return getstaticfile(pathways.themes, filename)

# /static/<path>
@app.route('/static/<filename:path>')
def get_static_file(filename):
    return getstaticfile(pathways.static, filename)

# favicon.ico
@app.route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', pathways.static)

run(app, host='localhost', port=8080, debug=False)
