
import func

def main_menu():
    play = True
    while play:
        
        answer = input("Меню:\n"
                       "1. Показать все животных\n"
                       "2. Добавить животное\n"
                       "3. Обучить животное\n"
                       "4. Отсортировать по дате рождения\n"
                       "5. Найти\n"
                       "6. Exit\n")
        match answer:
            case "1":
                func.show_all()
            case "2":
                play = False
            case "3":
                play = False           
            case "4":
                func.show_all_date()
            case "5":
                func.search()
            case "6":
                play = False
            case _:
                print("Не известная команда, повторите ввод \n")

main_menu()