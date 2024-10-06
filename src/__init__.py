
## \file ../src/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""  **Это корневая директория проекта** 
@details 

@imagemain-launcher-suppler.png


@image html hypotez_flowchart.png
## Блоксхема 

- `Scenario` - JSON файл, содержащий последовательность действий для получения конечных данных
- `Supplier` - Класс поставщика. При инициализации получает список сценариев, после запуска отправляет их в исполнитель
- `Executor` - Исполнитель сценариев.
- `Connections Layer` - Подключение к источнику информации. Настраивается в классе поставщика.
- `Supplier's Data` - Информация и товаре. То, ради чего все сделано.
- `Parser` - Разбор полученных данных.
- `Product` - Сущность `товар` для экспорта.
- `Export Layer` - конечый получатель данных. У меня это фрймворк `Prestashop`.


---------------------------------------


Старт без параметров запусстит выполнения сценария/ев, из файлов поставщиков. 
Список поставщиков  <<по умолчанию>>
прописан в файле `settings.json`

- Запуск скрипта начинается в `main.py`

## Опции запуска программы

Запуск из командной строки
@code
> python main.py

~powershell
> ./run
@endcode

- При запуске из командной строки все настройки читаются из файла `settings.json`

Запуск из интерпретаторa python

@code
>python
>>> import main
>>> launcher()
@endcode

---------

Для настройки запуска см комментарии к функции `main.launcher()` (`src.main.launcher()`)



@details Парсер всего, что парсится 
@file
@image html 'kitkat diagrams-how it work.drawio.png' 
@todo
    1. Превратить поставщиков в классы и убрать suplier['related_functions']['login'] -> supplier.login
    2. s.locators["product"] -> в Enum
    3. Вынести поставщиков за переделы s
"""
...


from packaging.version import Version
from .version import __version__, __doc__, __details__
from .credentials import gs
