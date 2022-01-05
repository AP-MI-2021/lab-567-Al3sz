from Domain.rezervare import getId, getnume, getclasa, getpret, getcheckin
from Logic.CRUD import adaugarezervare, getbyid, stergerezervare, modificarezervare


def testadaugarezervare():
    lista = []
    lista = adaugarezervare("1" , "Alex" , "economy" , 317.78 , "da", lista)
    assert len(lista) == 1
    assert getId(getbyid("1" , lista)) == "1"
    assert getnume(getbyid("1" , lista)) == "Alex"
    assert getclasa(getbyid("1" , lista)) == "economy"
    assert getpret(getbyid("1" , lista)) == 317.78
    assert getcheckin(getbyid("1" , lista)) == "da"

def teststergerezervare():
    lista = []
    lista = adaugarezervare("1", "Alex", "economy", 317.78, "da" , lista)
    lista = adaugarezervare("2", "Mircea", "business", 1118.90, "nu" , lista)
    lista = stergerezervare("1" , lista)
    assert len(lista) == 1
    assert getbyid("1" , lista) is None
    lista = adaugarezervare("3", "Mircea", "business", 1118.90, "nu", lista)
    lista = stergerezervare("3", lista)
    assert len(lista) == 1
    assert getbyid("2", lista) is not None

def testmodificarezervare():
    lista = []
    lista = adaugarezervare("1", "Alex", "economy", 317.78, "da", lista)
    lista = adaugarezervare("2", "Mircea", "business", 1119.90, "nu", lista)
    lista = adaugarezervare("3" , "Gabi" , "economy plus" , 890.02 ,"da", lista )
    lista = modificarezervare("2" , "George" , "economy" , 113.90 , "nu" , lista)
    assert len(lista) == 3
    assert getId(getbyid("2", lista)) == "2"
    assert getnume(getbyid("2", lista)) == "George"
    assert getclasa(getbyid("2", lista)) == "economy"
    assert getpret(getbyid("2", lista)) == 113.90
    assert getcheckin(getbyid("2", lista)) == "nu"

def testgetbyid():
    lista = []
    lista = adaugarezervare("1", "Alex", "economy", 317.78, "da", lista)
    lista = adaugarezervare("2", "Mircea", "business", 1119.90, "nu", lista)
    lista = adaugarezervare("3", "Gabi", "economy plus", 890.02, "da", lista)
    assert getbyid("1" , lista) == lista[0]
    assert getbyid("2" , lista) == lista[1]
    assert getbyid("3" , lista) == lista[2]