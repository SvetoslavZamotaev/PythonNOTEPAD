def Command():
    res = input("         ->>>")
    return res 


def getInfoNewNote():
    arrInfo = []
    nameHeader = input("     Введите заголовок заметки: ")
    note = input("     Введите тело заметки: ")
    arrInfo.append(nameHeader)
    arrInfo.append(note)
    return arrInfo


def FindSubString():
    substr = input("     Введите фрагмент заголовка или его тела ")
    return substr


def CallForDelete():
    char = input()
    return char

def CallForEdit():
    res = []
    idNum = input("Введите id заметки для ее редактирования: ")
    header = input('Введите Название заметки: ')
    note = input('Введите тело заметки: ')
    res.append(idNum)
    res.append(header)
    res.append(note)
    return res

