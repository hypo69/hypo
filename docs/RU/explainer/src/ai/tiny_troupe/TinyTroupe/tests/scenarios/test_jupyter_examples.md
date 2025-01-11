```MD
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

**Шаг 1:** Импорт необходимых библиотек.
  * `os`: Для работы с файловой системой.
  * `nbformat`: Для работы с Jupyter Notebook файлами.
  * `ExecutePreprocessor`: Для выполнения Jupyter Notebook.
  * `pytest`: Для запуска тестов.
  * `sys`: Для изменения пути поиска модулей.

**Шаг 2:** Установка пути поиска модулей.
  * `sys.path.insert(0, ...)`: Добавляет директории в начало пути поиска, что необходимо, если `tinytroupe` расположен в другом каталоге.

**Шаг 3:** Определение переменных `NOTEBOOK_FOLDER`, `TIMEOUT`, `KERNEL_NAME`.
  * `NOTEBOOK_FOLDER`: Путь к папке с Jupyter Notebook.
  * `TIMEOUT`: Максимальное время выполнения Notebook.
  * `KERNEL_NAME`: Имя ядра для выполнения.

**Шаг 4:** Функция `get_notebooks(folder)` возвращает список путей к Jupyter Notebook файлам в заданной папке, исключая файлы, содержащие ".executed." или ".local.".

**Шаг 5:** Декоратор `@pytest.mark.parametrize`:
  * Итерируется по списку, полученному функцией `get_notebooks`.
  * Для каждого пути выполняется функция `test_notebook_execution`.

**Шаг 6:** Функция `test_notebook_execution(notebook_path)`:
  * Читает Jupyter Notebook из файла `notebook_path`.
  * Выводит сообщение о выполнении.
  * Создает экземпляр `ExecutePreprocessor`.
  * Выполняет `notebook` с помощью `ep.preprocess`.
  * Если произошла ошибка, завершает тест с сообщением об ошибке.
  * В блоке `finally` сохраняет измененный `notebook` в новый файл с добавленным префиксом ".executed.local".

**Пример данных:**
Если `NOTEBOOK_FOLDER` = "../examples/", а в этой папке есть `example1.ipynb`, то `get_notebooks` вернёт `['../examples/example1.ipynb']`.  Функция `test_notebook_execution` обработает этот файл, сохранив результат в `../examples/example1.executed.local.ipynb`.

# <mermaid>

```mermaid
graph LR
    A[Начало] --> B{Получить список .ipynb};
    B --> C[Выполнить .ipynb];
    C --> D{Обработка исключений};
    D -- Успех --> E[Сохранить .executed.local.ipynb];
    D -- Ошибка --> F[Отчет об ошибке];
    E --> G[Конец];
    F --> G;
    subgraph "get_notebooks"
        B1[os.listdir(NOTEBOOK_FOLDER)] --> B2[Фильтр .ipynb];
        B2 --> B3[os.path.join(folder,f)];
    end
    subgraph "test_notebook_execution"
       C1[nbformat.read(nb_file)] --> C2[ep.preprocess(notebook)];
       C2 --> C3[Сохранить в out_file];
    end
```

# <explanation>

**Импорты:**

* `os`:  Для взаимодействия с файловой системой (получение списка файлов, создание/обработка файлов).
* `nbformat`: Для работы с форматом Jupyter Notebook (.ipynb).
* `ExecutePreprocessor`: из пакета `nbconvert`, отвечает за выполнение кода в ячейках Jupyter Notebook.
* `pytest`: Для написания и запуска автоматических тестов.
* `sys`: Для динамической модификации пути поиска модулей Python (`sys.path`).  Это важно для корректного импорта пакетов, которые находятся не в стандартном месте.

**Классы:**

* Нет явных пользовательских классов в коде. Используется класс `ExecutePreprocessor` из библиотеки `nbconvert`.  Этот класс отвечает за выполнение кода в Jupyter Notebook.

**Функции:**

* `get_notebooks(folder)`:  Возвращает список путей к .ipynb файлам в указанной папке. Использует `os.listdir` для получения списка всех файлов в папке и фильтрует, оставляя только .ipynb файлы.
* `test_notebook_execution(notebook_path)`: Эта функция является тестом. Она выполняет .ipynb файл, используя `ExecutePreprocessor` и обрабатывает любые возникшие исключения. Важно, что она сохраняет измененный Notebook в отдельный файл.

**Переменные:**

* `NOTEBOOK_FOLDER`:  Путь к папке с Jupyter Notebook файлами. Важно, чтобы этот путь был корректным относительно исполняемого файла.
* `TIMEOUT`:  Максимальное время ожидания выполнения ячеек Notebook в секундах.
* `KERNEL_NAME`: Имя ядра, используемого для выполнения. `python3` - типичное ядро для Python 3.

**Возможные ошибки или области для улучшений:**

* **Обработка ошибок:** Код пытается перехватить исключения, но можно добавить более подробную диагностику ошибок (логирование, улучшенное сообщение об ошибке).
* **Подключение к тестированию:** код использует `pytest`, но не включает утверждения (assert).  Тестирование без утверждений не будет корректным.
* **Управление зависимостями:** Использование `sys.path.insert` накладывает ответственность на пользователя для корректной установки пути. Использование `setup.py` или `requirements.txt` лучшее решение.
* **Документация:** Добавить более подробную документацию к функциям и переменным для лучшего понимания.
* **Удаление временных файлов:** Если код выполняется в непрерывном цикле, необходимо обеспечить удаление временных файлов `.executed.local.ipynb` после их использования.  Это поможет предотвратить накопление файлов и освободить дисковое пространство.

**Взаимосвязи с другими частями проекта:**

* Код взаимодействует с `tinytroupe`, но, скорее всего, не directly использует структуры данных или логику из этого пакета. Зависимость возникает, если пакеты используют файлы .ipynb в `tinytroupe`.

**Рекомендации:**

* Вместо `sys.path.insert` используйте установленные зависимости для `tinytroupe` в `requirements.txt`, тогда импорт будет работать правильно в любой ситуации, а не только с `sys.path.insert`.
* Добавьте assert statements в `test_notebook_execution` для более надежного тестирования, например, проверьте, что `notebook` содержит ожидаемые результаты.
* Добавьте `logging` для более подробного вывода о ходе выполнения теста.