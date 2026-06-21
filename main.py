import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = "Homework 3"

    name_field = ft.TextField(label="Введите имя")

    result_text = ft.Text()

    def show_message(e):
        current_time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        result_text.value = f"{current_time} - Привет, {name_field.value}!"
        page.update()

    page.add(
        name_field,
        ft.ElevatedButton("Показать", on_click=show_message),
        result_text
    )


ft.app(target=main)
