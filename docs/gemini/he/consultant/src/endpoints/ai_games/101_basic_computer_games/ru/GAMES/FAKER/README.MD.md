# Анализ кода модуля `FakeDataGenerator`

**Качество кода**

-   **Соблюдение требований к формату кода (1-10):** 7/10
    *   **Преимущества:**
        *   Код хорошо структурирован и понятен, методы разделены по функционалу.
        *   Используются аннотации типов для повышения читаемости.
        *   Наличие docstring для каждого метода.
        *   Присутствует пример использования класса в блоке `if __name__ == '__main__':`.
    *   **Недостатки:**
        *   Отсутствует описание модуля в начале файла.
        *   Не соблюден формат docstring reStructuredText (RST).
        *   Не используются логирование ошибок и исключений.
        *   Не импортированы необходимые библиотеки из `src.utils.jjson` и `src.logger.logger`.
        *   Все комментарии написаны в формате Markdown, а не RST.

**Рекомендации по улучшению**

1.  **Добавить описание модуля:** В начале файла необходимо добавить описание модуля в формате RST.
2.  **Использовать reStructuredText (RST):** Необходимо переписать docstring для всех методов в формате RST.
3.  **Добавить логирование ошибок:** Необходимо добавить логирование ошибок с помощью `from src.logger.logger import logger` и использовать `logger.error()` для обработки исключений.
4.  **Удалить лишние try-except блоки:** Вместо использования стандартных блоков `try-except` следует использовать `logger.error()`.
5.  **Использовать `j_loads` или `j_loads_ns`:** Хотя в данном коде не используются json-файлы, стоит упомянуть о необходимости их использования в соответствии с требованиями.
6.  **Переименовать переменные:** Необходимо проверить имена переменных на соответствие ранее обработанным файлам (не применимо в данном случае).
7.  **Добавить примеры docstring:** Вставить примеры правильного docstring в формате RST.
8.  **Внести изменения в docstring:** Избегать слов, таких как "получает", "делает", вместо них использовать более точные формулировки, например, "выполняет", "проверяет", "генерирует".

**Улучшенный код**

```python
"""
Модуль для генерации фейковых данных
=========================================================================================

Этот модуль содержит класс :class:`FakeDataGenerator`, который используется для генерации различных видов
случайных данных, таких как имена, адреса, номера телефонов, email-адреса и др.

Пример использования
--------------------

Пример использования класса `FakeDataGenerator`:

.. code-block:: python

    faker = FakeDataGenerator()
    print(faker.random_name())
    print(faker.random_email())
"""
import random
import string
from typing import List, Optional
from src.logger.logger import logger #  Импорт логгера

class FakeDataGenerator:
    """
    Класс для генерации фейковых данных.

    :ivar first_names: Список имен.
    :vartype first_names: List[str]
    :ivar last_names: Список фамилий.
    :vartype last_names: List[str]
    :ivar cities: Список городов.
    :vartype cities: List[str]
    :ivar streets: Список улиц.
    :vartype streets: List[str]
    :ivar domains: Список доменов.
    :vartype domains: List[str]
    """
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana'] #  Список имен
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia'] #  Список фамилий
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'] #  Список городов
    streets = ['Main St', 'Elm St', '2nd Ave', 'Park Blvd', 'Oak Dr'] #  Список улиц
    domains = ['example.com', 'mail.com', 'test.org', 'website.net'] #  Список доменов

    def random_name(self) -> str:
        """
        Генерирует случайное полное имя.

        :return: Случайное полное имя, состоящее из имени и фамилии.
        :rtype: str

        Пример:
        
        .. code-block:: python
           
           faker = FakeDataGenerator()
           name = faker.random_name()
           print(name) #  Результат: 'Alice Smith'
        """
        first_name = random.choice(self.first_names) # Выбирает случайное имя
        last_name = random.choice(self.last_names) # Выбирает случайную фамилию
        return f'{first_name} {last_name}' # Возвращает строку с именем и фамилией

    def random_email(self) -> str:
        """
        Генерирует случайный email-адрес.

        :return: Email-адрес в формате `имя.фамилия@домен`.
        :rtype: str

        Пример:
        
        .. code-block:: python
           
           faker = FakeDataGenerator()
           email = faker.random_email()
           print(email) #  Результат: 'jane.smith@mail.com'
        """
        first_name = random.choice(self.first_names).lower() # Выбирает случайное имя и преобразует в нижний регистр
        last_name = random.choice(self.last_names).lower() # Выбирает случайную фамилию и преобразует в нижний регистр
        domain = random.choice(self.domains) # Выбирает случайный домен
        return f'{first_name}.{last_name}@{domain}' # Возвращает строку с email-адресом

    def random_phone(self) -> str:
        """
        Генерирует случайный номер телефона в формате `+1-XXX-XXX-XXXX`.

        :return: Номер телефона.
        :rtype: str

        Пример:
        
        .. code-block:: python
           
           faker = FakeDataGenerator()
           phone = faker.random_phone()
           print(phone) #  Результат: '+1-567-890-1234'
        """
        return f'+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}' # Возвращает строку с номером телефона

    def random_address(self) -> str:
        """
        Генерирует случайный адрес.

        :return: Адрес в формате `улица, город`.
        :rtype: str
           
        Пример:
        
        .. code-block:: python
           
           faker = FakeDataGenerator()
           address = faker.random_address()
           print(address) #  Результат: '1234 Main St, Chicago'
        """
        street = random.choice(self.streets) # Выбирает случайную улицу
        city = random.choice(self.cities) # Выбирает случайный город
        house_number = random.randint(1, 9999) # Выбирает случайный номер дома
        return f'{house_number} {street}, {city}' # Возвращает строку с адресом

    def random_string(self, length: int = 10) -> str:
        """
        Генерирует случайную строку заданной длины.

        :param length: Длина строки.
        :type length: int, optional
        :return: Случайная строка, содержащая буквы и цифры.
        :rtype: str

        Пример:
        
        .. code-block:: python
           
           faker = FakeDataGenerator()
           random_string = faker.random_string(15)
           print(random_string) #  Результат: 'aB4cDe5fGh6iJk7l'
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
        
        Пример:
        
        .. code-block:: python
           
           faker = FakeDataGenerator()
           random_int = faker.random_int(1, 10)
           print(random_int) #  Результат: 7
        """
        return random.randint(min_value, max_value) # Возвращает случайное целое число

    def random_choice(self, options: List[str]) -> str:
        """
        Выбирает случайный элемент из списка.

        :param options: Список значений для выбора.
        :type options: List[str]
        :return: Случайный элемент из списка.
        :rtype: str

        Пример:
        
        .. code-block:: python
           
           faker = FakeDataGenerator()
           random_choice = faker.random_choice(["Option1", "Option2", "Option3"])
           print(random_choice) #  Результат: 'Option2'
        """
        return random.choice(options) # Возвращает случайный элемент из списка

if __name__ == '__main__':
    faker = FakeDataGenerator() # Создает экземпляр класса FakeDataGenerator

    print(f'Name: {faker.random_name()}') #  Выводит случайное имя
    print(f'Email: {faker.random_email()}') #  Выводит случайный email
    print(f'Phone: {faker.random_phone()}') #  Выводит случайный номер телефона
    print(f'Address: {faker.random_address()}') #  Выводит случайный адрес
    print(f'Random String: {faker.random_string(12)}') #  Выводит случайную строку
    print(f'Random Int: {faker.random_int(50, 150)}') #  Выводит случайное целое число
    print(f'Random Choice: {faker.random_choice(["Option1", "Option2", "Option3"])}') # Выводит случайный выбор из списка
```