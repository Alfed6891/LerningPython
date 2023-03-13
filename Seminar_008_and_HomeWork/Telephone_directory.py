import json

def new_values (name):
        count_values = int(input(f"Введите количество новых значений {name}: "))
        values = {}
        for i in range (0, count_values):
                key = input(f"Введите вид {name}: ")
                value = input(f"Введите значение {name}: ")
                values.update({key: value})
        return values

def Print_DB (name_DB):
        fname = name_DB
        with open(fname, 'r', encoding='utf-8') as od:
                BD_local = json.load(od)
        for k,v in  BD_local.items():
                print (k,": ", end= "")
                for i,j in v.items():
                        print(i, end= ": ")
                        for a,b in j.items():
                                print (a,"-", b, end= "; ")                
                print()
        print('БД успещно загружена')

def delite_contact (name_DB):
        fname = name_DB
        with open(fname, encoding= "utf-8") as bd:
                 data = json.load(bd)
                 print(data.keys())
                 data.pop (input("Введите контакт который нужно удалить: "))
                 with open (fname, 'w', encoding='utf-8') as bd_out:
                        json.dump (data, bd_out, ensure_ascii= False, indent= 4)

def add_contact (name_DB):
        new_data = {input("Введите имя нового контакта: "):{"tel": new_values("tel"), "email": new_values("email")}}
        fname = name_DB
        with open(fname, encoding= "utf-8") as bd:
                 data = json.load(bd)
                 data.update(new_data)
                 with open (fname, 'w', encoding='utf-8') as bd_out:
                         json.dump (data, bd_out, ensure_ascii= False, indent= 4)

def change_value (name_DB):
        fname = name_DB
        with open(fname, encoding= "utf-8") as bd:
                data = json.load(bd)
                print(data.keys())
                dir = input("Введите контакт который требуется изменить: ")
                print(data[dir].keys())
                dir_2 = input("Введите категорию которую требуется изменить: ")
                print(data[dir][dir_2].keys())
                dir_3 = input("Введите подкатегорию которую требуется изменить: ")
                data[dir][dir_2][dir_3] = input("Введите новое значение: ")
                with open (fname, 'w', encoding='utf-8') as bd_out:
                        json.dump (data, bd_out, ensure_ascii= False, indent= 4)

                    

BD_telephone_directory = {"Иванов Иван Иваныч": {"tel": {"home": "84958873524", "job": "84991173547"}, "email": {"person": "ivan@gmail.com"}}, 
                         "Петров Петр Петрович": {"tel": {"mobile": "89854447889"}, "email": {"job": "pppasd.mail.ru"}}}



request = str(input("Вветите команду (1 - создать справочник, 2 - вывести справочник, 3 - добавить контакт, 4 - удалить контакт, 5 - изменить данные контакта): "))
if request == "1":
        with open("BD_telephone_directory.json",'w', encoding= 'utf-8') as bd:
                bd.write(json.dumps(BD_telephone_directory,
                                    ensure_ascii=False))
        print ("Телефонный справочник успешно записан")
if request == "2":
        Print_DB ('BD_telephone_directory.json')
if request == "3": 
        add_contact ('BD_telephone_directory.json')
if request == "4":
        delite_contact('BD_telephone_directory.json')
if request == 5:
        change_value("BD_telephone_directory.json")