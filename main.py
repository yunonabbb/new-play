import os
def show_menu(menu_items, selected_index):
    os.system('cls' if os.name == 'nt' else 'clear')

    for index, item in enumerate(menu_items):
        if index == selected_index:
            print("->", item)
        else:
            print("  ", item)

def main_menu():
    menu_items = ["Новая игра", "Загрузить игру", "Настройки", "Выход"]
    selected_index = 0

    while True:
        show_menu(menu_items, selected_index)
        key = input()

        if key == "w" and selected_index > 0:
            selected_index -= 1
        elif key == "s" and selected_index < len(menu_items) - 1:
            selected_index += 1
        elif key == "Enter":
            if selected_index == 0:
                print("Начало новой игры...")
            elif selected_index == 1:
                print("Загрузка игры...")
            elif selected_index == 2:
                print("Настройки...")
            elif selected_index == 3:
                print("Выход из игры...")
                break

main_menu()





