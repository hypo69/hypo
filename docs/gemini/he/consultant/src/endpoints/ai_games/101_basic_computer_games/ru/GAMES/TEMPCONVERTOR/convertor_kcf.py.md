# Анализ кода модуля `convertor_kcf.py`

**Качество кода**

-   **Соблюдение требований к формату кода (1-10):** 7/10
    -   **Плюсы:**
        -   Код хорошо структурирован и читаем.
        -   Функции имеют docstring, хотя и не в формате reStructuredText (RST).
        -   Код выполняет поставленную задачу конвертации температур.
    -   **Минусы:**
        -   Отсутствует импорт `logger` из `src.logger.logger`.
        -   Не используется `j_loads` или `j_loads_ns`.
        -   Docstring не соответствуют формату RST.
        -   Используются стандартные блоки `try-except` вместо `logger.error` для обработки ошибок.

**Рекомендации по улучшению**

1.  **Формат документации:**
    -   Переписать все docstring в формате reStructuredText (RST).
    -   Добавить описание модуля в начале файла.
    -   Использовать правильный синтаксис RST для параметров, возвращаемых значений и исключений.
2.  **Импорты:**
    -   Добавить импорт `logger` из `src.logger.logger` для логирования ошибок.
3.  **Обработка ошибок:**
    -   Заменить стандартные блоки `try-except` на `logger.error` для обработки ошибок.
4.  **Работа с JSON:**
    -   Использовать `j_loads` или `j_loads_ns` при чтении файлов, если это необходимо. В текущем коде это не требуется.
5.  **Общее:**
    -   Переписать комментарии после `#` в коде, для описания происходящего в коде.
    -   Удалить лишние комментарии.

**Улучшенный код**

```python
"""
Модуль для конвертации температуры между градусами Цельсия, Фаренгейта и Кельвина.
===================================================================================

Этот модуль предоставляет функции для конвертации температуры из одной единицы измерения в другую.
Поддерживаются следующие единицы: градусы Цельсия (C), градусы Фаренгейта (F) и Кельвины (K).

Пример использования
--------------------

.. code-block:: python

    from convertor_kcf import convert_temperature

    celsius = 25
    fahrenheit = convert_temperature(celsius, 'C', 'F')
    print(f"{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")
"""
from src.logger.logger import logger # Добавлен импорт logger

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Конвертирует температуру из градусов Цельсия в градусы Фаренгейта.

    :param celsius: Температура в градусах Цельсия.
    :type celsius: float
    :return: Температура в градусах Фаренгейта.
    :rtype: float
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
    """
    celsius = kelvin_to_celsius(kelvin) # Конвертация из Кельвинов в Цельсия
    fahrenheit = celsius_to_fahrenheit(celsius) # Конвертация из Цельсия в Фаренгейта
    return fahrenheit

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
    """
    if from_unit == to_unit:
        return value  # Если исходная и целевая единицы совпадают, возвращаем исходное значение

    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value) # Конвертация из Цельсия в Фаренгейта
        elif to_unit == 'K':
            return celsius_to_kelvin(value) # Конвертация из Цельсия в Кельвины
    elif from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value) # Конвертация из Фаренгейта в Цельсия
        elif to_unit == 'K':
            return fahrenheit_to_kelvin(value) # Конвертация из Фаренгейта в Кельвины
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value) # Конвертация из Кельвинов в Цельсия
        elif to_unit == 'F':
            return kelvin_to_fahrenheit(value) # Конвертация из Кельвинов в Фаренгейта

    raise ValueError("Некорректные единицы измерения.") # Выбрасывается исключение, если указаны некорректные единицы измерения

def main():
    """
    Главная функция для взаимодействия с пользователем.
    """
    while True:
        print("\nВыберите действие:")
        print("1. Конвертировать температуру")
        print("2. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            try:
                value = float(input("Введите температуру: ")) # Получение значения температуры от пользователя
                from_unit = input("Введите исходную единицу измерения (C, F, K): ").upper() # Получение исходной единицы измерения от пользователя
                to_unit = input("Введите целевую единицу измерения (C, F, K): ").upper() # Получение целевой единицы измерения от пользователя

                result = convert_temperature(value, from_unit, to_unit) # Вызов функции конвертации температуры
                print(f"Результат: {result:.2f} {to_unit}")

            except ValueError as e:
                logger.error(f"Ошибка ввода: {e}") # Логирование ошибки ValueError
                print(f"Ошибка: {e}")
            except Exception as e:
                logger.error(f"Непредвиденная ошибка: {e}") # Логирование непредвиденной ошибки
                print(f"Непредвиденная ошибка: {e}")


        elif choice == '2':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.") # Вывод сообщения об ошибке ввода

if __name__ == "__main__":
    main()
```