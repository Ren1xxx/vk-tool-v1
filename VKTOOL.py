import config
from config import first_name, last_name
from rich.console import Console
from rich.table import Table
from rich import print
from cls import cls
import sys
import os

cls()

table = Table(header_style="bold magenta", border_style="yellow", title="Опции:", caption="♥ʀᴇɴɪx ᴠᴋᴛᴏᴏʟ♥ ᴠ 1.0.0")
table.add_column("♥Номер♥")
table.add_column("♥Опции♥")
table.add_row(
    "1",
    "♥Добавить друзей со стен групп/страниц♥"
)
table.add_row(
    "2",
    "♥Добавить друзей с раздела рекомендации♥"
)
table.add_row(
    "3",
    "♥Принять новые заявки в друзья♥"
)
table.add_row(
    "4",
    "♥Принять все заявки в друзья♥"
)
table.add_row(
    "5",
    "♥Отписаться от всех исходящих заявок♥"
)
table.add_row(
    "6",
    "♥Удалить неактивных друзей♥"
)
table.add_row(
    "7",
    "♥Удалить невидимых друзей♥"
)
table.add_row(
    "8",
    "♥Удалить собачек из друзей♥"
)
table.add_row(
    "9",
    "♥Удалить всех друзей♥"
)
table.add_row(
    "10",
    "♥Написать в \"Добавь в друзья\"♥"
)
table.add_row(
    "11",
    "♥Коммент в \"Добавь в друзья\"♥"
)
table.caption_style = "bold cyan"

console = Console()
console.print(table)

print("")
vid = input(f"({first_name} {last_name}) ♥Выберите номер♥: ")

if vid == "1":
    import handlers.friends_add_from_wall
elif vid == "2":
    import handlers.friends_add_from_recommended_section
elif vid == "3":
    import handlers.request_accept.new
elif vid == "4":
    import handlers.request_accept.all
elif vid == "5":
    import handlers.unsubscribe
elif vid == "6":
    import handlers.friends_delete.one_day_and_more
elif vid == "7":
    import handlers.friends_delete.without_last_seen
elif vid == "8":
    import handlers.friends_delete.deleted
elif vid == "9":
    import handlers.friends_delete.all
elif vid == "10":
    import handlers.write
elif vid == "11":
    import handlers.comment
else:
    print("[red]♥Ошибка: Пункт не найден♥[/red]")
    sys.exit()
