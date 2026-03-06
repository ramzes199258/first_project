import sys
print(sys.executable)

from dotenv import load_dotenv
import os

# Загрузка переменных из .env
load_dotenv(dotenv_path=r'C:\Users\79101\my_project_2\.env')

def print_author():
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

# Вызов функции
print_author()
