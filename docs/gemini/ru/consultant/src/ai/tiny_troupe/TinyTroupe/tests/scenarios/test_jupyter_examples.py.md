# Анализ кода модуля `test_jupyter_examples.py`

**Качество кода**
7
-   Плюсы
    -   Код структурирован, разбит на функции.
    -   Используется параметризация тестов pytest.
    -   Присутствует обработка исключений при выполнении ноутбуков.
    -   Сохранение копии выполненного ноутбука.
-   Минусы
    -   Отсутствует reStructuredText документация.
    -   Используется `print` для логирования, лучше использовать `logger`.
    -   Пути импорта не соответствуют стандарту проекта.
    -   Не используется `j_loads` для чтения файлов.
    -   Жестко заданные значения `TIMEOUT` и `KERNEL_NAME`.
    -   Общий `try-except` блок.

**Рекомендации по улучшению**

1.  Добавить reStructuredText документацию для модуля, функций.
2.  Заменить `print` на логирование с использованием `logger` из `src.logger.logger`.
3.  Уточнить пути импорта и использовать абсолютные пути.
4.  Использовать `j_loads` для чтения файлов ноутбуков.
5.  Перенести `TIMEOUT` и `KERNEL_NAME` в переменные окружения или конфигурационный файл.
6.  Разделить `try-except` блок на более конкретные блоки, логировать ошибки с помощью `logger.error`.
7.  Добавить проверку на наличие директории перед ее использованием.
8.  Использовать f-строки для форматирования логов.

**Оптимизированный код**

```python
"""
Модуль для тестирования выполнения Jupyter Notebook.
=========================================================================================

Этот модуль содержит функции для поиска и выполнения Jupyter Notebooks
и проверки их на отсутствие ошибок.

Пример использования
--------------------

.. code-block:: python

    pytest test_jupyter_examples.py
"""
import os
# from src.utils.jjson import j_loads # убрал, так как json не используется
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest
from src.logger.logger import logger # подключаем логер

import sys
sys.path.insert(0, 'src/ai/tiny_troupe/TinyTroupe/') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, 'src/') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, 'src/ai/tiny_troupe/') # ensures that the package is imported from the parent directory, not the Python installation

# Set the folder containing the notebooks
NOTEBOOK_FOLDER = "examples"  # Update this path
if not os.path.exists(NOTEBOOK_FOLDER):
    logger.error(f"Директория '{NOTEBOOK_FOLDER}' не найдена.")
    raise FileNotFoundError(f"Директория '{NOTEBOOK_FOLDER}' не найдена.")
# Set a timeout for long-running notebooks
TIMEOUT = 600

KERNEL_NAME = "python3" #"py310"


def get_notebooks(folder: str) -> list[str]:
    """
    Извлекает все файлы Jupyter notebook из указанной папки.

    :param folder: Путь к папке с ноутбуками.
    :return: Список путей к файлам ноутбуков.
    """
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".ipynb") and not ".executed." in f and not ".local." in f
    ]


@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path: str):
    """
    Выполняет Jupyter notebook и проверяет, что не возникает исключений.

    :param notebook_path: Путь к файлу ноутбука.
    """
    try:
        # открываем файл с ноутбуком
        with open(notebook_path, "r", encoding="utf-8") as nb_file:
            # Читаем содержимое файла
            notebook = nbformat.read(nb_file, as_version=4)
        logger.info(f"Выполнение ноутбука: {notebook_path} с ядром: {KERNEL_NAME}")
        # инициализируем препроцессор
        ep = ExecutePreprocessor(timeout=TIMEOUT, kernel_name=KERNEL_NAME)

        # Выполняем notebook
        ep.preprocess(notebook, {'metadata': {'path': NOTEBOOK_FOLDER}})
        logger.info(f"Ноутбук {notebook_path} выполнен успешно.")

    except Exception as e:
        logger.error(f"Ноутбук {notebook_path} вызвал исключение: {e}")
        pytest.fail(f"Ноутбук {notebook_path} вызвал исключение: {e}")

    finally:
        # сохраняем копию выполненного ноутбука
        output_path = notebook_path.replace(".ipynb", ".executed.local.ipynb")
        try:
            with open(output_path, "w", encoding="utf-8") as out_file:
                nbformat.write(notebook, out_file)
            logger.info(f"Выполненный ноутбук сохранен как: {output_path}")
        except Exception as e:
           logger.error(f"Не удалось сохранить выполненный ноутбук: {output_path}, ошибка: {e}")
```