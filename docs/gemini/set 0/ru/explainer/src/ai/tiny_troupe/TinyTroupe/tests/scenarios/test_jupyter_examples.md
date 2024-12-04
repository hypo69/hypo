# <input code>

```python
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest

import sys
sys.path.insert(0, '../../tinytroupe/') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '../../') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '..') # ensures that the package is imported from the parent directory, not the Python installation

# Set the folder containing the notebooks
NOTEBOOK_FOLDER = "../examples/"  # Update this path

# Set a timeout for long-running notebooks
TIMEOUT = 600

KERNEL_NAME = "python3" #"py310"


def get_notebooks(folder):
    """Retrieve all Jupyter notebook files from the specified folder."""
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb") and not ".executed." in f and not ".local." in f
    ]


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

        except Exception as e:
            pytest.fail(f"Notebook {notebook_path} raised an exception: {e}")
        
        finally:
            # save a copy of the executed notebook
            output_path = notebook_path.replace(".ipynb", ".executed.local.ipynb")
            with open(output_path, "w", encoding="utf-8") as out_file:
                nbformat.write(notebook, out_file)
            
            print(f"Executed notebook saved as: {output_path}")
```

# <algorithm>

**Шаг 1:** Импорт библиотек.
* Импортируются необходимые модули: `os`, `nbformat`, `ExecutePreprocessor` из `nbconvert`, `pytest`, `sys`.
* `sys.path` изменяется, чтобы Python мог импортировать файлы из родительских директорий. Это важно для работы с пакетом `tinytroupe`.


**Шаг 2:** Настройка переменных.
* `NOTEBOOK_FOLDER`: Путь к папке с Jupyter ноутбуками.
* `TIMEOUT`: Таймаут для выполнения ноутбука.
* `KERNEL_NAME`: Имя ядра Jupyter.

**Шаг 3:** Функция `get_notebooks`.
* Принимает на вход папку.
* Возвращает список путей к Jupyter ноутбукам в этой папке, исключая те, которые уже были обработаны (имеют суффикс ".executed." или ".local.").

**Шаг 4:** Тест `test_notebook_execution`.
* Итерируется по списку ноутбуков, полученному из функции `get_notebooks`.
* Открывает Jupyter ноутбук.
* Выводит информацию о выполняемом ноутбуке.
* Создает экземпляр класса `ExecutePreprocessor` с заданными параметрами таймаута и ядра.
* Пытается выполнить ноутбук с помощью метода `preprocess`.
* Если выполнение прошло успешно, выводит сообщение об успехе и сохраняет измененный ноутбук с суффиксом ".executed.local.ipynb".
* Если возникло исключение, выводит сообщение об ошибке и прекращает выполнение теста.
* В `finally` блоке сохраняет выполненный ноутбук в файл с соответствующим именем.

**Пример данных:**

Вход: `NOTEBOOK_FOLDER = "../examples/"`  и существует файл `example.ipynb` в этой папке.

Выход: `example.ipynb` будет открыт и обработан. Сохранится `example.executed.local.ipynb`.


# <mermaid>

```mermaid
graph TD
    A[Начало] --> B{Импорт библиотек};
    B --> C[Настройка переменных];
    C --> D[get_notebooks(NOTEBOOK_FOLDER)];
    D --> E[Проверка списка ноутбуков];
    E -- Успех --> F[Открытие Jupyter ноутбука];
    E -- Ошибка --> G[Ошибка];
    F --> H[Создание ExecutePreprocessor];
    H --> I[Попытка выполнения ноутбука];
    I -- Успех --> J[Сохранение выполненного ноутбука];
    I -- Ошибка --> K[Обработка исключения];
    J --> L[Сообщение об успехе];
    K --> L;
    L --> M[Конец];
    G --> M;
```

**Подключаемые зависимости:**

* `os`: Для работы с файловой системой (получение списка ноутбуков, запись/чтение файлов).
* `nbformat`: Для работы с форматом Jupyter Notebook.
* `nbconvert`: Для выполнения ноутбуков.
* `pytest`: Для тестирования.
* `sys`: Для управления путем поиска модулей.

# <explanation>

**Импорты:**

* `os`: Для работы с операционной системой, например, для получения списка файлов в папке.
* `nbformat`: Для чтения и записи файлов Jupyter Notebook.
* `nbconvert.preprocessors`: Для выполнения кода в Jupyter Notebook.
* `pytest`: Для написания и запуска тестов.
* `sys`:  Для динамической модификации `sys.path`, что необходимо для импорта пакетов из текущей директории.


**Классы:**

* `ExecutePreprocessor`: Класс из библиотеки `nbconvert`, который отвечает за выполнение кода в ноутбуке. В данном случае он выполняет код ядра `KERNEL_NAME`  (например, `python3`).

**Функции:**

* `get_notebooks(folder)`: Возвращает список путей к Jupyter ноутбукам в заданной папке, исключая те, что уже были выполнены.

* `test_notebook_execution(notebook_path)`: Функция, которая выполняет Jupyter Notebook. Она принимает путь к ноутбуку в качестве аргумента. 
   * Открывает ноутбук.
   * Выводит сообщение о начале выполнения.
   * Использует `ExecutePreprocessor` для выполнения ноутбука.
   * Обрабатывает возможные исключения во время выполнения.
   * Сохраняет измененный ноутбук с суффиксом, указывающим на выполнение.


**Переменные:**

* `NOTEBOOK_FOLDER`: Путь к папке с ноутбуками.
* `TIMEOUT`: Таймаут выполнения ноутбука в секундах.
* `KERNEL_NAME`: Имя ядра Jupyter.
* `notebook_path`: Путь к конкретному ноутбуку, получаемый из `get_notebooks`.


**Возможные ошибки и улучшения:**

* **Обработка ошибок:** Код содержит обработку исключений (`try...except`), но можно добавить более детальную обработку (например, логирование).
* **Отчётливость:** Имена переменных, констант (например, `NOTEBOOK_FOLDER`) могли бы быть более информативными (`NOTEBOOKS_DIR`).
* **Универсальность**: Код можно сделать более гибким, например, сделать аргумент для выбора ядра.
* **Документация**: Добавление более подробной документации к функциям.

**Взаимосвязь с другими частями проекта:**

Код взаимодействует с файлами Jupyter Notebook, расположенными в папке `examples`. Предполагается, что `tinytroupe` предоставляет или использует библиотеки для работы с Jupyter, но конкретные зависимости не прописаны в примере.