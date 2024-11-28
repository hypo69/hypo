Как использовать этот блок кода
=========================================================================================\n\nОписание
-------------------------
Данный код содержит тест `test_generate_person`, который проверяет генерацию персонажа с использованием `TinyPersonFactory`.  Он определяет спецификацию персонажа ("banker_spec"), создает фабрику `TinyPersonFactory` на основе этой спецификации, генерирует персонажа и проверяет, что сгенерированная краткая биография (`minibio`) соответствует заданному шаблону с помощью `proposition_holds`.

Шаги выполнения
-------------------------
1. Импортируются необходимые модули, включая `TinyPersonFactory` из `tinytroupe.factory`, `Simulation` и `create_oscar_the_architect` из `tinytroupe.examples`, а также вспомогательную функцию `proposition_holds` из `testing_utils`. Пути к модулям корректируются, добавляя в `sys.path` необходимые директории.
2. Определяется строковая спецификация `banker_spec` для персонажа, описывающая его роль и квалификацию.
3. Создается экземпляр фабрики `banker_factory` класса `TinyPersonFactory` с переданной спецификацией.
4. Генерируется персонаж (`banker`) с помощью метода `generate_person()` фабрики.
5. Получается краткая биография персонажа (`minibio`) с помощью метода `minibio()`.
6. Используется функция `proposition_holds` для проверки того, что сгенерированная биография (`minibio`) соответствует ожидаемому шаблону, связанному с банковской деятельностью.  Возвращаемое значение сравнивается с ожидаемой строкой для валидации.  Если проверка не пройдёт, то выдается сообщение об ошибке с пояснением, что утверждение не верно.

Пример использования
-------------------------
.. code-block:: python

    import pytest
    import os
    import sys
    sys.path.append('path/to/tinytroupe/')  # Замените на реальный путь
    sys.path.append('path/to/your/project/') # Замените на реальный путь

    from tinytroupe.examples import create_oscar_the_architect
    from tinytroupe.control import Simulation
    import tinytroupe.control as control
    from tinytroupe.factory import TinyPersonFactory
    from testing_utils import proposition_holds

    def test_generate_person(setup):
        banker_spec = """
            A vice-president of one of the largest brazillian banks. Has a degree in engineering and an MBA in finance. 
            Is facing a lot of pressure from the board of directors to fight off the competition from the fintechs.    
        """

        banker_factory = TinyPersonFactory(banker_spec)
        banker = banker_factory.generate_person()
        minibio = banker.minibio()

        assert proposition_holds(f"The following is an acceptable short description for someone working in banking: '{minibio}'"), f"Proposition is false according to the LLM."