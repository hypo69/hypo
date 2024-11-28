Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предоставляет примеры создания агентов (TinyPerson) с определенными характеристиками, включая возраст, национальность, профессию, рутину, описание профессии, личностные черты, профессиональные и личные интересы, навыки и отношения.  Функции `create_oscar_the_architect()`, `create_lisa_the_data_scientist()`, `create_marcos_the_physician()`, и `create_lila_the_linguist()` демонстрируют, как создавать таких агентов, заполняя различные атрибуты.


Шаги выполнения
-------------------------
1. **Импортирование класса:**  Импортируется класс `TinyPerson` из модуля `tinytroupe.agent`.

2. **Определение агента:** Функции `create_oscar_the_architect()`, `create_lisa_the_data_scientist()`, `create_marcos_the_physician()` и `create_lila_the_linguist()` определяют и конфигурируют агентов.

3. **Использование методов `define`, `define_several`:** Эти методы используются для задания различных характеристик агента:
    - `define("атрибут", "значение")`: для задания единичных атрибутов (например, `age`, `nationality`).
    - `define_several("атрибут", [{"ключ":"значение"}, ...])`: для задания нескольких значений одного атрибута (например, `personality_traits`, `skills`).


4. **Возврат объекта:** Каждая функция возвращает созданный объект `TinyPerson`.


Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.agent import TinyPerson
    from hypotez.src.ai.tiny_troupe.TinyTroupe.tinytroupe.examples import create_oscar_the_architect

    # Создание агента "Oscar, the architect"
    oscar = create_oscar_the_architect()

    # Вывод некоторых характеристик агента (пример)
    print(f"Имя: {oscar.name}")
    print(f"Возраст: {oscar.age}")
    print(f"Профессия: {oscar.occupation}")
    print(f"Описание профессии:\n{oscar.occupation_description}")