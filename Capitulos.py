class Capitulos:
    __titulo = str
    __paginas = int

    def __init__(self, tit, pags):
        self.__titulo = tit
        self.__paginas = pags

    def gettitulo(self):
        return str(self.__titulo)
    def getpaginas(self):
        return int(self.__paginas)