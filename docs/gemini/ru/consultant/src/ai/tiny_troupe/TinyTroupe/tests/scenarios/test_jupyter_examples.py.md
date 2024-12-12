# Анализ кода модуля `test_jupyter_examples.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован и читаем.
    -   Используется параметризация тестов для запуска на нескольких ноутбуках.
    -   Обработка исключений при выполнении ноутбука.
    -   Сохранение выполненной копии ноутбука.
    -   Используются относительные импорты для доступа к модулям пакета.

-   Минусы
    -   Отсутствует документация в формате reStructuredText (RST).
    -   Используется `print` для логирования, лучше использовать `logger`.
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**
1. Добавить документацию в формате RST для модуля и функций.
2. Заменить `print` на `logger` для логирования.
3. Использовать `j_loads` или `j_loads_ns` для чтения файлов.
4. Добавить обработку ошибок с использованием `logger.error`.
5. Убрать лишние `sys.path.insert(0, ...)` так как они дублируют друг друга.

**Оптимизированный код**
```python
"""
Модуль для тестирования Jupyter Notebook
=========================================================================================

Этот модуль содержит функции для тестирования выполнения Jupyter Notebook файлов.
Он использует `pytest` для запуска тестов и `nbformat` и `nbconvert` для работы с ноутбуками.

Пример использования
--------------------

Пример использования:
    
    pytest tests/scenarios/test_jupyter_examples.py

Этот код запускает все тесты, определенные в данном модуле.
"""
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest
# from src.utils.jjson import j_loads  # TODO: пока не используется
from src.logger.logger import logger  # подключаем logger
import sys

# Ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '../../')
sys.path.insert(0, '..') 

# Set the folder containing the notebooks
NOTEBOOK_FOLDER = "../examples/"  # Update this path

# Set a timeout for long-running notebooks
TIMEOUT = 600

KERNEL_NAME = "python3"


def get_notebooks(folder: str) -> list:
    """
    Извлекает все Jupyter notebook файлы из указанной папки.

    :param folder: Путь к папке с ноутбуками.
    :return: Список путей к файлам ноутбуков.
    """
    # код получает список файлов в указанной папке и фильтрует их, оставляя только те, что заканчиваются на .ipynb
    # и не содержат в названии .executed. или .local.
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb") and not ".executed." in f and not ".local." in f
    ]


@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path: str):
    """
    Выполняет Jupyter notebook и проверяет отсутствие ошибок.

    :param notebook_path: Путь к файлу ноутбука.
    """
    # Код открывает файл ноутбука для чтения
    try:
        with open(notebook_path, "r", encoding="utf-8") as nb_file:
            # код читает содержимое файла и преобразует в объект Notebook
            notebook = nbformat.read(nb_file, as_version=4)
            # код выводит сообщение о начале выполнения ноутбука
            logger.info(f"Executing notebook: {notebook_path} with kernel: {KERNEL_NAME}")
            # код инициализирует препроцессор для выполнения ноутбука
            ep = ExecutePreprocessor(timeout=TIMEOUT, kernel_name=KERNEL_NAME)
    except Exception as ex:
        logger.error(f'Ошибка при открытии файла {notebook_path=}', exc_info=True) # TODO: исправить формат ex
        pytest.fail(f"Ошибка при открытии файла {notebook_path}: {ex}")
        return

    try:
        # код запускает выполнение ноутбука
        ep.preprocess(notebook, {'metadata': {'path': NOTEBOOK_FOLDER}})
        # код выводит сообщение об успешном выполнении
        logger.info(f"Notebook {notebook_path} executed successfully.")

    except Exception as e:
        # код перехватывает ошибки во время выполнения
        logger.error(f"Notebook {notebook_path} raised an exception: {e}", exc_info=True) # TODO: исправить формат e
        # код сообщает об ошибке
        pytest.fail(f"Notebook {notebook_path} raised an exception: {e}")

    finally:
        # код формирует путь для сохранения выполненного ноутбука
        output_path = notebook_path.replace(".ipynb", ".executed.local.ipynb")
        # Код открывает файл для записи выполненного ноутбука
        try:
            with open(output_path, "w", encoding="utf-8") as out_file:
                # код сохраняет выполненный ноутбук
                nbformat.write(notebook, out_file)
                # код выводит сообщение о сохранении
            logger.info(f"Executed notebook saved as: {output_path}")
        except Exception as ex:
            logger.error(f'Ошибка при сохранении файла {output_path=}', exc_info=True)  # TODO: исправить формат ex
            pytest.fail(f"Ошибка при сохранении файла {output_path}: {ex}")
```