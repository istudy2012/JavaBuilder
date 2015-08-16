import os;
from util import *

def complier() :
    javacCommand = "javac -sourcepath ./src/ %s -d .\\bin"
    for parent,dirnames,filenames in os.walk('./'):  
        for filename in filenames:
            if isJava(filename):
                inPath = os.path.join(parent,filename)
                try:
                    os.system(javacCommand % inPath)
                except Exception, e:
                    sys.exit()

def run() :
    output = os.popen('findstr /s /M /C:"public static void main" .\*.java')
    mainPath = output.read()
    mainClass = formatMain(mainPath)
    output = os.popen('findstr "package" %s' % mainPath)
    package = output.read();
    if len(package) != 0:
        mainClass = formatPackage(package) + '.' + mainClass
    os.system("java -classpath ./bin %s" % mainClass)

if __name__ == '__main__':
    complier()
    run()