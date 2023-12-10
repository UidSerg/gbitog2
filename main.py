
import func

def main_menu():
    play = True
    while play:
        
        answer = input("Меню:\n"
                       "1. Показать все животных\n"
                       "2. Добавить животное\n"
                       "3. Обучить животное\n"
                       "4. Отсортировать по дате рождения\n"
                       "5. Узнать команды животного\n"
                       "6. показать случайное животное\n"
                       "7. Exit\n")
        match answer:
            case "1":
                func.show_all()
            case "2":
                func.add_animal()
            case "3":
                func.to_teach()        
            case "4":
                func.show_all_date()
            case "5":
                func.search()
            case "6":
                func.rand_animal()
            case "7":
                play = False    
            case _:
                print("Не известная команда, повторите ввод \n")

main_menu()