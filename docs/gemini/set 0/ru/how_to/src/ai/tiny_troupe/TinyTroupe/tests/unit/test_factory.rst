Как использовать этот блок кода
=========================================================================================\n\nОписание
-------------------------
Данный код проверяет корректность генерации объекта `TinyPerson` с помощью фабрики `TinyPersonFactory`. Он задаёт спецификацию для персонажа - "банкира", описывающего его должность, образование и текущие проблемы. Затем, код генерирует персонажа, выводит его мини-биографию и проверяет, соответствует ли она заданному описанию с помощью функции `proposition_holds`.

Шаги выполнения
-------------------------
1. Импортируются необходимые модули, в том числе `TinyPersonFactory` для создания персонажа, `Simulation`, `control`, а также вспомогательная функция `proposition_holds` для проверки утверждения.
2. Определяется строковая переменная `banker_spec`, содержащая описание персонажа (банкира).
3. Создаётся экземпляр фабрики `TinyPersonFactory` с предоставленной спецификацией.
4. Генерируется объект `banker` с помощью метода `generate_person()` фабрики.
5. Получается мини-биография `banker` с помощью метода `minibio()`.
6. Используется функция `proposition_holds` для проверки, соответствует ли сгенерированная мини-биография описанию в `banker_spec`.
7. В случае, если проверка не пройдёт, генерируется сообщение об ошибке.

Пример использования
-------------------------
.. code-block:: python

    import pytest
    import os
    import sys
    sys.path.append('../../tinytroupe/')
    sys.path.append('../../')
    sys.path.append('..')
    
    from tinytroupe.examples import create_oscar_the_architect
    from tinytroupe.control import Simulation
    import tinytroupe.control as control
    from tinytroupe.factory import TinyPersonFactory
    from testing_utils import *

    def test_generate_person(setup):
        banker_spec ="""
        A vice-president of one of the largest brazillian banks. Has a degree in engineering and an MBA in finance. 
        Is facing a lot of pressure from the board of directors to fight off the competition from the fintechs.    
        """

        banker_factory = TinyPersonFactory(banker_spec)

        banker = banker_factory.generate_person()

        minibio = banker.minibio()

        assert proposition_holds(f"The following is an acceptable short description for someone working in banking: \'{minibio}\'"), f"Proposition is false according to the LLM."