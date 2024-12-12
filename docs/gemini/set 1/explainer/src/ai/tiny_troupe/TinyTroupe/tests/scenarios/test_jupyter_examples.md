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

**Описание алгоритма:**

1. **Импорты:**  Код импортирует необходимые библиотеки для работы с Jupyter notebooks (`nbformat`, `ExecutePreprocessor`), тестирования (`pytest`), и операционной системой (`os`). Также есть импорты для управления путями (`sys`).
2. **Настройка путей:**  Код добавляет пути к каталогу с пакетом `tinytroupe` и родительским каталогам в `sys.path`, чтобы Python мог найти нужные модули.
3. **Установка констант:**  `NOTEBOOK_FOLDER`, `TIMEOUT`, `KERNEL_NAME` определяют настройки для работы с ноутбуками.
4. **Функция `get_notebooks`:** Получает список путей к .ipynb файлам в заданном каталоге (`NOTEBOOK_FOLDER`). Фильтрует файлы, исключая уже обработанные.  Пример: Если `NOTEBOOK_FOLDER = "../examples"` и в нём находятся `example1.ipynb`, `example2.ipynb`, то функция вернёт список  `["../examples/example1.ipynb", "../examples/example2.ipynb"]`.
5. **Тест `test_notebook_execution`:**
   -  Итеративно проходит по списку ноутбуков, полученному функцией `get_notebooks`.
   -  Читает содержимое ноутбука `.ipynb` в переменную `notebook`.
   -  Выводит сообщение об исполняемом ноутбуке и ядре.
   -  Создаёт экземпляр `ExecutePreprocessor` с заданным таймаутом и ядром.
   -  Блок `try...except`:  Выполняет `preprocess` на ноутбуке, записывая результат в `notebook`. Если возникнет исключение, то тест завершается с ошибкой.
   -  Блок `finally`: Создаёт копию выполненного ноутбука с добавлением ".executed.local.ipynb" в имя.


**Пример данных:**

Вход: `NOTEBOOK_FOLDER = "../examples"`. В директории содержатся файлы `example1.ipynb`, `example2.ipynb`.

Выход: функция `get_notebooks` вернёт список `["../examples/example1.ipynb", "../examples/example2.ipynb"]`.


# <mermaid>

```mermaid
graph TD
    A[Импорты] --> B{Настройка путей};
    B --> C[Установка констант];
    C --> D[Функция get_notebooks];
    D --> E[Тест test_notebook_execution];
    E --> F[Чтение ноутбука];
    F --> G[Выполнение ноутбука];
    G --Успех--> H[Сохранение результата];
    G --Ошибка--> I[Обработка ошибки];
    H --> J[Вывести сообщение];
    I --> J;
    subgraph "tinytroupe"
        H --Зависимость--> tinytroupe
    end
    
    subgraph "nbformat, ExecutePreprocessor"
        B --Зависимость--> nbformat, ExecutePreprocessor
    end

    subgraph "pytest"
        E --Зависимость--> pytest
    end

    subgraph "os"
        B --Зависимость--> os
    end

    style F fill:#f9f,stroke:#333,stroke-width:2px
```

# <explanation>

**Импорты:**

- `os`: Для взаимодействия с файловой системой (получение списка файлов, создание копий).
- `nbformat`: Для чтения и записи файлов Jupyter Notebook.
- `nbconvert.preprocessors.ExecutePreprocessor`: Для выполнения кода в ноутбуках.
- `pytest`: Для запуска тестов.
- `sys`: Для управления путями импорта, необходим для работы с пакетами в иерархии каталогов.

**Классы:**

- `ExecutePreprocessor`: Этот класс из пакета `nbconvert` отвечает за выполнение ядра Jupyter.  Код не создаёт собственных классов.

**Функции:**

- `get_notebooks(folder)`: Получает список путей к Jupyter notebook-файлам в заданной папке, возвращает список строк.
- `test_notebook_execution(notebook_path)`: Функция, которая запускает notebook и проверяет, что нет исключений.  Принимает путь к notebook.  Не возвращает значений, но может выводить сообщения и сохранять результаты.


**Переменные:**

- `NOTEBOOK_FOLDER`: Строка, содержащая путь к папке с Jupyter notebook-файлами.
- `TIMEOUT`: Целое число, определяющее таймаут выполнения notebook (в секундах).
- `KERNEL_NAME`: Строка, имя ядра для выполнения ноутбука.


**Возможные ошибки/улучшения:**

- **Обработка исключений:**  Обработка исключений в блоке `try...except` - хороший подход, но следует указать более подробную информацию об исключениях в сообщении об ошибке для улучшения отладки.
- **Управление ошибками таймаута:**  Код обрабатывает исключения, но отсутствие более детальной информации о типе исключения (например, TimeoutError) может сделать отладку сложнее.

**Взаимосвязи с другими частями проекта:**

Код тестирует работу Jupyter ноутбуков, предполагая наличие соответствующих ячеек кода, которые будут выполняться.  Он использует библиотеки из пакета `nbconvert`, который, предположительно, входит в состав проекта `tinytroupe`.  Зависимости от проекта `tinytroupe` неявны, но предполагается, что ноутбуки содержат код, который использует функции или классы, определённые в этом проекте.  Обратите внимание, что код предполагает, что ноутбуки находятся в папке "../examples/".