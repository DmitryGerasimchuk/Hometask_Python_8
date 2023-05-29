# Функция для добавление контакта
def add_contact():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")

    contact = f"{name} {surname}: {phone}\n"

    with open("phon.txt", "a") as file:
        file.write(contact)

    print("Контакт успешно добавлен.")


# Функция для изменения контакта
def update_contact():
    name = input("Введите имя или фамилию контакта, который хотите изменить: ")
    new_phone = input("Введите новый номер телефона: ")

    with open("phon.txt", "r") as file:
        lines = file.readlines()

    found = False

    with open("phon.txt", "w") as file:
        for line in lines:
            if name.lower() in line.lower():
                file.write(f"{line.split(':')[0]}: {new_phone}\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Контакт успешно изменен.")
    else:
        print("Контакт не найден.")


# Функция для удаления контакта
def delete_contact():
    name = input("Введите имя или фамилию контакта, который хотите удалить: ")

    with open("phon.txt", "r") as file:
        lines = file.readlines()

    found = False

    with open("phon.txt", "w") as file:
        for line in lines:
            if name.lower() not in line.lower():
                file.write(line)
            else:
                found = True

    if found:
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")

# Функция для запуска меню, где можно выбрать команду, что сделать с контактом:
def main():
    while True:
        print("\nТелефонный справочник")
        print("1. Добавить контакт")
        print("2. Изменить контакт")
        print("3. Удалить контакт")
        print("4. Выйти")

        choice = input("Введите номер операции: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4": 
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()