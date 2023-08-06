# "Volodymyr": "0630000102", "Vika": "0976000504" 
ADDRESSBOOK = {}


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me name and phone please\nДайте ім'я та телефон, будь ласка"

    return wrap


@input_error
def handler_add(data):  # Функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved. (Збережено)"


# "hello", відповідає у консоль "How can I help you?"
def handler_hello(*args):
    return "How can I help you? \nЧим я можу вам допомогти?"


# "change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту.
# Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
def handler_change(data):
    for name in ADDRESSBOOK:
        if data[0].title() == name:
            ADDRESSBOOK[name] = data[1]
            return f"У контакта {name} замінено номер телефона на {data[1]}"


# "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту.
# Замість ... користувач вводить ім'я контакту, чий номер потрібно показати.
def handler_phone(data):
    for name, phone in ADDRESSBOOK.items():
        if data[0] == phone:
            print(f"Ім'я власника {name}")


# "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
def handler_show_all(*args):
    for name, phone in ADDRESSBOOK.items():
        print(f"{name}, tel: {phone")


# "good bye", "close", "exit" за будь-якою з цих команд бот завершує свою роботу після того,
# як виведе у консоль "Good bye!".
def handler_exit(*args):
    return "Good bye!\nДо побачення!"


@input_error
def command_parser(raw_str: str):  # Парсер команд
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key(elements[1:])
    return "Unknown command"


COMMANDS = {
    handler_hello: ["hello", "!", "привіт", "хай"],
    handler_add: ["add", "додай", "+"],
    handler_change: ["change", "ch", "зміни"],
    handler_phone: ["phone", "ph", "телефон"],
    handler_show_all: ["show all", "print", "p", "показати все", "покажи все", "все"],
    handler_exit: ["good bye", "x", "close", "exit", "бувай"],
}


def main():  # Цикл запит-відповідь.
    while True:
        # print("Ведіть будь ласка команду")
        user_input = input(">>> ")  # add Volodymyr 380937000000
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!\nДо побачення!":
            break


if __name__ == "__main__":
    main()
