# Анализ кода модуля TEMPCONVERTOR

**Качество кода**
*   Соответствие требованиям к формату кода (1-10): 7
    *   **Преимущества:**
        *   Код хорошо структурирован и разделен на логические блоки (функции конвертации, универсальная функция, функция main).
        *   Используются аннотации типов и docstring для функций.
        *   Логика конвертации температуры корректна.
        *   Имеется обработка исключений в функции `main`.
        *   Используется `dataclass` для более структурированного подхода во втором файле.
    *   **Недостатки:**
        *   Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        *   Нет единого импорта логгера `from src.logger.logger import logger`.
        *   Отсутствуют reStructuredText (RST) комментарии.
        *   Имеется избыточное использование `try-except` в функции `main`.
        *   Не все комментарии после `#` соответствуют требованиям (должны объяснять последующий код).
        *   Не везде соблюдается стиль наименования функций и переменных, соответствующий предыдущим файлам.
        *   Отсутствуют примеры использования в docstring.

**Рекомендации по улучшению**

1.  **Форматирование документации:**
    *   Перевести все docstring в формат reStructuredText (RST).
    *   Добавить примеры использования в docstring.

2.  **Импорты:**
    *   Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
    *   Убедиться в отсутствии лишних импортов.

3.  **Обработка данных:**
    *   Заменить `json.load` на `j_loads` или `j_loads_ns` при чтении данных (если это потребуется).

4.  **Логирование:**
    *   Заменить избыточное использование `try-except` в функции `main` на логирование ошибок через `logger.error`.

5.  **Комментарии:**
    *   Привести комментарии после `#` к виду, когда они объясняют последующий код, а не просто дублируют его смысл.
    *   Переписать все комментарии к модулям, функциям, методам и переменным в формат RST.

6.  **Стиль кода:**
    *   Соблюдать единый стиль именования переменных и функций, соответствующий предыдущим файлам.

7.  **Общая функция:**
    *   Рассмотреть возможность создания универсальной функции конвертации для класса, если это уместно.

**Улучшенный код**

```python
"""
Модуль для конвертации температур
=========================================================================================

Модуль содержит реализации калькулятора температуры, который может конвертировать значения между
градусами Цельсия, Фаренгейта и Кельвина.

Примеры использования
--------------------

.. code-block:: python

    # Пример использования в convertor_kcf.py
    from convertor_kcf import convert_temperature
    celsius_temp = convert_temperature(25, 'C', 'F')
    print(celsius_temp)

    # Пример использования в convertor_kcf_dataclass.py
    from convertor_kcf_dataclass import TemperatureConverter
    converter = TemperatureConverter()
    kelvin_temp = converter.convert_temperature(300, 'K', 'C')
    print(kelvin_temp)
"""
from src.logger.logger import logger # Добавлен импорт logger

# Калькулятор температуры на Python

# Этот проект содержит два варианта реализации калькулятора температуры, который может конвертировать значения между градусами Цельсия, Фаренгейта и Кельвина.

# ## Файлы проекта

# 1.  **`convertor_kcf.py`**: Реализация калькулятора температуры с использованием отдельных функций.
# 2.  **`convertor_kcf_dataclass.py`**: Реализация калькулятора температуры с использованием `dataclass`.
# 3.  **`readme.md`**: Этот файл с описанием проекта.

# ## Описание `convertor_kcf.py`

# Этот файл содержит реализацию калькулятора температуры с использованием отдельных функций. Код разделен на несколько блоков:

# ### 1. Функции конвертации


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Конвертирует температуру из градусов Цельсия в градусы Фаренгейта.

    :param celsius: Температура в градусах Цельсия.
    :type celsius: float
    :return: Температура в градусах Фаренгейта.
    :rtype: float

    .. code-block:: python

        celsius_to_fahrenheit(25)
        # Вывод: 77.0
    """
    fahrenheit = (celsius * 9/5) + 32 # Вычисление температуры в градусах Фаренгейта
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Конвертирует температуру из градусов Фаренгейта в градусы Цельсия.

    :param fahrenheit: Температура в градусах Фаренгейта.
    :type fahrenheit: float
    :return: Температура в градусах Цельсия.
    :rtype: float

    .. code-block:: python

        fahrenheit_to_celsius(77)
        # Вывод: 25.0
    """
    celsius = (fahrenheit - 32) * 5/9 # Вычисление температуры в градусах Цельсия
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    """
    Конвертирует температуру из градусов Цельсия в Кельвины.

    :param celsius: Температура в градусах Цельсия.
    :type celsius: float
    :return: Температура в Кельвинах.
    :rtype: float

     .. code-block:: python

        celsius_to_kelvin(25)
        # Вывод: 298.15
    """
    kelvin = celsius + 273.15 # Вычисление температуры в Кельвинах
    return kelvin


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Конвертирует температуру из Кельвинов в градусы Цельсия.

    :param kelvin: Температура в Кельвинах.
    :type kelvin: float
    :return: Температура в градусах Цельсия.
    :rtype: float

    .. code-block:: python

        kelvin_to_celsius(298.15)
        # Вывод: 25.0
    """
    celsius = kelvin - 273.15 # Вычисление температуры в градусах Цельсия
    return celsius


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    Конвертирует температуру из градусов Фаренгейта в Кельвины.

    :param fahrenheit: Температура в градусах Фаренгейта.
    :type fahrenheit: float
    :return: Температура в Кельвинах.
    :rtype: float

     .. code-block:: python

        fahrenheit_to_kelvin(77)
        # Вывод: 298.15
    """
    celsius = fahrenheit_to_celsius(fahrenheit) # Конвертация из Фаренгейта в Цельсия
    kelvin = celsius_to_kelvin(celsius) # Конвертация из Цельсия в Кельвины
    return kelvin


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    Конвертирует температуру из Кельвинов в градусы Фаренгейта.

    :param kelvin: Температура в Кельвинах.
    :type kelvin: float
    :return: Температура в градусах Фаренгейта.
    :rtype: float

    .. code-block:: python

        kelvin_to_fahrenheit(298.15)
        # Вывод: 77.0
    """
    celsius = kelvin_to_celsius(kelvin) # Конвертация из Кельвинов в Цельсия
    fahrenheit = celsius_to_fahrenheit(celsius) # Конвертация из Цельсия в Фаренгейта
    return fahrenheit

# Каждая функция имеет:

# -   **Аннотацию типов:** `(celsius: float) -> float` указывает на тип аргумента и возвращаемого значения.
# -   **Docstring:** Строка документации описывает назначение функции, аргументы и возвращаемое значение.
# -   **Логика:** Функция выполняет конвертацию согласно известным формулам.

# ### 2. Универсальная функция конвертации


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует температуру из одной единицы измерения в другую.

    :param value: Температура для конвертации.
    :type value: float
    :param from_unit: Исходная единица измерения ('C', 'F', 'K').
    :type from_unit: str
    :param to_unit: Целевая единица измерения ('C', 'F', 'K').
    :type to_unit: str
    :return: Конвертированная температура.
    :rtype: float
    :raises ValueError: Если указаны некорректные единицы измерения.

    .. code-block:: python

        convert_temperature(25, 'C', 'F')
        # Вывод: 77.0
    """
    if from_unit == to_unit: # Проверка, что исходная и целевая единицы измерения совпадают
        return value  # нет необходимости в конвертации

    if from_unit == 'C': # Проверка исходной единицы измерения Цельсий
        if to_unit == 'F': # Проверка целевой единицы измерения Фаренгейт
            return celsius_to_fahrenheit(value) # Конвертация из Цельсия в Фаренгейт
        elif to_unit == 'K': # Проверка целевой единицы измерения Кельвин
            return celsius_to_kelvin(value) # Конвертация из Цельсия в Кельвин
    elif from_unit == 'F': # Проверка исходной единицы измерения Фаренгейт
        if to_unit == 'C': # Проверка целевой единицы измерения Цельсий
            return fahrenheit_to_celsius(value) # Конвертация из Фаренгейта в Цельсий
        elif to_unit == 'K': # Проверка целевой единицы измерения Кельвин
            return fahrenheit_to_kelvin(value) # Конвертация из Фаренгейта в Кельвин
    elif from_unit == 'K': # Проверка исходной единицы измерения Кельвин
        if to_unit == 'C': # Проверка целевой единицы измерения Цельсий
            return kelvin_to_celsius(value) # Конвертация из Кельвина в Цельсий
        elif to_unit == 'F': # Проверка целевой единицы измерения Фаренгейт
            return kelvin_to_fahrenheit(value) # Конвертация из Кельвина в Фаренгейт

    raise ValueError("Некорректные единицы измерения.") # Возбуждение исключения при некорректных единицах измерения

# Эта функция принимает значение температуры, исходную единицу измерения и целевую единицу измерения. На основе этих параметров она вызывает соответствующую функцию конвертации. Если единицы измерения одинаковы, она возвращает исходное значение. Если переданы некорректные единицы измерения, она вызывает `ValueError`.

# ### 3. Функция `main`


def main():
    """
    Главная функция для взаимодействия с пользователем.
    """
    while True: # Бесконечный цикл для взаимодействия с пользователем
        print("\nВыберите действие:")
        print("1. Конвертировать температуру")
        print("2. Выйти")

        choice = input("Введите номер действия: ") # Получение выбора от пользователя

        if choice == '1': # Проверка выбора пользователя
            try:
                value = float(input("Введите температуру: ")) # Получение значения температуры
                from_unit = input("Введите исходную единицу измерения (C, F, K): ").upper() # Получение исходной единицы измерения
                to_unit = input("Введите целевую единицу измерения (C, F, K): ").upper() # Получение целевой единицы измерения

                result = convert_temperature(value, from_unit, to_unit) # Конвертация температуры
                print(f"Результат: {result:.2f} {to_unit}") # Вывод результата

            except ValueError as e: # Обработка ошибок ввода
                logger.error(f"Ошибка ввода: {e}") # Логирование ошибки ввода
            except Exception as e: # Обработка непредвиденных ошибок
                logger.error(f"Непредвиденная ошибка: {e}") # Логирование непредвиденной ошибки

        elif choice == '2': # Проверка выбора пользователя
            print("До свидания!")
            break # Выход из цикла
        else:
            print("Некорректный ввод. Попробуйте снова.") # Сообщение о некорректном вводе

if __name__ == "__main__":
    main()
# Функция `main` содержит бесконечный цикл, в котором пользователю предлагается выбрать действие. Если пользователь выбирает конвертацию, программа запрашивает значение температуры, исходную и целевую единицы измерения, вызывает функцию `convert_temperature` и выводит результат. Также, мы обрабатываем возможные ошибки ввода с помощью `try-except` блока.

# ## Описание `convertor_kcf_dataclass.py`

# Этот файл содержит реализацию калькулятора температуры с использованием `dataclass`.

# ### 1. `dataclass` `TemperatureConverter`
```
```python
"""
Модуль для конвертации температур с использованием dataclass
=========================================================================================

Модуль содержит реализацию калькулятора температуры с использованием `dataclass`,
который может конвертировать значения между градусами Цельсия, Фаренгейта и Кельвина.

Примеры использования
--------------------

.. code-block:: python

    from convertor_kcf_dataclass import TemperatureConverter
    converter = TemperatureConverter()
    kelvin_temp = converter.convert_temperature(300, 'K', 'C')
    print(kelvin_temp)
"""
from dataclasses import dataclass # Импорт dataclass
from src.logger.logger import logger # Добавлен импорт logger

@dataclass
class TemperatureConverter:
    """
    Класс для конвертации температур между градусами Цельсия, Фаренгейта и Кельвина.
    """

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        Конвертирует температуру из градусов Цельсия в градусы Фаренгейта.

        :param celsius: Температура в градусах Цельсия.
        :type celsius: float
        :return: Температура в градусах Фаренгейта.
        :rtype: float

        .. code-block:: python

            converter = TemperatureConverter()
            converter.celsius_to_fahrenheit(25)
            # Вывод: 77.0
        """
        fahrenheit = (celsius * 9/5) + 32 # Вычисление температуры в градусах Фаренгейта
        return fahrenheit


    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        """
        Конвертирует температуру из градусов Фаренгейта в градусы Цельсия.

        :param fahrenheit: Температура в градусах Фаренгейта.
        :type fahrenheit: float
        :return: Температура в градусах Цельсия.
        :rtype: float

        .. code-block:: python

            converter = TemperatureConverter()
            converter.fahrenheit_to_celsius(77)
            # Вывод: 25.0
        """
        celsius = (fahrenheit - 32) * 5/9 # Вычисление температуры в градусах Цельсия
        return celsius


    def celsius_to_kelvin(self, celsius: float) -> float:
        """
        Конвертирует температуру из градусов Цельсия в Кельвины.

        :param celsius: Температура в градусах Цельсия.
        :type celsius: float
        :return: Температура в Кельвинах.
        :rtype: float

         .. code-block:: python

            converter = TemperatureConverter()
            converter.celsius_to_kelvin(25)
            # Вывод: 298.15
        """
        kelvin = celsius + 273.15 # Вычисление температуры в Кельвинах
        return kelvin


    def kelvin_to_celsius(self, kelvin: float) -> float:
        """
        Конвертирует температуру из Кельвинов в градусы Цельсия.

        :param kelvin: Температура в Кельвинах.
        :type kelvin: float
        :return: Температура в градусах Цельсия.
        :rtype: float

        .. code-block:: python

            converter = TemperatureConverter()
            converter.kelvin_to_celsius(298.15)
            # Вывод: 25.0
        """
        celsius = kelvin - 273.15 # Вычисление температуры в градусах Цельсия
        return celsius


    def fahrenheit_to_kelvin(self, fahrenheit: float) -> float:
        """
        Конвертирует температуру из градусов Фаренгейта в Кельвины.

        :param fahrenheit: Температура в градусах Фаренгейта.
        :type fahrenheit: float
        :return: Температура в Кельвинах.
        :rtype: float

        .. code-block:: python

            converter = TemperatureConverter()
            converter.fahrenheit_to_kelvin(77)
            # Вывод: 298.15
        """
        celsius = self.fahrenheit_to_celsius(fahrenheit) # Конвертация из Фаренгейта в Цельсия
        kelvin = self.celsius_to_kelvin(celsius) # Конвертация из Цельсия в Кельвины
        return kelvin


    def kelvin_to_fahrenheit(self, kelvin: float) -> float:
        """
        Конвертирует температуру из Кельвинов в градусы Фаренгейта.

        :param kelvin: Температура в Кельвинах.
        :type kelvin: float
        :return: Температура в градусах Фаренгейта.
        :rtype: float

        .. code-block:: python

            converter = TemperatureConverter()
            converter.kelvin_to_fahrenheit(298.15)
            # Вывод: 77.0
        """
        celsius = self.kelvin_to_celsius(kelvin) # Конвертация из Кельвинов в Цельсия
        fahrenheit = self.celsius_to_fahrenheit(celsius) # Конвертация из Цельсия в Фаренгейта
        return fahrenheit
    # -   **Импорт `dataclass`:** Мы импортируем декоратор `dataclass` из модуля `dataclasses`.
    # -   **Класс `TemperatureConverter`:** Мы создаем класс `TemperatureConverter` и декорируем его с помощью `@dataclass`. Это автоматически создаст конструктор и другие необходимые методы для класса.
    # -   **Методы класса:** Все наши функции конвертации теперь являются методами класса `TemperatureConverter`. Первый параметр `self` указывает на экземпляр класса.

    # Методы конвертации аналогичны методам в `convertor_kcf.py`, за исключением того, что они являются методами класса и принимают `self` в качестве первого аргумента.

    # ### 2. Функция `convert_temperature`

    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Конвертирует температуру из одной единицы измерения в другую.

        :param value: Температура для конвертации.
        :type value: float
        :param from_unit: Исходная единица измерения ('C', 'F', 'K').
        :type from_unit: str
        :param to_unit: Целевая единица измерения ('C', 'F', 'K').
        :type to_unit: str
        :return: Конвертированная температура.
        :rtype: float
        :raises ValueError: Если указаны некорректные единицы измерения.

        .. code-block:: python

            converter = TemperatureConverter()
            converter.convert_temperature(25, 'C', 'F')
            # Вывод: 77.0
        """
        if from_unit == to_unit: # Проверка, что исходная и целевая единицы измерения совпадают
            return value  # нет необходимости в конвертации

        if from_unit == 'C': # Проверка исходной единицы измерения Цельсий
            if to_unit == 'F': # Проверка целевой единицы измерения Фаренгейт
                return self.celsius_to_fahrenheit(value) # Конвертация из Цельсия в Фаренгейт
            elif to_unit == 'K': # Проверка целевой единицы измерения Кельвин
                return self.celsius_to_kelvin(value) # Конвертация из Цельсия в Кельвин
        elif from_unit == 'F': # Проверка исходной единицы измерения Фаренгейт
            if to_unit == 'C': # Проверка целевой единицы измерения Цельсий
                return self.fahrenheit_to_celsius(value) # Конвертация из Фаренгейта в Цельсий
            elif to_unit == 'K': # Проверка целевой единицы измерения Кельвин
                return self.fahrenheit_to_kelvin(value) # Конвертация из Фаренгейта в Кельвин
        elif from_unit == 'K': # Проверка исходной единицы измерения Кельвин
            if to_unit == 'C': # Проверка целевой единицы измерения Цельсий
                return self.kelvin_to_celsius(value) # Конвертация из Кельвина в Цельсий
            elif to_unit == 'F': # Проверка целевой единицы измерения Фаренгейт
                return self.kelvin_to_fahrenheit(value) # Конвертация из Кельвина в Фаренгейт

        raise ValueError("Некорректные единицы измерения.") # Возбуждение исключения при некорректных единицах измерения
    # Эта функция, также как и в `convertor_kcf.py`, принимает значение температуры, исходную единицу измерения и целевую единицу измерения. Но теперь она вызывает методы класса `TemperatureConverter`.

    # ### 3. Функция `main`


def main():
    """
    Главная функция для взаимодействия с пользователем.
    """
    converter = TemperatureConverter() # Создание экземпляра класса TemperatureConverter

    while True: # Бесконечный цикл для взаимодействия с пользователем
        print("\nВыберите действие:")
        print("1. Конвертировать температуру")
        print("2. Выйти")

        choice = input("Введите номер действия: ") # Получение выбора от пользователя

        if choice == '1': # Проверка выбора пользователя
            try:
                value = float(input("Введите температуру: ")) # Получение значения температуры
                from_unit = input("Введите исходную единицу измерения (C, F, K): ").upper() # Получение исходной единицы измерения
                to_unit = input("Введите целевую единицу измерения (C, F, K): ").upper() # Получение целевой единицы измерения

                result = converter.convert_temperature(value, from_unit, to_unit) # Конвертация температуры
                print(f"Результат: {result:.2f} {to_unit}") # Вывод результата

            except ValueError as e: # Обработка ошибок ввода
                logger.error(f"Ошибка ввода: {e}") # Логирование ошибки ввода
            except Exception as e: # Обработка непредвиденных ошибок
                 logger.error(f"Непредвиденная ошибка: {e}") # Логирование непредвиденной ошибки

        elif choice == '2': # Проверка выбора пользователя
            print("До свидания!")
            break # Выход из цикла
        else:
            print("Некорректный ввод. Попробуйте снова.") # Сообщение о некорректном вводе

if __name__ == "__main__":
    main()
# В функции `main` мы создаем экземпляр класса `TemperatureConverter` с именем `converter`. Теперь мы вызываем методы конвертации через этот экземпляр, например: `converter.convert_temperature()`.

# ## Сравнение двух подходов

# -   **`convertor_kcf.py`:** Функции конвертации существуют независимо друг от друга, что может быть менее организованным для более сложных программ.
# -   **`convertor_kcf_dataclass.py`:** Все функции конвертации сгруппированы в классе, что делает код более модульным и читаемым. `dataclass` также обеспечивает автоматическое создание конструктора и других методов.

# ## Запуск кода

# Чтобы запустить любой из файлов, убедись, что у тебя установлен Python. Затем выполни в терминале:

# ```bash
# python convertor_kcf.py
# ```

# или

# ```bash
# python convertor_kcf_dataclass.py
# ```

# Оба подхода решают одну и ту же задачу, но с использованием разных способов организации кода.
# `dataclass` позволяет более структурировано подойти к решению задачи и упрощает сопровождение и расширение кода.
```