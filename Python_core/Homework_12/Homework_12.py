import pickle
from collections import UserDict
from datetime import date
from dateparser import parse as dt_parser


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


class Record:
    def __init__(
        self, name: Name, phone: Phone, emails: list = None, birthday: Birthday = None
    ) -> None:
        name = self.try_valid_type_name(name)
        phone = self.try_valid_type_phone(phone)
        birthday = self.try_valid_type_birthday(birthday)

        self.name = name
        self.phones = [phone] if phone else []
        self.birthday = birthday if birthday is not None else None
        self.emails = [Mail(email) for email in emails]  # emails

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
    def try_valid_type_name(name: str) -> Name:
        if type(name) != Name:
            try:
                return Name(name)  # тут перезаписуємо змінну name в обькт классу
            except Exception:
                raise ValueError(
                    f"name: '{name}' must be type(Name) or a valid string representation of a Name object"
                )
        return name

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

    @staticmethod
    def try_valid_type_birthday(birthday: str) -> str:
        if type(birthday) != Birthday and birthday != None:
            try:
                return Birthday(str(birthday))
            except Exception:
                raise ValueError(
                    f"birthday:{birthday} must be type(Birthday) or a valid string representation of a Birthday object"
                )
        return birthday

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
class AddressBook(UserDict):
    MAX_VALUE = 5

    def __init__(self):
        self.current_value = 0

    def dump(self):
        with open(self.file, "wb") as file:
            pickle.dump((self.last_record_id, self.records), file)

    def load(self):
        if not self.file.exists():
            return
        with open(self.file, "rb") as file:
            self.last_record_id, self.records = pickle.load(file)

    def search(self, search_str: str):
        result = []
        for record_id, record in self.records.items():
            if search_str in record:
                result.append(record_id)
        return result

    # ===========================================================

    # def add_record(self, record: Record):
    #     self.data[record.name.value] = record

    # def find_record(self, value):
    #     return self.data.get(value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self
        raise StopIteration


if __name__ == "__main__":
    # p = Phone("0638884455")
    # print(p)
    # test = Birthday("1994/02/26")
    # print(test)
