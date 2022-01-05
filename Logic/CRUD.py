from Domain.rezervare import getId, creeazarezervare


def adaugarezervare( id , nume , clasa , pret , checkin, lista):
    '''
    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:
    :return:
    '''
    if getbyid(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    rezervare = creeazarezervare(id , nume , clasa , pret , checkin)
    return lista + [rezervare]

def adaugaRezervareUndoRedo(id,nume,clasa,pret,checkin,lista,undoList,redoList):
    '''
    Adauga o rezervare in lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista:
    :param undoList:
    :param redoList:
    :return: Retuneaza o lista continand elementele vechii cat si noua rezervare
    '''

    if getbyid(id,lista) is not None:
        raise ValueError("Id-ul exista deja!")
    rezervare=creeazarezervare(id,nume, clasa ,pret, checkin )
    undoList.append(lista)
    redoList.clear()
    return lista+[rezervare]

def getbyid(id , lista):
    '''

    :param id: id-ul rezervarii pe care o cautam
    :param lista: lista rezervarilor in care cautam rezervarea cu id ul dat
    :return: rezervarea cu id ul cautat
    '''
    for rezervare in lista:
        if getId(rezervare) == id :
            return rezervare
    return None

def stergerezervare(id , lista):
    '''
    sterge  o rezervare dupa id dintr o lista
    :param id: id-ul rezervarilor de sters, string
    :param lista: lista de rezervari
    :return: lista dupa stergerea rezervarii cu id ul dat
    '''
    if getbyid(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat!")
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificarezervare(id , nume , clasa , pret , checkin , lista):
    '''

    :param id: id-ul rezervarii care trebuie modificate
    :param nume: numele noii rezervari
    :param clasa: noua clasa
    :param pret: noul pret
    :param checkin: noul tip de checkin
    :param lista: lista de rezervari
    :return:  listaNoua care contine toate rezervarile dupa modificare
    '''
    if getbyid(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat!")
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervarenoua = creeazarezervare(id , nume , clasa , pret , checkin)
            listaNoua.append(rezervarenoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua



