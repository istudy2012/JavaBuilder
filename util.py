import os

def isJava(filename) :
    l = filename.split('.')
    if l[-1] == 'java':
        return True
    else:
        return False

def rePath(basepath, subpath) :
	return subpath[len(basepath)+1: ]

def makeDir(dirpath) :
	if os.path.isdir(dirpath) == False:
		os.mkdir(dirpath)

def formatMain(path) :
	#path is like '.\src\Main.java'
	return path.split('\\')[-1].split('.')[0]

def formatPackage(package) :
	#package is like 'package main;'
	return package.split()[1].split(';')[0]