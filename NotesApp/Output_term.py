import FileWorker


def MessageToMenu(message):
    print(message)


def MainMenu():
    print('===================================================')
    print('-------------------Greetings !!--------------------')
    print('     Введите 0 если хотите хотите остановить приложение.')
    print('     Введите 1 если хотите создать заметку.')
    print('     Введите 2 если хотите хотите показать все заметки.')
    print('     Введите 3 если хотите найти записи заметок по поиску.')
    print('     Введите 4 если хотите удалить запись по id.')
    print('     Введите 5 если хотите редактировать заметку.')


def PrintAll_db():
    copylist = FileWorker.ReadAllFile()
    for element in copylist:
        print(f'{element}\n') 


def PrintResults(arr: list):
    if len(arr) == 0:
        print("----------result----------------------------")
        print("-----it's empty, sorry!---------------------")
        print("----------result----------------------------") 
    else:
        print("--------------result---------------------")
        for element in arr:
            print(f'{element}' '\n')
        print("--------------result--------------------")




