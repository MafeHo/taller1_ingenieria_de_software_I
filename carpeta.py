from archivo import Archivo
import os

class Carpeta():
    def __init__(self, ruta):
        self.nombreArchivos = []
        self.ruta = ruta
        self.totalPalabras = 0

    def buscarArchivos(self, palabra):

        if os.path.isdir(self.ruta): 
            with os.scandir(self.ruta) as ficheros:
                for fichero in ficheros:
                    archivo = Archivo(fichero.name, self.ruta)
                    self.nombreArchivos.append(archivo)

            self.buscarEnArchivos(palabra)
            
            if self.totalPalabras != 0:
                self.mostrarTotalPalabras()
                    
        else:
            print("No se encontró la carpeta")
            

    def buscarEnArchivos(self, palabra):
        self.totalPalabras = 0
        for archivo in self.nombreArchivos:
            archivo.contarPalabras(palabra)
            self.totalPalabras += archivo.numeroPalabras

        if self.totalPalabras == 0:
            print(f"La palabra buscada no aparece en los archivos de la carpeta.")

    def mostrarTotalPalabras(self):
        print(f"La palabra buscada aparece {self.totalPalabras} veces en los archivos de la carpeta.")