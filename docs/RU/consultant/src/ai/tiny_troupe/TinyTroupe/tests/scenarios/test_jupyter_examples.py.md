# Анализ кода модуля `test_jupyter_examples.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и читабелен.
    - Используются параметризованные тесты pytest для проверки нескольких ноутбуков.
    - Присутствует логирование начала и завершения выполнения ноутбука.
    - Сохраняется копия выполненного ноутбука.
 -  Минусы
    - Отсутствует обработка ошибок с использованием `logger.error`.
    - Присутствуют избыточные импорты sys.path.
    - Нет документации в формате RST.
    - Жестко заданы пути.
    - Присутствует использование `print` вместо `logger`.
    - Не используются константы для путей.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате RST.
2.  Использовать `from src.logger.logger import logger` для логирования.
3.  Заменить `print` на `logger.info` и `logger.error`.
4.  Добавить документацию для функций в формате RST.
5.  Удалить лишние `sys.path.insert(0, ...)` так как это дублирует пути.
6.  Добавить константы для путей.
7.  Использовать константу для расширений файлов.
8.  Заменить `Exception as e` на конкретный тип исключения при обработке.
9.  Вынести константу KERNEL_NAME из глобальной области видимости в функцию.
10. Улучшить читаемость и форматирование кода.

**Оптимизированный код**

```python
"""
Модуль для тестирования выполнения Jupyter Notebook.
=====================================================

Этот модуль содержит функции для автоматического тестирования выполнения примеров Jupyter Notebook.
Он использует pytest для параметризации тестов и nbconvert для выполнения кода в ноутбуках.

Пример использования
--------------------

Для запуска тестов необходимо установить pytest и nbconvert, а затем выполнить:

.. code-block:: bash

   pytest tests/scenarios/test_jupyter_examples.py

"""
import os
from pathlib import Path

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest

from src.logger.logger import logger  #  Импорт logger


# Определение констант для путей и расширений файлов
NOTEBOOK_FOLDER = Path("../examples/")
EXECUTED_NOTEBOOK_SUFFIX = ".executed.local.ipynb"
NOTEBOOK_EXTENSION = ".ipynb"


def get_notebooks(folder: Path) -> list[str]:
    """
    Извлекает все файлы Jupyter Notebook из указанной папки, исключая уже выполненные и локальные копии.

    Args:
        folder (Path): Путь к папке с ноутбуками.

    Returns:
        list[str]: Список путей к найденным файлам ноутбуков.
    """
    # код возвращает список всех файлов в указанной папке, которые имеют расширение .ipynb, но не содержат ".executed." или ".local." в своем имени.
    return [
        str(folder / f)
        for f in os.listdir(folder)
        if f.endswith(NOTEBOOK_EXTENSION)
        and not ".executed." in f
        and not ".local." in f
    ]


@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
def test_notebook_execution(notebook_path: str):
    """
    Выполняет Jupyter Notebook и проверяет отсутствие ошибок.

    Args:
        notebook_path (str): Путь к файлу ноутбука.

    Raises:
        pytest.fail: Если во время выполнения ноутбука возникает исключение.
    """
    kernel_name = "python3" #  Определение переменной kernel_name
    # код открывает файл ноутбука для чтения, используя кодировку utf-8.
    with open(notebook_path, "r", encoding="utf-8") as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)
        logger.info(f"Выполнение ноутбука: {notebook_path} с ядром: {kernel_name}") #  Логирование начала выполнения ноутбука.
        ep = ExecutePreprocessor(timeout=600, kernel_name=kernel_name) #  Инициализация препроцессора для выполнения ячеек ноутбука.

        try:
            #  Код выполняет предобработку ноутбука
            ep.preprocess(notebook, {"metadata": {"path": str(NOTEBOOK_FOLDER)}})
            logger.info(f"Ноутбук {notebook_path} успешно выполнен.") #  Логирование успешного выполнения.

        except Exception as e:
            #  Код логирует ошибку при выполнении и вызывает pytest.fail
            logger.error(f"Ноутбук {notebook_path} вызвал исключение: {e}") #  Логирование ошибки.
            pytest.fail(f"Ноутбук {notebook_path} вызвал исключение: {e}")

        finally:
             #  Код сохраняет копию выполненного ноутбука
            output_path = notebook_path.replace(
                NOTEBOOK_EXTENSION, EXECUTED_NOTEBOOK_SUFFIX
            )
            with open(output_path, "w", encoding="utf-8") as out_file:
                nbformat.write(notebook, out_file)
            logger.info(f"Выполненный ноутбук сохранен как: {output_path}")  #  Логирование сохранения.
```