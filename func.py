from os import path
import datetime
import mysql.connector ## бд коннектор
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='human_friends') ## подключаемся
cursor = cnx.cursor()

def show_all():
    """Вывод всех животных"""
    print(f'Вывод всех животных\n id: кличка | дата рождения| вид')
    try:
        query = ("SELECT a.id, a.name, a.birthdate, va.name_v FROM animals a join various_animals va ON a.various_animals=va.id_v") 
        cursor.execute(query)
        for (id, name, birthdate, various_animals) in cursor:
            print(f"{id}: {name}, {birthdate}, {various_animals}")

    except:
        cnx.rollback()
    ##cursor.close()
    ##cnx.close()  

def show_all_date():
    """Вывод всех животных по возрасту"""
    print(f'Вывод всех животных\n id: кличка | дата рождения| вид')
    try:
        query = ("SELECT a.id, a.name, a.birthdate, va.name_v FROM animals a join various_animals va ON a.various_animals=va.id_v order by a.birthdate") 
        cursor.execute(query)
        for (id, name, birthdate, various_animals) in cursor:
            print(f"{id}: {name}, {birthdate}, {various_animals}")
    except:
        cnx.rollback()
    ##cursor.close()
    ##cnx.close()

def search():
    try:
        search_name = input("Введите кличку животного: ") 
        query = "SELECT id, name, birthdate FROM animals WHERE name=%s"
        val = (search_name,) 
        cursor.execute(query, val)
        ## result = cursor.fetchone()
        for (id, name, birthdate) in cursor:
            print(f"id:{id}, {name}, {birthdate}")
            print("исполняемые команды:")
            query = "SELECT ac.id_com, c.command FROM animal_comm ac join commands c ON ac.id_com=c.id WHERE ac.id_animal=%s"
            val = (id,)
            cursor.execute(query, val)
            for (id,command)in cursor:
                print(f"{id} - {command}")
    except:
        cnx.rollback()
def to_teach():
    try:
        search_name = input("Введите кличку животного: ") 
        query = "SELECT id, name FROM animals WHERE name=%s"
        val = (search_name,) 
        cursor.execute(query, val)
        for row in cursor:
            id_animal = int(row[0])
        query = "SELECT id, command FROM commands"
        cursor.execute(query)
        for (id, command) in cursor:
            print(f"Id: {id} - {command}", end='  ')
        print("")    
        new_command = int(input("Введите Id новой команды: "))
        query = "SELECT count(*) FROM commands"
        cursor.execute(query)
        result = cursor.fetchone()
        max = int(result[0])
        if new_command > max:
            print(f"нет такой команды в списке")
        if new_command < 1:
            print(f"нет такой команды в списке")
        query = "SELECT * FROM animal_comm WHERE id_com=%s AND id_animal=%s"
        val = (new_command, id_animal)
        cursor.execute(query, val)
        if cursor.fetchone():
            print("Животное уже знает данную команду")
        else:
            try:
                cursor.execute("INSERT INTO animal_comm (id_com, id_animal) VALUES (%s, %s)", (new_command, id_animal))
                print("команда добавлена")
            except:
                cnx.rollback()
    except:
        cnx.rollback()
def add_animal():
    try:
        print("Какое животное добавляем")
        query = "SELECT * FROM type_animal"
        cursor.execute(query)
        print("тип животного:")
        for (id_t, name_t) in cursor:
            print(f"Id: {id_t} - {name_t}")
        new_id_t = int(input("Введите Id Типа животного: "))
        if(new_id_t > 2 or new_id_t < 1):
            print("у нас пока 2 типа животных")
        query = "SELECT id_v, name_v FROM various_animals WHERE id_t=%s"
        val = (new_id_t,)
        cursor.execute(query, val)
        print("вид животного:")
        for (id_v, name_v) in cursor:
            print(f"Id: {id_v} - {name_v}")
        new_id_v = int(input("Введите Id вид животного: "))
        new_name = input("Введите кличку животного: ")
        if(len(new_name)) > 45:
            print("слишком длинная кличка")
        if(len(new_name)) < 3:
            print("слишком длинная кличка")
        new_date_y = int(input("Введите год рождения животного: "))
        if(new_date_y > 2024 or new_date_y < 1900):
            print("Не корректный год от 1900 до 2023")
        new_date_m = int(input("Введите месяц рождения животного: "))
        if(new_date_m > 12 or new_date_m < 1):
            print("Не корректный мес от 1 до 12")
        new_date_d = int(input("Введите день рождения животного: "))
        if(new_date_d > 31 or new_date_d < 1):
            print("Не корректный день от 1 до 31")
        new_date = str(new_date_y)+"-"+str(new_date_m)+"-"+str(new_date_d)
        cursor.execute("INSERT INTO animals (name, birthdate, various_animals) VALUES (%s, %s, %s)", (new_name, new_date, new_id_v))
        print("Животное добавлено, може обучить его через обучить животное")
    except:
        cnx.rollback()
def rand_animal():
    import random
    from dog import Dog, Cat, Hamster, Horse, Camel, Donkey

    query = "SELECT count(*) FROM animals"
    cursor.execute(query)
    result = cursor.fetchone()
    max = int(result[0])
    rand_a = random.randint(1, max)
    query = "SELECT id, name, birthdate, various_animals FROM animals WHERE id=%s"
    val = (rand_a,)
    cursor.execute(query, val)
    for (id, name, birthdate, various_animals) in cursor:
        if various_animals == 1:
            animals_r = Cat(name, birthdate)
        if various_animals == 2:
            animals_r = Dog(name, birthdate)  
        if various_animals == 3:
            animals_r = Hamster(name, birthdate)
        if various_animals == 4:
            animals_r = Horse(name, birthdate)
        if various_animals == 5:
            animals_r = Camel(name, birthdate)  
        if various_animals == 6:
            animals_r = Donkey(name, birthdate) 
    animals_r.animal_info()
    animals_r.comand()
    check = input("показать сородичей? (Y/N) ")
    if check == "Y":
        query = "SELECT id, name, birthdate FROM animals WHERE various_animals=%s"
        val = (animals_r.id_v,)
        cursor.execute(query, val)
        for (id, name, birthdate) in cursor:
            print(f"{id}: {name}, {birthdate}")