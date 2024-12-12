# Документация для `test_jupyter_examples.py`

## Обзор

Данный файл содержит тесты для проверки выполнения примеров Jupyter Notebook. Он использует `pytest` для параметризации тестов и `nbformat` для работы с notebook. Файл обеспечивает запуск всех примеров notebook в папке `../examples/` и проверяет, что они выполняются без ошибок.

## Содержание

1.  [Импорты](#импорты)
2.  [Константы](#константы)
3.  [Функции](#функции)
    *   [`get_notebooks`](#get_notebooks)
4.  [Тесты](#тесты)
    *   [`test_notebook_execution`](#test_notebook_execution)

## Импорты

```python
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest

import sys
```

## Константы

```python
NOTEBOOK_FOLDER = "../examples/"
TIMEOUT = 600
KERNEL_NAME = "python3"
```
- `NOTEBOOK_FOLDER`: Папка, содержащая тестируемые Jupyter Notebook.
- `TIMEOUT`: Максимальное время выполнения notebook в секундах.
- `KERNEL_NAME`: Название ядра Jupyter, используемое для выполнения notebook.

## Функции

### `get_notebooks`

**Описание**:
Извлекает все файлы Jupyter Notebook из указанной папки.

**Параметры**:
- `folder` (str): Путь к папке, содержащей файлы notebook.

**Возвращает**:
- `list[str]`: Список путей к файлам notebook.

```python
def get_notebooks(folder):
    """Retrieve all Jupyter notebook files from the specified folder."""
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb") and not ".executed." in f and not ".local." in f
    ]
```

## Тесты

### `test_notebook_execution`

**Описание**:
Выполняет Jupyter Notebook и проверяет, что не возникает исключений.

**Параметры**:
- `notebook_path` (str): Путь к файлу Jupyter Notebook.

**Вызывает исключения**:
- `pytest.fail`: Если во время выполнения notebook возникает исключение.

```python
@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path):
    """Execute a Jupyter notebook and assert that no exceptions occur."""
    with open(notebook_path, "r", encoding="utf-8") as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)
        print(f"Executing notebook: {notebook_path} with kernel: {KERNEL_NAME}")
        ep = ExecutePreprocessor(timeout=TIMEOUT, kernel_name=KERNEL_NAME)

        try:
            ep.preprocess(notebook, {'metadata': {'path': NOTEBOOK_FOLDER}})
            print(f"Notebook {notebook_path} executed successfully.")

        except Exception as ex:
            pytest.fail(f"Notebook {notebook_path} raised an exception: {ex}")

        finally:
            # save a copy of the executed notebook
            output_path = notebook_path.replace(".ipynb", ".executed.local.ipynb")
            with open(output_path, "w", encoding="utf-8") as out_file:
                nbformat.write(notebook, out_file)

            print(f"Executed notebook saved as: {output_path}")
```