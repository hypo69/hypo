# Модуль `test_jupyter_examples`

## Обзор

Этот модуль содержит тесты для проверки выполнения Jupyter-ноутбуков.  Он перебирает все `.ipynb` файлы в указанной папке, выполняет их и сохраняет результаты.

## Функции

### `get_notebooks`

**Описание**: Возвращает список путей к Jupyter-ноутбукам в заданной папке.

**Параметры**:
- `folder` (str): Путь к папке с ноутбуками.

**Возвращает**:
- list[str]: Список путей к `.ipynb` файлам в папке.  Возвращает пустой список, если папка пуста или в ней нет `.ipynb` файлов.

**Вызывает исключения**:
- `FileNotFoundError`: Если указанная папка не найдена.

### `test_notebook_execution`

**Описание**: Выполняет Jupyter-ноутбук и проверяет, что не возникло никаких исключений.

**Параметры**:
- `notebook_path` (str): Путь к Jupyter-ноутбуку.

**Возвращает**:
-  Не имеет значения.

**Вызывает исключения**:
- `Exception`: Если во время выполнения ноутбука возникло какое-либо исключение. В этом случае тест завершается с ошибкой.

**Примечание**:  Функция использует `pytest.fail` для  остановки теста при возникновении исключения и предоставления подробного сообщения об ошибке.  Также сохраняет копию выполненного ноутбука с добавленным префиксом ".executed.local.".


## Постоянные значения

### `NOTEBOOK_FOLDER`

**Описание**: Путь к папке, содержащей Jupyter-ноутбуки.  **НЕОБХОДИМО** обновить этот путь в коде перед использованием.

### `TIMEOUT`

**Описание**:  Таймаут для длительных вычислений в Jupyter-ноутбуках (в секундах).

### `KERNEL_NAME`

**Описание**: Имя ядра, используемого для выполнения ноутбуков.


## Подробности импорта

- `os`: Предоставляет функции для работы с файловой системой (например, поиск файлов).
- `nbformat`: Библиотека для работы с форматом Jupyter Notebook.
- `nbconvert.preprocessors`: Модуль для обработки Jupyter Notebooks.  Используется для выполнения кода.
- `pytest`: Библиотека для написания тестов.
- `sys`:  Библиотека для доступа к системным параметрам. Используется для добавления каталогов в `sys.path`, что позволяет импортировать модули из родительских каталогов.

**Важно**:  Строки `sys.path.insert(0, '...tinytroupe/')` и т.д. необходимы для корректного импорта модулей из родительских каталогов.  Необходимо скорректировать пути, если структура проекта отличается.