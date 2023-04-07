import csv



def PushToFile(string: list):
    with open("database.csv", mode="a+", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(string)


def ReadAllFile():
    with open("database.csv", encoding='utf-8') as r_file:
        F_reader = csv.reader(r_file, delimiter=";")
        listStr: list = [] 
        for row in F_reader:
            listStr.append(";".join(row))
        return listStr


def PushEditedBase(listDb: list):
    with open("database.csv", mode="w", encoding='utf-8') as w_file:
        for element in listDb:
            w_file.writelines(f'{element}\n')
        
        
         
