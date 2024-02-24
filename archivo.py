from extension import Extension
import xml.etree.ElementTree as ET
import json
import csv
import os
import re

class Archivo():
    def __init__(self, nombre, ruta):
        self.nombre = nombre
        self.ruta = ruta + '/' + nombre
        self.archivo = open(ruta + '/' + nombre, 'r')
        self.numeroPalabras = 0
        self.extension = self.obtenerExtension(nombre)

    def contarPalabras(self, palabra):
        self.numeroPalabras = 0

        if self.extension == Extension.TXT.value:
            content = self.archivo.read()
            self.numeroPalabras = len(re.findall(r'\b{}\b'.format(palabra), content))

        elif self.extension == Extension.XML.value:
            tree = ET.parse(self.ruta)
            content = ET.tostring(tree.getroot(), encoding='utf8').decode('utf8')
            self.numeroPalabras = len(re.findall(r'\b{}\b'.format(palabra), content))

        elif self.extension == Extension.JSON.value:
            data = json.load(self.archivo)
            content = json.dumps(data)
            self.numeroPalabras = len(re.findall(r'\b{}\b'.format(palabra), content))

        elif self.extension == Extension.CSV.value:
            reader = csv.reader(self.archivo)
            for row in reader:
                self.numeroPalabras += len(re.findall(r'\b{}\b'.format(word), ' '.join(row)))

        else :
            print("No se puede contar palabras de archivos con extensión", self.extension)
            return

        print(f"La palabra buscada aparece {self.numeroPalabras} veces en el archivo {self.nombre}")

    def obtenerExtension(self, nombre):
        extension = os.path.splitext(nombre)[1]
        return extension  