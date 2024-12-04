Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит тесты для класса `ABRandomizer`, который реализует алгоритм случайной выборки (рандомизации) для A/B тестирования.  Тесты проверяют корректность методов `randomize`, `derandomize` и `derandomize_name` класса.  Включают также проверку  наличия функции `passtrough_name`.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек**: Код импортирует библиотеку `pytest`, изменяет пути поиска модулей (`sys.path.append`) и импортирует вспомогательные функции из `testing_utils` и класс `ABRandomizer` из модуля `tinytroupe.experimentation`.

2. **Функция `test_randomize`**: Создает экземпляр `ABRandomizer`, многократно вызывает метод `randomize` для разных входных данных (i, "option1", "option2"). Проверяет, что полученные пары ("option1", "option2") или ("option2", "option1") соответствуют значениям в `randomizer.choices`. Обрабатывает случай, когда рандомизация не выполняется, вызывая исключение.

3. **Функция `test_derandomize`**:  Создает экземпляр `ABRandomizer`, многократно вызывает метод `randomize` и затем `derandomize` для каждого результата рандомизации. Проверяет, что восстановленные значения соответствуют исходным.

4. **Функция `test_derandomize_name`**:  Аналогично предыдущей функции, но тестирует метод `derandomize_name`, который возвращает имя варианта (control или treatment) на основе результата рандомизации.

5. **Функция `test_passtrough_name`**: Тестирует обработку списка `passtrough_name` в конструкторе `ABRandomizer`. Создается экземпляр с опцией `passtrough_name=["option3"]`.  Вызывается `randomize`,  и `derandomize_name` для значения "option3". Проверяет, что имя "option3" возвращается корректно.

6. **Функция `test_intervention_1`**:  Это "заглушка" (TODO), пока что не реализованная функция тестирования.


Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.experimentation import ABRandomizer

    # Создание объекта рандомизатора
    randomizer = ABRandomizer()

    # Рандомизация для конкретного элемента
    i = 10
    option1 = "Вариант 1"
    option2 = "Вариант 2"
    a, b = randomizer.randomize(i, option1, option2)

    # Восстановление исходных значений
    c, d = randomizer.derandomize(i, a, b)

    # Получение имени варианта
    real_name = randomizer.derandomize_name(i, a)


    # Пример использования passtrough_name
    randomizer_passtrough = ABRandomizer(passtrough_name=["option3"])
    random_name = randomizer_passtrough.derandomize_name(0, "option3")