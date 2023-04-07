import TimeNow
import FileWorker


def Write(list: list):
    list.insert(0, str(MakeId()))
    list.append(TimeNow.GetTimeNow())
    return list


def MakeId():
    copylist = FileWorker.ReadAllFile()
    nums = []
    element: str
    for element in copylist:
        nums.append(GetId(element))
    if len(nums) == 0:
        return 1
    return str(max(nums)+1)

    

def FindNotes(substring: str):
        arr = FileWorker.ReadAllFile()
        result = []
        element: str
        for element in arr:
            if element.find(substring) != -1:
                result.append(element)
        return result        


def Delete(id: str):
    arrList = FileWorker.ReadAllFile()
    removing: str
    element: str
    for element in arrList:
        if GetId(element) == int(id):
            removing = element
    arrList.remove(removing)
    return arrList


def GetId(stri: str):
    index = stri.find(";")
    result = stri[0:index]
    return int(result)



def Edit(info: list):
    arr = FileWorker.ReadAllFile()
    element: str 
    i = 0
    edited = info[0]+";"+info[1]+";"+info[2]+";"+" edited: "+ TimeNow.GetTimeNow()
    for element in arr:
        if GetId(element) == int(info[0]):
            i = arr.index(element)
    arr[i] = edited       
    return arr   
    



