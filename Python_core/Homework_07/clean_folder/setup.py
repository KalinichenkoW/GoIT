from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="1.0.0",
    description="Наводимо порядо у папках",
    url="http://github.com/kalinichenko.w/Homework_07",
    author="Volodymyr Kalinichenko",
    author_email="kalinichenko.w@gmail.com",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["clean_folder=clean_folder.clean:start"]},
)
