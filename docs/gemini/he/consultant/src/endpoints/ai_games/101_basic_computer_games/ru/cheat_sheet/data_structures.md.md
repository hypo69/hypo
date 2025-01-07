# Анализ кода модуля `data_structures.md`

**Качество кода**

-   **Соответствие требованиям к формату кода (1-10):** 7
    *   **Преимущества:**
        *   Код хорошо структурирован и понятен.
        *   Присутствуют примеры использования различных структур данных.
        *   Используется `f-строки` для форматированного вывода.
    *   **Недостатки:**
        *   Отсутствует документация в формате `reStructuredText (RST)`.
        *   Не используются `j_loads` или `j_loads_ns`.
        *   Не используется `logger` для обработки ошибок.
        *   Нет импорта необходимых модулей, если это не в `md` файле.
        *   Присутствуют комментарии `#` в стиле, не совпадающим с форматом, указанным в инструкции.

**Рекомендации по улучшению**

1.  Добавить документацию в формате `reStructuredText (RST)` для каждой структуры данных.
2.  Импортировать необходимые модули.
3.  Добавить обработку ошибок с использованием `logger.error`.
4.  Убрать лишние комментарии, оставить только необходимые.
5.  Комментарии должны быть в стиле `RST`, где это возможно.
6.  Переписать код в Python формате, который можно будет исполнить.

**Улучшенный код**

```python
"""
Модуль, представляющий шпаргалку по структурам данных в Python.
==============================================================

Этот модуль содержит примеры работы с основными структурами данных Python:
списками, словарями, кортежами и SimpleNamespace.

Примеры использования
---------------------

Примеры использования различных структур данных:

.. code-block:: python

    from types import SimpleNamespace

    # Списки
    boris_list = ['Борис', 'Москва', 30, 'инженер']
    print(f"Создание списка: {boris_list}")

    # Словари
    alice_dict = {'name': 'Алиса', 'age': 25, 'city': 'Лондон', 'occupation': 'художница'}
    print(f"Создание словаря: {alice_dict}")

    # Кортежи
    boris_tuple = ('Борис', 'Москва', 30, 'инженер')
    print(f"Создание кортежа: {boris_tuple}")

    # SimpleNamespace
    alice_namespace = SimpleNamespace(name='Алиса', age=25, city='Лондон')
    print(f"Создание SimpleNamespace: {alice_namespace}")
"""
from types import SimpleNamespace  # Импорт SimpleNamespace
from src.logger.logger import logger  # Импорт logger
#from src.utils.jjson import j_loads, j_loads_ns # Импорт j_loads и j_loads_ns
# 1. Списки (Lists)

#: Списки в Python - это упорядоченные, изменяемые коллекции элементов.
#: Это значит, что можно добавлять, удалять и изменять элементы в списке, и порядок элементов имеет значение.
#: Списки создаются с помощью квадратных скобок `[]`, а элементы разделяются запятыми.
def list_examples():
    """
    Примеры работы со списками.

    :return: None
    """
    try:
        boris_list = ['Борис', 'Москва', 30, 'инженер'] # Создание списка
        print(f"Создание списка: {boris_list}") # Вывод списка

        print(f"Элемент по индексу 0: {boris_list[0]}") # Доступ по индексу

        boris_list[2] = 31 # Изменение элемента
        print(f"Изменение элемента: {boris_list}")

        boris_list.append('женат') # Добавление элемента в конец
        print(f"Добавление в конец: {boris_list}")

        boris_list.insert(1, 'Россия') # Вставка элемента по индексу
        print(f"Вставка элемента: {boris_list}")

        boris_list.remove('инженер') # Удаление элемента по значению
        print(f"Удаление элемента по значению: {boris_list}")

        del boris_list[2] # Удаление элемента по индексу
        print(f"Удаление элемента по индексу: {boris_list}")

        boris_list.extend(['хобби', 'рыбалка']) # Расширение списка другим списком
        print(f"Расширение списка: {boris_list}")

        boris_list.pop()  # Удаление элемента с конца
        print(f"Удаление элемента с конца: {boris_list}")
    except Exception as ex:  # Обработка исключений
        logger.error(f'Ошибка при работе со списками', ex)  # Логирование ошибки

# 2. Словари (Dictionaries)

#: Словари в Python - это неупорядоченные коллекции элементов, где каждый элемент состоит из пары "ключ-значение".
#: Словари создаются с помощью фигурных скобок `{}`, а пары "ключ-значение" разделяются двоеточием `:`.
def dict_examples():
    """
    Примеры работы со словарями.

    :return: None
    """
    try:
        alice_dict = {'name': 'Алиса', 'age': 25, 'city': 'Лондон', 'occupation': 'художница'} # Создание словаря
        print(f"Создание словаря: {alice_dict}") # Вывод словаря

        print(f"Значение по ключу \'name\': {alice_dict['name']}") # Доступ по ключу

        alice_dict['age'] = 26  # Изменение значения
        print(f"Изменение значения: {alice_dict}")

        alice_dict['hobby'] = 'рисование'  # Добавление пары ключ-значение
        print(f"Добавление пары: {alice_dict}")

        del alice_dict['city'] # Удаление пары по ключу
        print(f"Удаление пары: {alice_dict}")

        hobby = alice_dict.pop('hobby') # Удаление пары методом pop (с возвращением значения)
        print(f"Удаление с возвратом значения: {alice_dict}, значение: {hobby}")

        print(f"Наличие ключа \'name\': {'name' in alice_dict}") # Проверка наличия ключа
    except Exception as ex:  # Обработка исключений
        logger.error(f'Ошибка при работе со словарями', ex)  # Логирование ошибки

# 3. Кортежи (Tuples)
#: Кортежи в Python - это упорядоченные, **неизменяемые** коллекции элементов.
#: Кортежи создаются с помощью круглых скобок `()`, а элементы разделяются запятыми.
def tuple_examples():
    """
    Примеры работы с кортежами.

    :return: None
    """
    try:
        boris_tuple = ('Борис', 'Москва', 30, 'инженер')  # Создание кортежа
        print(f"Создание кортежа: {boris_tuple}")  # Вывод кортежа

        print(f"Элемент по индексу 2: {boris_tuple[2]}") # Доступ по индексу

        # boris_tuple[0] = "Борис" # Это вызовет ошибку: TypeError: 'tuple' object does not support item assignment
        # boris_tuple.append(4) # Это вызовет ошибку: AttributeError: 'tuple' object has no attribute 'append'
        # del boris_tuple[0]  # Это вызовет ошибку: TypeError: 'tuple' object doesn't support item deletion
    except Exception as ex: # Обработка исключений
        logger.error(f'Ошибка при работе с кортежами', ex) # Логирование ошибки

# 4. SimpleNamespace
#: `SimpleNamespace` из модуля `types` - это простой класс, позволяющий создавать объекты, у которых атрибуты (свойства) можно задавать как при создании, так и потом.
#: Для создания объекта `SimpleNamespace` нужно импортировать его из `types` и передать в него именованные аргументы (или не передать их).
#: Позволяет создавать объекты с динамическими атрибутами (похоже на словарь).
#: Удобен для создания простых объектов для хранения данных.
#: Атрибуты доступны через точку, как у обычных объектов: `alice_namespace.name`
#: В отличие от словарей, порядок атрибутов сохраняется.
#: Поля можно менять, но нельзя добавлять новые поля

def simplenamespace_examples():
    """
    Примеры работы с SimpleNamespace.

    :return: None
    """
    try:
        alice_namespace = SimpleNamespace(name='Алиса', age=25, city='Лондон') # Создание SimpleNamespace
        print(f"Создание SimpleNamespace: {alice_namespace}") # Вывод SimpleNamespace

        print(f"Атрибут \'name\': {alice_namespace.name}") # Доступ к атрибуту

        alice_namespace.age = 26  # Изменение атрибута
        print(f"Изменение атрибута: {alice_namespace}")

        # alice_namespace.occupation = "художница" # Это вызовет ошибку: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

        setattr(alice_namespace, "occupation", "художница") # Добавление через setattr
        print(f"Добавление атрибута: {alice_namespace}")

        delattr(alice_namespace, "city") # Удаление через delattr
        print(f"Удаление атрибута: {alice_namespace}")
    except Exception as ex: # Обработка исключений
         logger.error(f'Ошибка при работе с SimpleNamespace', ex) # Логирование ошибки

if __name__ == '__main__': # Вызов примеров
    list_examples() # Вызов примеров списка
    dict_examples() # Вызов примеров словаря
    tuple_examples() # Вызов примеров кортежа
    simplenamespace_examples() # Вызов примеров SimpleNamespace
```