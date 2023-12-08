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