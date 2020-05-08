from Capitulos import Capitulos

class Libros:
    __idlibro   = int
    __titulo    = str
    __autor     = str
    __editorial = str
    __isnb      = str
    __cantcapi  = int
    __capitulos = list

    def __init__(self, id, titulo, autor, editorial, isnb, cantidadcapi):
        self.__idlibro = id
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__isnb     = isnb
        self.__cantcapi = cantidadcapi
        self.__capitulos = []
    def getid(self):
        return int(self.__idlibro)
    def  gettitulo (self):
        return str(self.__titulo)
    def getautor(self):
        return str(self.__autor)
    def geteditorial(self):
        return str(self.__editorial)
    def getisnb(self):
        return int(self.__isnb)
    def getcantcapitulos(self):
        return int(self.__cantcapi)
    def agregarcapi(self, capitulo):
        if type(capitulo) == Capitulos:
            self.__capitulos.append(capitulo)
    def getcapitulo(self, num):
        return self.__capitulos[num]
