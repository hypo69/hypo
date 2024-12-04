Как использовать класс ABRandomizer
========================================================================================

Описание
-------------------------
Класс `ABRandomizer` предназначен для случайной перестановки двух вариантов (например, A и B) и последующего возвращения исходных значений.  Он хранит результаты рандомизации для последующего дерандомизации. Класс позволяет задавать реальные имена вариантов, имена вариантов для пользователя (скрытые) и имена, которые не подлежат случайной перестановке.

Шаги выполнения
-------------------------
1. **Инициализация:** Создается экземпляр класса `ABRandomizer` с параметрами:
    - `real_name_1`:  реальное имя первого варианта.
    - `real_name_2`: реальное имя второго варианта.
    - `blind_name_a`: имя первого варианта для пользователя (скрытое).
    - `blind_name_b`: имя второго варианта для пользователя (скрытое).
    - `passtrough_name`: список имен, которые не должны быть переставлены.
    - `random_seed`:  значение для инициализации генератора случайных чисел (для воспроизводимости).
2. **Рандомизация:** Метод `randomize(i, a, b)` переставляет варианты `a` и `b` для элемента с индексом `i` с использованием заданного `random_seed`. Результаты перестановки хранятся во внутреннем словаре `choices`.  Возвращаются переставленные значения `a` и `b`.
3. **Дерандомизация:** Метод `derandomize(i, a, b)` восстанавливает исходный порядок вариантов `a` и `b` для элемента `i` на основе сохранённых данных в `choices`.  Возвращает исходные варианты.
4. **Декодирование выбора пользователя:** Метод `derandomize_name(i, blind_name)` определяет, был ли вариант `blind_name` для элемента с индексом `i` изменен в ходе рандомизации. Если да, то возвращается соответствующий вариант из `real_name_1` или `real_name_2`; иначе возвращает исходный `blind_name`.

Пример использования
-------------------------
.. code-block:: python

    import random
    import pandas as pd
    from tinytroupe.agent import TinyPerson

    # Инициализация класса
    randomizer = ABRandomizer(real_name_1="control", real_name_2="treatment",
                               blind_name_a="A", blind_name_b="B",
                               passtrough_name=["control"],
                               random_seed=42)

    # Предполагаемый DataFrame
    data = {'item': [1, 2, 3], 'option': ["A", "B", "control"]}
    df = pd.DataFrame(data)


    # Рандомизация
    for i, row in df.iterrows():
        item = row['item']
        option = row['option']
        a, b = randomizer.randomize(item, 'control', 'treatment')
        print(f'Item {item}, Original: {option}, Randomized: {a if option == "A" else b}')

    # Дерандомизация
    for i, row in df.iterrows():
        item = row['item']
        blind_name = 'A'
        real_name = randomizer.derandomize_name(item, blind_name)
        print(f"Item {item}, choice was {blind_name}, real name is {real_name}")