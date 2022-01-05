from Domain.rezervare import toString
from Logic.CRUD import adaugarezervare, stergerezervare, modificarezervare


def printDescriere():
    print("Lista de comenzi va fi separată prin ; ")
    print("Comenzile pot fi: add, showall, delete, update,exit ")
    print("Parametri dintr-o comandă vor fi separați prin ,")


def uiadaugarezervare(id, nume, clasa, pret, checkin, lista):
    try:
        return adaugarezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uistergerezervare(id, lista):
    try:
        return stergerezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uishowall(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uimodificare(id, nume, clasa, pret, checkin, lista):
    try:
        return modificarezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def command_line_console(lista):
    print(printDescriere())
    lista = []
    listainput = []
    shouldrun = True
    while shouldrun:
        listainput = input("Dați lista de comenzi: ")
        listacomenzi = []
        listacomenzi = listainput.split(",")
        i = 1
        for i in range(len(listacomenzi)):
            if listacomenzi[i] == "update":
                lista = uimodificare(listacomenzi[i+1], listacomenzi[i+2], listacomenzi[i+3], float(listacomenzi[i+4]), listacomenzi[i+5], lista)
            if listacomenzi[i] == "add":
                lista = uiadaugarezervare(listacomenzi[i+1], listacomenzi[i+2], listacomenzi[i+3], float(listacomenzi[i+4]), listacomenzi[i+5], lista)
                i = i + 6
            elif listacomenzi[i] == "delete":
                lista = uistergerezervare(listacomenzi[i+1], lista)
                i = i + 2
            elif listacomenzi[i] == "showall":
                uishowall(lista)
                i = i + 1
            elif listacomenzi[i] == "exit":
                shouldrun = False
                break

