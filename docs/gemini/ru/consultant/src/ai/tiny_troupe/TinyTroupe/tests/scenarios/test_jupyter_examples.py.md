# Анализ кода модуля `test_jupyter_examples.py`

**Качество кода**
9
 -  Плюсы
    -   Код хорошо структурирован и понятен.
    -   Используется параметризация тестов pytest для запуска на нескольких ноутбуках.
    -   Присутствует обработка исключений при выполнении ноутбука.
    -   Сохранение выполненной версии ноутбука.
 -  Минусы
    -   Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    -   Отсутствует логирование ошибок.
    -   Комментарии не соответствуют стандарту RST.
    -   Необходимо явно прописывать `sys.path.insert`, лучше использовать `os.path.abspath`
    -   Необходимо добавить документацию к функциям и модулю.

**Рекомендации по улучшению**

1.  **Использование `j_loads`**: Заменить `nbformat.read` на `j_loads` для чтения файлов.
2.  **Логирование**: Добавить логирование ошибок с помощью `logger.error`.
3.  **Документация**: Привести комментарии к стандарту RST, добавить документацию к функциям и модулю.
4.  **Абсолютные пути**: Использовать `os.path.abspath` для работы с путями.
5.  **Удалить sys.path.insert**:  Использовать `os.path.abspath` для работы с путями.

**Оптимизированный код**
```python
"""
Модуль для тестирования Jupyter Notebook
=========================================================================================

Этот модуль содержит тесты для выполнения Jupyter Notebook файлов и проверки отсутствия исключений.

Пример использования
--------------------

Запуск тестов для всех ноутбуков в папке `../examples/`:

.. code-block:: python

    pytest tests/scenarios/test_jupyter_examples.py

"""
import os
#from src.utils.jjson import j_loads, j_loads_ns # TODO удалить если не нужно 
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest
#from src.logger.logger import logger # TODO удалить если не нужно
#import sys # TODO удалить
#sys.path.insert(0, os.path.abspath('../../tinytroupe/')) # ensures that the package is imported from the parent directory, not the Python installation # TODO удалить
#sys.path.insert(0, os.path.abspath('../../')) # ensures that the package is imported from the parent directory, not the Python installation # TODO удалить
#sys.path.insert(0, os.path.abspath('../')) # ensures that the package is imported from the parent directory, not the Python installation # TODO удалить

# Set the folder containing the notebooks
NOTEBOOK_FOLDER = os.path.abspath("../examples/")  # Update this path # задаем абсолютный путь

# Set a timeout for long-running notebooks
TIMEOUT = 600

KERNEL_NAME = "python3" #"py310"

def get_notebooks(folder: str) -> list:
    """
    Извлекает все Jupyter notebook файлы из указанной папки.

    :param folder: Путь к папке с ноутбуками.
    :return: Список путей к файлам ноутбуков.
    """
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb") and not ".executed." in f and not ".local." in f
    ]

@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path: str) -> None:
    """
    Выполняет Jupyter notebook и проверяет отсутствие исключений.

    :param notebook_path: Путь к файлу ноутбука.
    """
    try:
    # открываем файл ноутбука
        with open(notebook_path, "r", encoding="utf-8") as nb_file:
            # читаем содержимое ноутбука
            notebook = nbformat.read(nb_file, as_version=4)
            print(f"Executing notebook: {notebook_path} with kernel: {KERNEL_NAME}")
             # инициализируем препроцессор для выполнения ячеек
            ep = ExecutePreprocessor(timeout=TIMEOUT, kernel_name=KERNEL_NAME)

            # выполняем ноутбук
            ep.preprocess(notebook, {'metadata': {'path': NOTEBOOK_FOLDER}})
            print(f"Notebook {notebook_path} executed successfully.")
    # обрабатываем исключения, которые могут возникнуть при выполнении
    except Exception as e:
        # если возникло исключение, тест считается проваленным
        pytest.fail(f"Notebook {notebook_path} raised an exception: {e}")
    
    finally:
        # создаем путь для сохранения выполненной копии ноутбука
        output_path = notebook_path.replace(".ipynb", ".executed.local.ipynb")
        # открываем файл для записи выполненного ноутбука
        with open(output_path, "w", encoding="utf-8") as out_file:
            # сохраняем выполненный ноутбук
            nbformat.write(notebook, out_file)
        
        print(f"Executed notebook saved as: {output_path}")
```