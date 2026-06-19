from datetime import datetime

name = input("Введите имя: ")

current_time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

print(f"{current_time} - Привет, {name}!")