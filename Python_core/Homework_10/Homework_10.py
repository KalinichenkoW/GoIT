from collections import UserDict


# Клас Field, який буде батьківським для всіх полів,
# у ньому потім реалізуємо логіку, загальну для всіх полів.
class Field:
    def __init__(self, value):
        self.value = value


# Клас Name, обов'язкове поле з ім'ям.
class Name(Field):
    def __init__(self, name):
        self.name = name


# Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
class Phone(Field):
    phone = []

    def __init__(self, phone):
        self.phone = phone


# Клас Mail, необов'язкове поле з e-mail та таких один запис (Record) може містити кілька
class Mail(Field):
    pass
    # Field


# Клас Record, який відповідає за логіку додавання/видалення/редагування
# необов'язкових полів та зберігання обов'язкового поля Name.
class Record:
    phones = []
    emails = []

    def __init__(self, name: str, *phones: list, **emails: list):
        self.name = name
        self.phones = [Phone(phone) for phone in phones]
        self.emails = [Mail(email) for email in emails]  # emails

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def find_phone(self, value):
        pass

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


# Клас AddressBook, який наслідується від UserDict,
# та ми потім додамо логіку пошуку за записами до цього класу.
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)

    # Mentor
    # Для ДЗ 10 рекомендую в код додати наступні тести, при корректній реалізації ДЗ - вони повинні успішно пройти
    # if name == "main":

    # name = Name("Bill")
    # phone = Phone("1234567890")
    # email = Mail("mail@ukr.ua")
    # rec = Record(name)

    # ab = AddressBook()
    # ab.add_record(rec)


#     assert isinstance(ab['Bill'], Record)
#     assert isinstance(ab['Bill'].name, Name)
#     assert isinstance(ab['Bill'].phones, list)
#     assert isinstance(ab['Bill'].phones[0], Phone)
#     assert ab['Bill'].phones[0].value == '1234567890'
#     print('All Ok)')
