import os
import webbrowser

from abc import ABC, abstractmethod

from ContactBook import ContactBook
# from NoteBook import NoteManager
# from sort import FileSorter
# from CryptoPrice import CryptoPriceFetcher

# Базовий клас для модулів
class BaseClass(ABC):
    @abstractmethod
    def run(self):
        pass

class ContactBookABS(BaseClass):
    def run(self):
        contacts = ContactBook()
        contacts.main()
        print("ContactBook functionality")


class NoteManager(BaseClass):
    def run(self):
        print("NoteManager functionality")

class FileSorter(BaseClass):
    def run(self):
        target_folder = input("Enter the folder path to sort: ")
        print(f"Sorting files in {target_folder}")

class CryptoPriceFetcher(BaseClass):
    def run(self):
        print("CryptoPriceFetcher functionality")

class WebSearch(BaseClass):
    def run(self):
        query = input("Enter your search query: ")
        webbrowser.open(f"https://www.google.com/search?q={query}")

class Exit(BaseClass):
    def run(self):
        print("Goodbye!") 

def main():
    modules = {        
        '1': ContactBookABS(),
        '2': NoteManager(),
        '3': FileSorter(),
        '4': CryptoPriceFetcher(),
        '5': WebSearch(),
        '0': Exit(),        
    }
   
    while True:
        print("Choose a command:")
        for key, value in modules.items():
            print(f"{key}. {value.__class__.__name__}")

        user_input = input("Enter command number: ")

        if user_input in modules:
            modules[user_input].run()
           
            break
        else:
            print("Wrong command. Enter a valid command.")

if __name__ == '__main__':
    main()

