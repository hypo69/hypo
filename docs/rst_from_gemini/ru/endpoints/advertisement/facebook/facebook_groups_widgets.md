```markdown
# facebook_groups_widgets.py

Файл: `C:\Users\user\Documents\repos\hypotez\src\endpoints\advertisement\facebook\facebook_groups_widgets.py`

**Роль:** `doc_creator` (генератор документации)

**Описание:**

Этот модуль предоставляет класс `FacebookGroupsWidget`, который создаёт и отображает интерактивный виджет выпадающего списка с URL-адресами групп Facebook.  Список загружается из файла JSON.  Позволяет пользователю выбрать группу для размещения объявления.

**Класс `FacebookGroupsWidget`:**

Этот класс отвечает за создание и управление виджетом Dropdown для выбора группы Facebook.

**Методы класса:**

* **`__init__(self, json_file_path: Path)`:**
    * Инициализирует объект `FacebookGroupsWidget`.
    * Загружает данные о группах из файла JSON, используя функцию `j_loads_ns` из модуля `src.utils`.  Результат парсинга хранится в атрибуте `self.groups_data` в виде `SimpleNamespace`.
    * Создаёт виджет Dropdown и сохраняет его в `self.dropdown`.

* **`create_dropdown(self) -> Dropdown`:**
    * Создаёт и возвращает виджет `Dropdown` на основе загруженных данных из JSON.
    * Варианты выбора (`options`) в `Dropdown` — это ключи (URL-адреса групп) из словаря `self.groups_data`.
    * Описывает виджет, добавляя метку 'Facebook Groups:'.

* **`display_widget(self)`:**
    * Отображает созданный виджет `Dropdown` в интерактивной среде, например, в Jupyter Notebook.

**Требования:**

* Модуль `header` (импортируется, но его содержимое не определено в предоставленном фрагменте).
* Модуль `ipywidgets` для работы с виджетами.
* Модуль `IPython.display` для отображения виджетов.
* Модуль `src.utils`, содержащий функцию `j_loads_ns` для загрузки данных из JSON в `SimpleNamespace`.
* Файл JSON с URL-адресами групп Facebook, путь к которому передаётся в конструктор.


**Пример использования (в интерактивной среде, например, Jupyter Notebook):**

```python
from pathlib import Path
from facebook_groups_widgets import FacebookGroupsWidget

# Путь к файлу JSON
json_file = Path("./facebook_groups.json")  # Замените на реальный путь

# Создание виджета
widget = FacebookGroupsWidget(json_file)

# Отображение виджета
widget.display_widget()
```


**Примечание:**

Для корректной работы требуется файл `facebook_groups.json` в формате, соответствующем ожидаемому формату `j_loads_ns`.
```