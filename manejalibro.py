from Libros import Libros

class ManejaLibros:
    __libros = list

    def __init__(self):
        self.__libros = []
    
    def agregalibro(self, libro):
        if type(libro) == Libros:
            self.__libros.append(libro)
    def buscalibroid(self, id):
        i = 0
        while i < len(self.__libros) and self.__libros[i].getid() != id:
            i += 1
        if i == len(self.__libros):
            aux = -1
        else:
            aux = self.__libros[i]
        
        return aux
    def buscalibropalabra(self, palabra):
        lista = []
        for libro in self.__libros:
            if palabra in libro.gettitulo():
                lista.append(libro)
            else:
                for i in range(libro.getcantcapitulos()):
                    if palabra in libro.getcapitulo(i).gettitulo():
                        lista.append(libro)
        return lista