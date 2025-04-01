# Модуль для тестирования Jupyter Notebook примеров
====================================================

Модуль `test_jupyter_examples.py` предназначен для автоматического тестирования Jupyter Notebook файлов, расположенных в директории `examples`. Он использует библиотеки `nbformat` и `nbconvert` для выполнения ноутбуков и проверяет, не возникают ли ошибки в процессе выполнения.

## Обзор

Этот модуль выполняет следующие задачи:

1.  Находит все файлы Jupyter Notebook (`.ipynb`) в указанной директории.
2.  Выполняет каждый ноутбук, используя ядро Python3.
3.  Проверяет, не возникли ли исключения во время выполнения.
4.  Сохраняет копию выполненного ноутбука с добавлением суффикса `.executed.local.ipynb`.
5.  Пропускает выполнение ноутбуков, если параметр `test_examples` установлен в `False`.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `get_notebooks`

```python
def get_notebooks(folder: str) -> list[str]:
    """Retrieve all Jupyter notebook files from the specified folder."""
    ...
```

**Назначение**: Извлекает все Jupyter notebook файлы из указанной папки.

**Параметры**:

*   `folder` (str): Путь к папке, содержащей ноутбуки.

**Возвращает**:

*   `list[str]`: Список путей ко всем Jupyter notebook файлам в указанной папке.

**Как работает функция**:

1.  Функция принимает на вход путь к папке (`folder`).
2.  Использует `os.listdir(folder)` для получения списка всех файлов и директорий в указанной папке.
3.  Фильтрует список, оставляя только файлы, удовлетворяющие следующим условиям:
    *   Имеют расширение `.ipynb`.
    *   Не содержат в имени `.executed.`.
    *   Не содержат в имени `.local.`.
4.  Формирует полные пути к файлам с использованием `os.path.join(folder, f)`.
5.  Возвращает список полных путей к Jupyter notebook файлам.

**ASCII Flowchart**:

```
A[Получение списка файлов из папки]
|
B[Фильтрация файлов по расширению и наличию '.executed.' или '.local.']
|
C[Формирование полных путей к файлам]
|
D[Возврат списка путей]
```

**Примеры**:

```python
# Пример использования функции get_notebooks
notebook_folder = "../../examples/"
notebooks = get_notebooks(notebook_folder)
print(notebooks)  # Вывод: список путей к Jupyter notebook файлам в папке examples
```

### `test_notebook_execution`

```python
@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path: str) -> None:
    """Execute a Jupyter notebook and assert that no exceptions occur."""
    ...
```

**Назначение**: Выполняет Jupyter notebook и проверяет, не возникают ли исключения.

**Параметры**:

*   `notebook_path` (str): Путь к Jupyter notebook файлу.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Функция принимает на вход путь к Jupyter notebook файлу (`notebook_path`).
2.  Проверяет, установлен ли флаг `conftest.test_examples` в `True`. Если нет, то пропускает выполнение ноутбука.
3.  Открывает ноутбук с использованием кодировки UTF-8.
4.  Инициализирует `ExecutePreprocessor` с указанием времени ожидания (`TIMEOUT`) и имени ядра (`KERNEL_NAME`).
5.  Выполняет ноутбук с использованием `ep.preprocess(notebook, {'metadata': {'path': NOTEBOOK_FOLDER}})`.
6.  В случае возникновения исключения, тест завершается с ошибкой `pytest.fail`.
7.  Сохраняет копию выполненного ноутбука с суффиксом `.executed.local.ipynb`.

**ASCII Flowchart**:

```
A[Проверка флага conftest.test_examples]
|
B[Открытие Notebook файла]
|
C[Инициализация ExecutePreprocessor]
|
D[Выполнение Notebook]
|
E[Обработка исключений]
|
F[Сохранение выполненной копии Notebook]
```

**Примеры**:

```python
# Пример вызова функции test_notebook_execution (обычно вызывается pytest)
# pytest test_jupyter_examples.py
```
```python
# test_jupyter_examples.py
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest

import sys
sys.path.insert(0, '../../tinytroupe/') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '../../') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '..') # ensures that the package is imported from the parent directory, not the Python installation

import conftest

# Set the folder containing the notebooks
NOTEBOOK_FOLDER = os.path.join(os.path.dirname(__file__), "../../examples/")  # Update this path

# Set a timeout for long-running notebooks
TIMEOUT = 600

KERNEL_NAME = "python3" #"py310"


def get_notebooks(folder: str) -> list[str]:
    """
    Извлекает все Jupyter notebook файлы из указанной папки.

    Args:
        folder (str): Путь к папке, содержащей ноутбуки.

    Returns:
        list[str]: Список путей ко всем Jupyter notebook файлам в указанной папке.
    """
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb") and not ".executed." in f and not ".local." in f
    ]


@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path: str) -> None:
    """
    Выполняет Jupyter notebook и проверяет, не возникают ли исключения.

    Args:
        notebook_path (str): Путь к Jupyter notebook файлу.

    Returns:
        None
    """

    if conftest.test_examples:
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
    else:
        print(f"Skipping notebooks executions for {notebook_path}.")