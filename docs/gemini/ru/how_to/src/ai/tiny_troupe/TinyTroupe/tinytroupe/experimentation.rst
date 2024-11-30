Как использовать класс ABRandomizer
========================================================================================

Описание
-------------------------
Класс `ABRandomizer` предназначен для рандомизации выбора между двумя вариантами (например, A и B) и последующего разворота этой рандомизации.  Он хранит информацию о рандомизации для каждого элемента в словаре `self.choices`.  Класс позволяет задать имена вариантов в реальном и замаскированном виде, а также имена элементов, которые не должны подвергаться рандомизации.

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `ABRandomizer`, передавая необходимые параметры:
    - `real_name_1`: Имя первого варианта в исходных данных.
    - `real_name_2`: Имя второго варианта в исходных данных.
    - `blind_name_a`: Имя первого варианта, используемое в отображении для пользователя.
    - `blind_name_b`: Имя второго варианта, используемое в отображении для пользователя.
    - `passtrough_name`: Список имен, которые не должны подвергаться рандомизации (возвращаются как есть).
    - `random_seed`: Число для задания зерна генератора случайных чисел (для воспроизводимости).

2. **Рандомизация:** Вызовите метод `randomize(i, a, b)` для рандомизации выбора между вариантами `a` и `b` для элемента `i`. Метод запишет информацию о рандомизации для элемента `i` в `self.choices`.

3. **Дерандомизация:** Вызовите метод `derandomize(i, a, b)` для возврата исходного выбора для элемента `i` на основе сохраненной информации о рандомизации.

4. **Получение дерандомизированного имени:** Вызовите метод `derandomize_name(i, blind_name)` для определения реального имени, соответствующего выбранному пользователю имени `blind_name` для элемента `i`.

Пример использования
-------------------------
.. code-block:: python

    import random
    import pandas as pd
    from tinytroupe.agent import TinyPerson
    from tinytroupe.experimentation import ABRandomizer

    # Инициализация класса
    randomizer = ABRandomizer(real_name_1="control", real_name_2="treatment",
                               blind_name_a="A", blind_name_b="B",
                               passtrough_name=["skip"])

    # Рандомизация
    item_index = 0
    choice_a = "value_a"
    choice_b = "value_b"
    a, b = randomizer.randomize(item_index, choice_a, choice_b)

    # Предположим, пользователь выбрал 'A'
    user_choice = "A"

    # Получение реального имени
    real_name = randomizer.derandomize_name(item_index, user_choice)
    print(f"Real name for item {item_index}: {real_name}")

    # Пример с нерандомизированным элементом
    user_choice = "skip"
    real_name = randomizer.derandomize_name(item_index, user_choice)
    print(f"Real name for item {item_index} (passtrough): {real_name}")