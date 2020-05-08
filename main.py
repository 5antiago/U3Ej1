import csv

from Libros import Libros
from manejalibro import ManejaLibros
from Capitulos import Capitulos
from menu import Menu

def Lector(libros):
    with open("libros.csv") as f:
        reader = csv.reader(f, delimiter=",")
        capitulo = False
        i = 0
        libroagregar = Libros
        for row in reader:
            if not capitulo:
                libroagregar = Libros(row[0], row[1], row[2],row[3],row[4], row[5])
                capitulo = True
                i = 1
            else:
                libroagregar.agregarcapi( Capitulos(row[0], row[1]) )
                i += 1
                if i > libroagregar.getcantcapitulos():
                    capitulo = False
                    libros.agregalibro(libroagregar)
                    libroagregar = Libros

if __name__ == "__main__":
    libros = ManejaLibros()
    Lector(libros)
    menu=Menu()
    print(" 1. Buscar libro por id \n 2. Buscar libro por palabra \n 0. Salir")
    op = int(input('Ingrese una opcion: '))
    while op > 0:
        menu.opcion(op, libros)
        print(" 1. Buscar libro por id \n 2. Buscar libro por palabra \n 0. Salir")
        op = int(input('Ingrese una opcion: '))
