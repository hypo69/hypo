# Анализ кода модуля `FakeDataGenerator`

**Качество кода**
-  **Соблюдение требований к формату кода (1-10):** 7/10
    -  **Преимущества:**
        -   Код хорошо структурирован и читабелен.
        -   Используются аннотации типов для улучшения понимания кода.
        -   Методы класса имеют понятные названия и описания.
        -   Присутствуют docstring для методов, что облегчает понимание их назначения и использования.
    - **Недостатки:**
        -  Отсутствуют docstring для класса.
        -  Нет описания модуля.
        -  Не используется `logger` для обработки ошибок или отладки.
        -   Не все методы документированы в формате RST, отсутствуют такие поля, как параметры и возвращаемые значения, а также описания.

**Рекомендации по улучшению**
1.  Добавить описание модуля в начале файла.
2.  Добавить docstring для класса `FakeDataGenerator`.
3.  Использовать reStructuredText (RST) для всех docstring, включая описания параметров и возвращаемых значений.
4.  Заменить прямые вызовы `print()` на логирование с помощью `logger` для отладки и вывода результатов.
5.  Учесть возможность ошибок при генерации случайных данных и использовать `try-except` с `logger.error` для их обработки, если это необходимо.
6.  Использовать константы для списков имен, фамилий и т.д.

**Улучшенный код**
```python
"""
Модуль для генерации случайных данных.
=========================================================================================

Модуль `FakeDataGenerator` предоставляет класс для создания фиктивных данных,
таких как имена, email-адреса, номера телефонов, адреса и другие.

Пример использования
--------------------

Пример создания и использования `FakeDataGenerator`:

.. code-block:: python

    faker = FakeDataGenerator()
    name = faker.random_name()
    email = faker.random_email()
    print(f"Случайное имя: {name}, Случайный email: {email}")
"""
import random  # Используется для генерации случайных чисел
import string # Предоставляет набор символов
from typing import List, Optional # Используется для аннотации типов
from src.logger.logger import logger # Импорт логгера для записи ошибок

class FakeDataGenerator:
    """
    Класс для генерации фейковых данных.

    Этот класс предоставляет методы для создания различных видов случайных данных,
    таких как имена, email-адреса, номера телефонов, адреса и случайные строки.

    :ivar first_names: Список имен.
    :vartype first_names: List[str]
    :ivar last_names: Список фамилий.
    :vartype last_names: List[str]
    :ivar cities: Список городов.
    :vartype cities: List[str]
    :ivar streets: Список улиц.
    :vartype streets: List[str]
    :ivar domains: Список доменов для email.
    :vartype domains: List[str]
    """
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana'] # Список имен
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia'] # Список фамилий
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'] # Список городов
    streets = ['Main St', 'Elm St', '2nd Ave', 'Park Blvd', 'Oak Dr'] # Список улиц
    domains = ['example.com', 'mail.com', 'test.org', 'website.net'] # Список доменов


    def random_name(self) -> str:
        """
        Генерирует случайное полное имя.

        :return: Полное имя, состоящее из случайного имени и фамилии.
        :rtype: str
        """
        first_name = random.choice(self.first_names) # Выбор случайного имени
        last_name = random.choice(self.last_names) # Выбор случайной фамилии
        return f'{first_name} {last_name}' # Возвращает полное имя

    def random_email(self) -> str:
        """
        Генерирует случайный email-адрес.

        :return: Email-адрес в формате `имя.фамилия@домен`.
        :rtype: str
        """
        first_name = random.choice(self.first_names).lower() # Выбор случайного имени и преобразование в нижний регистр
        last_name = random.choice(self.last_names).lower() # Выбор случайной фамилии и преобразование в нижний регистр
        domain = random.choice(self.domains) # Выбор случайного домена
        return f'{first_name}.{last_name}@{domain}' # Возвращает email-адрес

    def random_phone(self) -> str:
        """
        Генерирует случайный номер телефона в формате `+1-XXX-XXX-XXXX`.

        :return: Номер телефона.
        :rtype: str
        """
        return f'+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}' # Возвращает номер телефона

    def random_address(self) -> str:
        """
        Генерирует случайный адрес.

        :return: Адрес в формате `номер_дома улица, город`.
        :rtype: str
        """
        street = random.choice(self.streets) # Выбор случайной улицы
        city = random.choice(self.cities) # Выбор случайного города
        house_number = random.randint(1, 9999) # Генерация случайного номера дома
        return f'{house_number} {street}, {city}' # Возвращает адрес

    def random_string(self, length: int = 10) -> str:
        """
        Генерирует случайную строку заданной длины.

        :param length: Длина строки.
        :type length: int, optional
        :return: Случайная строка, содержащая буквы и цифры.
        :rtype: str
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) # Возвращает случайную строку

    def random_int(self, min_value: int = 0, max_value: int = 100) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        :param min_value: Минимальное значение.
        :type min_value: int, optional
        :param max_value: Максимальное значение.
        :type max_value: int, optional
        :return: Случайное целое число.
        :rtype: int
        """
        return random.randint(min_value, max_value) # Возвращает случайное целое число

    def random_choice(self, options: List[str]) -> str:
        """
        Выбирает случайный элемент из списка.

        :param options: Список значений для выбора.
        :type options: List[str]
        :return: Случайный элемент из списка.
        :rtype: str
        """
        return random.choice(options) # Возвращает случайный элемент из списка


if __name__ == '__main__':
    faker = FakeDataGenerator() # Создание экземпляра класса

    try: # Обработка возможных исключений
        name = faker.random_name() # Генерация случайного имени
        logger.info(f'Name: {name}') # Логирование сгенерированного имени
        email = faker.random_email() # Генерация случайного email
        logger.info(f'Email: {email}') # Логирование сгенерированного email
        phone = faker.random_phone() # Генерация случайного номера телефона
        logger.info(f'Phone: {phone}') # Логирование сгенерированного номера телефона
        address = faker.random_address() # Генерация случайного адреса
        logger.info(f'Address: {address}') # Логирование сгенерированного адреса
        random_string = faker.random_string(12) # Генерация случайной строки
        logger.info(f'Random String: {random_string}') # Логирование сгенерированной строки
        random_int = faker.random_int(50, 150) # Генерация случайного целого числа
        logger.info(f'Random Int: {random_int}') # Логирование сгенерированного числа
        random_choice = faker.random_choice(["Option1", "Option2", "Option3"]) # Выбор случайного элемента из списка
        logger.info(f'Random Choice: {random_choice}') # Логирование выбранного элемента

    except Exception as e: # Перехват любых исключений
        logger.error(f'Произошла ошибка при генерации данных: {e}') # Логирование ошибки
```