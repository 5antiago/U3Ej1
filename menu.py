from Libros import Libros

class Menu:
    __switcher = dict
    def __init__(self):
        self.__switcher = {1: self.libroid, 2: self.libropalabra}
    def opcion(self, op, libros):
        self.__switcher.get(op)(libros)
    def libroid(self, libros):
        lib = libros.buscalibroid(int(input("Ingrese id del libro: ")))
        print(" Titulo: {0:40} \n Nombre del Autor: {1:15}".format(lib.gettitulo(), lib.getautor()))
    def libropalabra(self, libros):
        palabra = input("Ingrese palabra a Buscar: ")
        print(" {0:40} \t {1:15}".format("Titulo", "Autor"))
        for lib in libros.buscalibropalabra(palabra):
            print("{0:20} \t {1:15}".format(lib.gettitulo(), lib.getautor()))


