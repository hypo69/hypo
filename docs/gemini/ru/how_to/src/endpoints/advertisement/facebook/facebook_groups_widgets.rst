Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `FacebookGroupsWidget`, предназначенный для создания и отображения выпадающего списка (Dropdown) с URL-адресами групп Facebook.  Класс считывает информацию о группах из файла JSON, формирует список доступных опций для Dropdown и отображает его в интерактивной среде (например, Jupyter Notebook).

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует библиотеки `header`, `IPython.display`, `ipywidgets`, `j_loads_ns` из пользовательского модуля `src.utils`, `types`, и `pathlib`. Эти библиотеки необходимы для работы с JSON, создания и отображения интерактивных виджетов.

2. **Определение класса `FacebookGroupsWidget`:** Класс `FacebookGroupsWidget` отвечает за создание и управление выпадающим списком.

3. **Инициализация (`__init__`):** Конструктор класса принимает путь к файлу JSON (`json_file_path`) как аргумент. Внутри конструктора данные из JSON файла парсятся и преобразуются в `SimpleNamespace` объект, хранящийся в переменной `self.groups_data`.  Затем создаётся виджет Dropdown и сохраняется в `self.dropdown`.

4. **Создание виджета Dropdown (`create_dropdown`):** Метод `create_dropdown` извлекает список URL-адресов групп из атрибута `self.groups_data` и создает объект `Dropdown` с этими URL-адресами в качестве опций.  `description`  устанавливает подпись для Dropdown.

5. **Отображение виджета (`display_widget`):** Метод `display_widget` использует функцию `display` из библиотеки `IPython.display`, чтобы отобразить созданный виджет `Dropdown`.


Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

    # Путь к файлу JSON с данными о группах
    json_file_path = Path("./groups.json")  

    # Создаем объект класса FacebookGroupsWidget
    fb_groups_widget = FacebookGroupsWidget(json_file_path)

    # Отображаем виджет
    fb_groups_widget.display_widget()