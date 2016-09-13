# -*- coding: utf-8 -*-
#
################################################################################
import os.path
import types


pathways = types.SimpleNamespace()

# CURDIR = os.path.dirname(__file__)
pathways.curdir = os.path.abspath(os.path.dirname(__file__))

def mkabspath(*chunks):
    items = list(chunks)
    return os.path.abspath(os.path.join(*items))

def mkstaticfilepath(root, path):
    return (os.path.basename(path),
            os.path.abspath(os.path.join(root, os.path.dirname(path))))

def printinfo(ns):
    for k in vars(ns):
        print('{:<12}{}'.format(k, getattr(ns, k)))

def printinfo2(ns, lst):
    for k in lst:
        print('{:<12}{}'.format(k, getattr(ns, k)))


# html folder
pathways.html = mkabspath(pathways.curdir, 'html')
# static folder
pathways.static = mkabspath(pathways.curdir, 'static')
# app folder
pathways.app = mkabspath(pathways.curdir, 'app')


# Dojo release directory
# pathways.dr = mkabspath('..', CURDIR, 'dojo-release-1.11.2')
pathways.dr = mkabspath(pathways.curdir, '..', 'dojo-release-1.11.2')
# dojo directory
pathways.dojo = mkabspath(pathways.dr, 'dojo')
# dijit directory
pathways.dijit = mkabspath(pathways.dr, 'dijit')
# dojox directory
pathways.dojox = mkabspath(pathways.dr, 'dojox')
# Dojo themes directory
pathways.themes = mkabspath(pathways.dr, 'themes')

names = ('curdir',
         'dr', 'dojo', 'dijit', 'dojox', 'themes',
         'app', 'html', 'static')

# printinfo(pathways)
printinfo2(pathways, names)

msg = '\nAsk file {0[0]!r} in {0[1]}.'
print(msg.format(mkstaticfilepath(pathways.app, 'logger.js')))
