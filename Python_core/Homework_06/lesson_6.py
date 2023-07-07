"""
Завдання: Сортування файлів у папці.
Копіювати файли із зазначеної папки та покласти в нову папку з розширенням цього файлу.
"""
import argparse
from pathlib import Path
from shutil import copyfile

# Вважаємо що ми будемо запускати програму:
# python  Python%20core\Модуль%206.%20Робота%20з%20файлами\Homework_06\lesson_6.py -s home_dz -o dist
# python  lesson_6.py -s home_dz -o dist
# python lesson_6.py -s picture -o dist
# -s - source
# -o - output

parser = argparse.ArgumentParser(
    description="Sorting folder"
)  # парсер командної строки, description - просто опис, нінащо не впливає
parser.add_argument(
    "--source", "-s", required=True, help="Source folder"
)  # --source ім'я змінної, довгий запис (сюди приходить папку, яку потрібно обробити)
parser.add_argument(
    "--output", "-o", default="dist", help="Output folder"
)  # -o ім'я змінної, короткий запис (сюди приходить папку, куди потрібно скласти готовий результат)
args = vars(
    parser.parse_args()
)  # parser.parse_args() - парсер, vars - повертає словник
source = args.get("source")  # із словника отримаємо значення по ключу
output = args.get("output")  # із словника отримаємо значення по ключу
print(source, output)


def read_folder(path: Path) -> None:
    for el in path.iterdir():  # ітеруємось по папках  # path = picture (dir)
        if el.is_dir():  # перевіряємо чи це папка?
            read_folder(el)  # рекурсія
        else:
            copy_file(el)  # викликаємо ф-цію для копіювання файлу


def copy_file(file: Path) -> None:  # summer.jpg
    ext = file.suffix  # ext = .jpg
    new_path = output_folder / ext  # new_path = dist/.jpg/
    new_path.mkdir(exist_ok=True, parents=True)  # створюємо папку якщо вона не існує.
    copyfile(file, new_path / file.name)  # копіюємо файл у нову папку


output_folder = Path(output)
read_folder(Path(source))
