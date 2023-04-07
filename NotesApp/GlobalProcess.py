import FileWorker
import Engine
import Output_term
import Input_term


def Starting():
    while (True):
        Output_term.MainMenu()
        res = Input_term.Command()
        if (res == '1'):
            FileWorker.PushToFile(Engine.Write(Input_term.getInfoNewNote()))
            Output_term.MessageToMenu("Запись успешно добавлена! =)")
        elif (res == '0'):
            Output_term.MessageToMenu("До свидания!")
            break
        elif (res == '2'):
            Output_term.PrintAll_db()
        elif (res == '3'):
            Output_term.PrintResults(Engine.FindNotes(Input_term.FindSubString()))
        elif (res == '4'):
            Output_term.MessageToMenu("----Введите id заметки для удаления-->")
            FileWorker.PushEditedBase(Engine.Delete(Input_term.CallForDelete()))
        elif (res == '5'):
            FileWorker.PushEditedBase(Engine.Edit(Input_term.CallForEdit()))
        else:
            print('Введите команду корректно!')      