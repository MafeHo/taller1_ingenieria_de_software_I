from carpeta import Carpeta

if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")

    carpeta1 = Carpeta(carpeta)
    carpeta1.buscarArchivos(palabra)

    # for archivo in carpeta1.nombreArchivos:
    #     print(archivo.nombre)
    #     print(archivo.extension)
    #     print(archivo.archivo)

