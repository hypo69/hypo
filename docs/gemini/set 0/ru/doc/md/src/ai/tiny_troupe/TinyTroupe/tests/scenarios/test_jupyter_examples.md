# Модуль `test_jupyter_examples.py`

## Обзор

Этот модуль содержит тесты для проверки выполнения Jupyter ноутбуков. Он использует библиотеку `nbformat` для чтения и обработки ноутбуков, а `ExecutePreprocessor` для их выполнения. Модуль проверяет, что ноутбуки выполняются без ошибок, и сохраняет их в виде исполненных копий с добавлением префикса ".executed.".


## Функции

### `get_notebooks`

**Описание**: Возвращает список путей к Jupyter ноутбукам в заданной папке.

**Параметры**:
- `folder` (str): Путь к папке с ноутбуками.

**Возвращает**:
- list[str]: Список путей к файлам Jupyter ноутбуков с расширением `.ipynb`.


### `test_notebook_execution`

**Описание**: Выполняет Jupyter ноутбук и проверяет отсутствие исключений во время выполнения.

**Параметры**:
- `notebook_path` (str): Путь к файлу Jupyter ноутбука.

**Возвращает**:
- None

**Вызывает исключения**:
- `pytest.fail`: Если во время выполнения ноутбука произошла ошибка.


## Константы

### `NOTEBOOK_FOLDER`

**Описание**: Путь к папке, содержащей Jupyter ноутбуки.

**Тип**: str

**Значение**: `"../examples/"`


### `TIMEOUT`

**Описание**: Время ожидания выполнения ноутбука (в секундах).

**Тип**: int

**Значение**: `600`


### `KERNEL_NAME`

**Описание**: Имя ядра Jupyter, используемого для выполнения ноутбуков.

**Тип**: str

**Значение**: `"python3"`


## Модульные переменные

### `sys.path`

**Описание**: Путь, используемый для импорта пакетов.


## Примечания

Этот модуль предполагает, что папки `../../tinytroupe/` и `../../` находятся на пути поиска Python. Необходимо указать правильное значение `NOTEBOOK_FOLDER`, если оно отличается от значения по умолчанию.

```