from collections import UserDict
from datetime import date
from dateparser import parse as dt_parser


# Клас Field, який буде батьківським для всіх полів,
# у ньому потім реалізуємо логіку, загальну для всіх полів.
class Field:
    def __init__(self, value):
        self.__value = None  # додамо захищенне поле
        self.value = value

    @staticmethod
    def __valid_value(value) -> None:
        if type(value) != str:
            raise TypeError("received data must be STR")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self.__valid_value(value)
        self._value = value

    def __str__(self) -> str:
        return f"{self.value}"


# Клас Name, обов'язкове поле з ім'ям.
class Name(Field):
    def __init__(self, value: str):
        self.value = value


class Phone(Field):
    """
    Class representing the phone field in a record of the address book.
    """

    def __init__(self, value: str) -> None:
        self.value = value  # при инициализации отрабативает сеттер

    @staticmethod
    def __valid_phone(value) -> None:
        phone = "".join(filter(str.isdigit, value))
        if 9 >= len(phone) <= 15:  # псевдо проверка номера
            raise ValueError("Phone number isn't correct")

    @Field.value.setter  # переопределяем сеттер родительского класса
    def value(self, value: str) -> None:
        super(Phone, Phone).value.__set__(
            self, value
        )  # родительский сеттер проверка на стр
        self.__valid_phone(value)
        self._value = value


# Клас Mail, необов'язкове поле з e-mail та таких один запис (Record) # може містити кілька
class Mail(Field):
    pass


class FormatDateError(Exception):
    """
    Exception, If the input date string is not in a valid date format.
    """

    pass


class Birthday(Field):
    """
    Class representing the birthday field in a record of the address book.
    The date is stored in ISO 8601 format.
    """

    def __init__(self, value: str) -> None:
        self.value = value  # при инициализации отрабативает сеттер

    @staticmethod
    def __valid_date(value: str) -> str:
        try:
            return date.isoformat(
                dt_parser(str(value), settings={"STRICT_PARSING": True}).date()
            )
        except Exception:
            raise FormatDateError("not correct date!!!")

    @Field.value.setter
    def value(self, value: str) -> None:
        self._value = self.__valid_date(value)


# Клас Record, який відповідає за логіку додавання/видалення/редагування
# необов'язкових полів та зберігання обов'язкового поля Name. Phone=None)
class Record:
    def __init__(
        self, name: str, phone: Phone, emails: list = None, birthday: Birthday = None
    ):
        self.name = name
        # self.phones = [Phone(phone) for phone in phones]
        self.emails = [Mail(email) for email in emails]  # emails
        self.birthday = Birthday(birthday)
        phone = self.try_valid_type_phone(phone)

    def days_to_birthday(self) -> int:
        if self.birthday == None:
            raise RecordNotBirthdayError("No birthday set for the contact.")
        today = date.today()
        bday = date.fromisoformat(self.birthday.value).replace(
            year=today.year
        )  # дата др в этом году
        if today > bday:  # если др уже прошло берем дату следующего(в следующем году)
            bday = bday.replace(year=today.year + 1)
        return (bday - today).days

    @staticmethod
    def try_valid_type_phone(phone: str) -> Phone:
        if type(phone) != Phone:
            try:
                return Phone(phone)
            except Exception:
                raise ValueError(
                    f"phone:{phone} must be type(Phone) or a valid string representation of a Phone object"
                )
        return phone

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


if __name__ == "__main__":
    p = Phone("0638884455")
    print(p)
    test = Birthday("1994/02/26")
    print(test)

    rec_1 = Record("Олена", "0638884455", "test@MAIL.UA", "20/10/2000")
    print(rec_1.days_to_birthday())
