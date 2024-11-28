Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит тесты для валидации персон, созданных в рамках проекта TinyTroupe. Он проверяет, насколько хорошо сгенерированные персоны соответствуют заданным ожиданиям.  Функция `test_validate_person` выполняет валидацию для двух разных персон (банкира и монаха) с использованием разных ожиданий. Она проверяет, что баллы валидации корректны для соответствующих ожиданий.

Шаги выполнения
-------------------------
1. **Импортирует необходимые модули:**  Импортируются модули `pytest`, `os`, `sys`, `Simulation`, `TinyPersonFactory`, `TinyPersonValidator`, и другие необходимые для работы с проектом TinyTroupe.

2. **Настраивает пути к модулям:** Функция `sys.path.append` добавляет пути к директориям, содержащим нужные модули, к списку модулей Python, чтобы интерпретатор мог их найти.

3. **Создает фабрики персон:** Создаются фабрики персон `banker_factory` и `monk_spec_factory` для генерации персон банка и монаха соответственно.

4. **Создает персон:** Используя фабрики, генерируются персоны `banker` и `monk`.

5. **Формулирует ожидания:** Формулируются ожидания `banker_expectations` и `monk_expectations`, описывающие характеристики каждого типа персоны.

6. **Выполняет валидацию:** Вызывается функция `TinyPersonValidator.validate_person` для валидации созданных персон на основе заданных ожиданий. Функция возвращает балл валидации и обоснование.

7. **Проверяет баллы валидации:** Проверяется, что баллы валидации соответствуют ожиданиям. Для банкира ожидается высокий балл, для монаха - высокий балл, для монаха с неправильными ожиданиями (ожидания банкира) - низкий балл.


Пример использования
-------------------------
.. code-block:: python

    import pytest
    import os
    import sys
    sys.path.append('path/to/your/tinytroupe') #Замените на фактический путь
    from tinytroupe.examples import create_oscar_the_architect
    from tinytroupe.control import Simulation
    import tinytroupe.control as control
    from tinytroupe.factory import TinyPersonFactory
    from tinytroupe.validation import TinyPersonValidator
    from testing_utils import *

    # пример ожиданий (замените на ваши ожидания)
    banker_expectations = "A vice-president of a bank..."
    monk_expectations = "A poor buddhist monk..."


    # пример создания персоны и валидации
    banker_factory = TinyPersonFactory(banker_spec)
    banker = banker_factory.generate_person()
    banker_score, banker_justification = TinyPersonValidator.validate_person(banker, expectations=banker_expectations, include_agent_spec=False, max_content_length=None)
    print(f"Banker score: {banker_score}, Justification: {banker_justification}")


    # не забудьте импортировать необходимые модули и функции из testing_utils
    # и заменить 'path/to/your/tinytroupe' на фактический путь до папки tinytroupe.