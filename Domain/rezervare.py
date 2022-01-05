def creeazarezervare(id , nume , clasa , pret , checkin):
    '''
    creeaza o rezervare
    :param ID: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: un dictionar ce retine o rezervare
    '''
    return {
        'id' : id,
        'nume' : nume,
        'clasa' : clasa,
        'pret' : pret,
        'checkin' : checkin
    }

def getId(rezervare):
    '''
    ia id-ul rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: id-ul prajiturii
    '''
    return rezervare['id']

def getnume(rezervare):
    '''
    ia numele din rezervare
    :param rezervare: dictionar de tipul rezervare
    :return: numele din rezervare
    '''
    return rezervare['nume']

def getclasa(rezervare):
    '''
    ia clasa rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: clasa rezervarii
    '''
    return rezervare['clasa']

def getpret(rezervare):
    '''
    ia pretul din rezervare
    :param rezervare: dictionar de tipul rezervare
    :return: pretul din rezervare
    '''
    return rezervare['pret']

def getcheckin(rezervare):
    '''
    ia checkin ul rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: checkin ul rezervarii
    '''
    return rezervare['checkin']

def toString(rezervare):
    return 'id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}'.format(
        getId(rezervare) ,
        getnume(rezervare) ,
        getclasa(rezervare) ,
        getpret(rezervare) ,
        getcheckin(rezervare)
    )