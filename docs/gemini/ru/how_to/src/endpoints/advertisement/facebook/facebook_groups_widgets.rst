Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `FacebookGroupsWidget`, который создает и отображает выпадающий список (`Dropdown`) с URL адресами групп Facebook.  Список URL-адресов загружается из JSON файла.  Класс позволяет динамически создавать и отображать этот виджет для выбора группы в интерфейсе, например, в Jupyter Notebook.

Шаги выполнения
-------------------------
1. **Импортирует необходимые библиотеки:**  Код импортирует библиотеки `header`, `IPython.display`, `ipywidgets`, `src.utils`, `types`, и `pathlib`.  Библиотеки `IPython.display` и `ipywidgets` необходимы для создания и отображения виджетов в Jupyter Notebook, `src.utils` предполагается содержит функцию для загрузки данных из JSON, а `types` и `pathlib`  - для работы с данными.

2. **Определяет класс `FacebookGroupsWidget`:**  Класс `FacebookGroupsWidget` содержит методы для работы с виджетом.

3. **Инициализирует класс `FacebookGroupsWidget`:** Конструктор `__init__` принимает путь к JSON-файлу `json_file_path` в качестве аргумента.  Внутри конструктора данные из JSON файла загружаются и сохраняются в `self.groups_data`.  Затем вызывается метод `create_dropdown()` для создания виджета.

4. **Создает выпадающий список:** Метод `create_dropdown` создает экземпляр виджета `Dropdown`.  Он извлекает список ключей (URL-адресов групп) из данных `self.groups_data`.  Эти URL-адреса устанавливаются как опции для выпадающего списка.  Описание выпадающего списка устанавливается как 'Facebook Groups:'.

5. **Отображает виджет:** Метод `display_widget` отображает созданный виджет `self.dropdown` с помощью `display()`.

Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

    # Путь к вашему JSON файлу
    json_file_path = Path("./path/to/your/groups.json")

    # Создаем экземпляр класса
    facebook_groups_widget = FacebookGroupsWidget(json_file_path)

    # Отображаем виджет
    facebook_groups_widget.display_widget()