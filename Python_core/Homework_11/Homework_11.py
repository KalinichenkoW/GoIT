from collections import UserDict
from datetime import datetime, date


# Клас Field, який буде батьківським для всіх полів,
# у ньому потім реалізуємо логіку, загальну для всіх полів.
class Field:
    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        if hasattr(value, "value"):
            value = value.value
        else:
            value = value
        return self.value == value

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self.value = value


# Клас Name, обов'язкове поле з ім'ям.
class Name(Field):
    pass


# Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) # може містити кілька.
class Phone(Field):
    pass


# Клас Mail, необов'язкове поле з e-mail та таких один запис (Record) # може містити кілька
class Mail(Field):
    pass


class Birthday(Field):
    pass


# Клас Record, який відповідає за логіку додавання/видалення/редагування
# необов'язкових полів та зберігання обов'язкового поля Name. Phone=None)
class Record:
    def __init__(self, name: str, phones: list, emails: list, birthday: date):
        self.name = name
        self.phones = [Phone(phone) for phone in phones]
        self.emails = [Mail(email) for email in emails]  # emails
        self.birthday = Birthday(birthday)

    # повертає кількість днів до наступного дня народження.
    def days_to_birthday(self, birthday):
        today = datetime.now()

        birthday = birthday.replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        time_diff = birthday - today

        return f"Your birthday is in {time_diff.days} days."

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def find_phone(self, value):
        pass

    def delete_phone(self, phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            raise ValueError(f"phone {phone} not exists")

    # def delete_phone(self, phone):
    #     if phone in self.phones:
    #         self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


# Клас AddressBook, який наслідується від UserDict,
# та ми потім додамо логіку пошуку за записами до цього класу.
class AddressBook(UserDict):
    MAX_VALUE = 5

    def __init__(self):
        self.current_value = 0

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self
        raise StopIteration
