# Документация для `test_jupyter_examples.py`

## Обзор

Данный файл содержит тесты для выполнения Jupyter Notebooks и проверки отсутствия ошибок при их исполнении. Он использует `pytest` для параметризации тестов и `nbformat` и `nbconvert` для работы с Jupyter Notebooks.

## Оглавление

1. [Импорты](#Импорты)
2. [Константы](#Константы)
3. [Функции](#Функции)
    - [`get_notebooks`](#get_notebooks)
4. [Тесты](#Тесты)
    - [`test_notebook_execution`](#test_notebook_execution)
 
## Импорты

```python
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest

import sys
sys.path.insert(0, '../../tinytroupe/')
sys.path.insert(0, '../../')
sys.path.insert(0, '..')
```
- `os`: Для работы с файловой системой.
- `nbformat`: Для чтения и записи Jupyter Notebooks.
- `nbconvert.preprocessors.ExecutePreprocessor`: Для выполнения Jupyter Notebooks.
- `pytest`: Для создания тестов.
- `sys`: Для модификации пути поиска модулей.

## Константы

```python
NOTEBOOK_FOLDER = "../examples/"  
TIMEOUT = 600
KERNEL_NAME = "python3"
```
- `NOTEBOOK_FOLDER`: Путь к папке с Jupyter Notebooks для тестирования.
- `TIMEOUT`: Время ожидания выполнения Jupyter Notebooks в секундах.
- `KERNEL_NAME`: Имя ядра Jupyter Notebook, которое будет использоваться для выполнения.

## Функции

### `get_notebooks`

**Описание**:
Извлекает все Jupyter Notebook файлы из указанной папки.

```python
def get_notebooks(folder):
    """Retrieve all Jupyter notebook files from the specified folder."""
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb") and not ".executed." in f and not ".local." in f
    ]
```

**Параметры**:
- `folder` (str): Путь к папке, в которой ищутся файлы.

**Возвращает**:
- `list`: Список путей к Jupyter Notebook файлам.

## Тесты

### `test_notebook_execution`

**Описание**:
Выполняет Jupyter Notebook и проверяет, что не возникает исключений.

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
**Параметры**:
- `notebook_path` (str): Путь к Jupyter Notebook файлу.

**Вызывает исключения**:
- `pytest.fail`: Вызывается в случае возникновения исключения при выполнении Jupyter Notebook.