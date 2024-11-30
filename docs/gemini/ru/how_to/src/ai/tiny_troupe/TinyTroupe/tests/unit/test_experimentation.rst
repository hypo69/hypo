Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный код содержит тесты для класса `ABRandomizer`, который реализует алгоритм рандомизации для A/B-тестирования.  Тесты проверяют корректность работы методов `randomize`, `derandomize`, `derandomize_name` и `passtrough_name`. Функции `test_randomize`, `test_derandomize`, `test_derandomize_name`, и `test_passtrough_name`  содержат циклы для проверки работы алгоритма на большом количестве данных.

Шаги выполнения
-------------------------
1. **Импорт необходимых библиотек:** Код импортирует `pytest`, `sys` для управления путями, `testing_utils` (предполагается, что содержит вспомогательные функции), и `ABRandomizer` из модуля `experimentation`.
2. **Инициализация рандомизатора:** Создается экземпляр класса `ABRandomizer`.
3. **Проверка метода `randomize`:**  Функция `test_randomize` вызывает `randomize` с разными входными данными и проверяет, что возвращаемые пары значений ("option1", "option2")  соответствуют выбранным вариантам в `randomizer.choices`.
4. **Проверка метода `derandomize`:** Функция `test_derandomize`  вызывает `randomize` и `derandomize`, сравнивая результат с первоначальными значениями.
5. **Проверка метода `derandomize_name`:** Функция `test_derandomize_name` проверяет, что метод возвращает корректное название варианта (control или treatment).
6. **Проверка метода `passtrough_name`:** Функция `test_passtrough_name` проверяет, что метод `derandomize_name` правильно обрабатывает значения, заданные в `passtrough_name`.

Пример использования
-------------------------
.. code-block:: python

    import sys
    sys.path.append('path/to/tinytroupe')  # Замените на реальный путь
    from tinytroupe.experimentation import ABRandomizer

    randomizer = ABRandomizer(passtrough_name=["option3"])
    a, b = randomizer.randomize(0, "option1", "option2")
    real_name = randomizer.derandomize_name(0, "option3")
    print(f"Результат: {real_name}")