Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предназначен для автоматического выполнения Jupyter notebooks. Он проходит по списку Jupyter notebooks в заданной папке, выполняет их и сохраняет результаты.  Код обрабатывает потенциальные исключения во время выполнения, сохраняя копию каждого выполненного блокнота с добавленным постфиксом ".executed.local".  Он важен для тестирования и автоматизации работы с Jupyter notebooks.


Шаги выполнения
-------------------------
1. **Импортирует необходимые библиотеки:** `os`, `nbformat`, `ExecutePreprocessor` из `nbconvert`, `pytest`.  Также подключает необходимые пути для импорта пакета TinyTroupe.

2. **Определяет константы:**
    - `NOTEBOOK_FOLDER`: Путь к папке, содержащей Jupyter notebooks.  **Необходимо обновить** в коде.
    - `TIMEOUT`: Время ожидания выполнения notebook.
    - `KERNEL_NAME`: Имя ядра Jupyter, которое будет использоваться для выполнения.

3. **Функция `get_notebooks`:** Находит все файлы Jupyter notebook в заданной папке и возвращает список путей к ним, исключая те, которые уже были обработаны (имеют постфикс ".executed." или ".local.").

4. **Декоратор `@pytest.mark.parametrize`:**
    - Используется для выполнения `test_notebook_execution` функции для каждого notebook, полученного из `get_notebooks`.

5. **Функция `test_notebook_execution`:**
    - Открывает каждый Jupyter notebook.
    - Выводит сообщение об обработке.
    - Создаёт экземпляр `ExecutePreprocessor`, устанавливая `timeout` и `kernel_name`.
    - **Обрабатывает исключения:** Если при выполнении notebook возникает исключение, то функция `pytest.fail` останавливает тест и сообщает об ошибке.
    - **Сохраняет выполненный notebook:** Создаёт копию выполненного notebook с постфиксом `.executed.local`.

6. **Завершение:** Выводит сообщение об успешном выполнении или ошибке и сохраняет результат.


Пример использования
-------------------------
.. code-block:: python

    import os
    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor
    import pytest
    
    import sys
    sys.path.insert(0, '../../tinytroupe/')
    sys.path.insert(0, '../../')
    sys.path.insert(0, '..')

    # Set the folder containing the notebooks -  UPDATE THIS!
    NOTEBOOK_FOLDER = "../examples/" 

    TIMEOUT = 600
    KERNEL_NAME = "python3"

    def get_notebooks(folder):
        # ... (функция get_notebooks из примера)

    @pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))
    def test_notebook_execution(notebook_path):
        # ... (функция test_notebook_execution из примера)