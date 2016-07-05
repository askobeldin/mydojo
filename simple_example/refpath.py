# -*- coding: utf-8 -*-
#
################################################################################
import os.path
import types


pathways = types.SimpleNamespace()

CURDIR = os.path.dirname(__file__)

def mkabspath(*chunks):
    items = list(chunks)
    return os.path.abspath(os.path.join(*items))

def mkstaticfilepath(root, path):
    return (os.path.basename(path),
            os.path.abspath(os.path.join(root, os.path.dirname(path))))

def printinfo(ns):
    for k in vars(ns):
        print('{:<10}{}'.format(k, getattr(ns, k)))


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

printinfo(pathways)

print('filepath for app')
print(mkstaticfilepath(pathways.app, 'logger.js'))

