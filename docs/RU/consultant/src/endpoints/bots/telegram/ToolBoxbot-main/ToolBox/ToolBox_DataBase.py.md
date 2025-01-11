# Анализ кода модуля ToolBox_DataBase

**Качество кода**

6/10
- Плюсы
    - Код структурирован в класс `DataBase`, что способствует организации и повторному использованию.
    - Присутствует разделение на методы для создания, загрузки и обновления данных.
    - Используются аннотации типов, что улучшает читаемость и помогает в отладке.
    - Есть базовые проверки и преобразования данных.
- Минусы
    - Отсутствует обработка ошибок при работе с базой данных, что может привести к неожиданным сбоям.
    - Используется `literal_eval` для преобразования строк в списки, что небезопасно.
    - Не везде соблюдены требования по оформлению кода.
    - Не хватает документации для класса и методов в формате RST.
    - Используется `json.dumps` в `insert_or_update_data` для преобразования данных перед сохранением, но не используется `j_loads` или `j_loads_ns` при чтении данных.
    - Использование `sub` с регулярными выражениями в нескольких местах усложняет понимание кода.
    - Логирование не используется, что затрудняет отладку и мониторинг работы кода.

**Рекомендации по улучшению**

1.  **Безопасность**: Замените `literal_eval` на более безопасный способ преобразования строк в списки, например, с использованием `json.loads` или `ast.literal_eval` после дополнительной проверки.
2.  **Обработка ошибок**: Добавьте обработку ошибок с использованием `try-except` и логированием ошибок с помощью `logger.error`.
3.  **Использование `j_loads`**: Используйте `j_loads` из `src.utils.jjson` вместо стандартного `json.load` для чтения данных из файлов.
4.  **Форматирование**: Приведите код в соответствие с требованиями по оформлению (одинарные кавычки, и т.д.)
5.  **Документирование**: Добавьте docstrings в формате RST для класса и его методов.
6.  **Рефакторинг**: Упростите сложные преобразования данных с использованием вспомогательных функций.
7.  **Логирование**: Добавьте логирование для важных действий (например, создание подключения к базе данных, выполнение запросов, сохранение данных).
8.  **Константы**: Вынесите магические числа (например, `8` в `if __name__ == "__main__":`) в константы.
9.  **Улучшить именование**: Переменные `base` и `db` в `if __name__ == "__main__":` сделать более понятными.
10. **Переделать ввод данных**:  В `if __name__ == "__main__":` ввод `uid` и обработку сделать более гибкими.

**Оптимизированный код**

```python
"""
Модуль для работы с базой данных SQLite.
=========================================================================================

Этот модуль содержит класс :class:`DataBase`, который обеспечивает
функциональность для создания, загрузки и обновления данных в базе данных SQLite.

Пример использования
--------------------

Пример использования класса `DataBase`:

.. code-block:: python

    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    db = DataBase(
        db_name='UsersData.db',
        table_name='users_data_table',
        titles={
            'id': 'TEXT PRIMARY KEY',
            'text': 'INTEGER[]',
            'sessions_messages': 'TEXT[]',
            'some': 'BOOLEAN',
            'images': 'CHAR',
            'free': 'BOOLEAN',
            'basic': 'BOOLEAN',
            'pro': 'BOOLEAN',
            'incoming_tokens': 'INTEGER',
            'outgoing_tokens': 'INTEGER',
            'free_requests': 'INTEGER',
            'datetime_sub': 'DATETIME',
            'promocode': 'BOOLEAN',
            'ref': 'TEXT',
        },
    )
    db.create()
    user_id = 'user123'
    user_data = {
        'text': [0, 0, 0, 0, 0, 0, 0, 0],
        'sessions_messages': [],
        'some': False,
        'images': '',
        'free': False,
        'basic': True,
        'pro': False,
        'incoming_tokens': 1000,
        'outgoing_tokens': 2000,
        'free_requests': 5,
        'datetime_sub': datetime.now().replace(microsecond=0) + relativedelta(days=30),
        'promocode': False,
        'ref': '',
    }
    db.insert_or_update_data(user_id, user_data)
    loaded_data = db.load_data_from_db()
    print(loaded_data)
"""
import sqlite3
import json
from re import sub
from datetime import datetime
from dateutil.relativedelta import relativedelta
from ast import literal_eval
from src.logger.logger import logger # Импорт logger
from src.utils.jjson import j_loads # Импорт j_loads

# Database functions class
class DataBase:
    """
    Класс для управления базой данных SQLite.

    :param db_name: Имя файла базы данных.
    :type db_name: str
    :param table_name: Имя таблицы в базе данных.
    :type table_name: str
    :param titles: Словарь, определяющий названия и типы столбцов в таблице.
    :type titles: dict[str, str]

    :ivar db_name: Имя файла базы данных.
    :vartype db_name: str
    :ivar table_name: Имя таблицы в базе данных.
    :vartype table_name: str
    :ivar titles: Словарь, определяющий названия и типы столбцов в таблице.
    :vartype titles: dict[str, str]
    :ivar types: Словарь с функциями преобразования типов данных.
    :vartype types: dict[str, callable]
    """
    def __init__(self, db_name: str, table_name: str, titles: dict[str, str]) -> None:
        """
        Инициализирует объект DataBase.

        :param db_name: Имя файла базы данных.
        :type db_name: str
        :param table_name: Имя таблицы в базе данных.
        :type table_name: str
        :param titles: Словарь, определяющий названия и типы столбцов в таблице.
        :type titles: dict[str, str]
        """
        self.db_name = db_name
        self.table_name = table_name
        self.titles = titles
        self.types = {
            'INTEGER': lambda x: int(x),
            'BOOLEAN': lambda x: bool(x),
            'INTEGER[]': lambda x: [int(el) for el in literal_eval(sub(r'{(.*?)}', r'[\1]', x))],
            'BOOLEAN[]': lambda x: [bool(el) for el in literal_eval(sub(r'{(.*?)}', r'[\1]', x))],
            'TEXT[]': lambda x: [j_loads(el) for el in literal_eval(sub(r'^{(.*?)}$', r'[\1]', x))],
            'DATETIME': lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
            'CHAR': lambda x: str(x),
            'TEXT': lambda x: str(x),
        }

    def create(self) -> None:
        """
        Создает таблицу в базе данных, если она не существует.
        """
        conn = None # Инициализация conn
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name} ({",\\n".join(f"{key} {value}" for key, value in self.titles.items())})')
            conn.commit()
            logger.info(f'Таблица {self.table_name} создана или уже существует.')
        except sqlite3.Error as e:
             logger.error(f'Ошибка при создании таблицы: {e}')
        finally:
            if conn:
                conn.close()

    def insert_or_update_data(self, record_id: str, values: dict[str, list[bool | int] | bool | int | str]) -> None:
        """
        Вставляет или обновляет данные в таблице.

        :param record_id: Идентификатор записи.
        :type record_id: str
        :param values: Словарь со значениями для вставки или обновления.
        :type values: dict[str, list[bool | int] | bool | int | str]
        """
        conn = None # Инициализация conn
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            placeholders = ', '.join(['?'] * (len(self.titles)))

            sql = f'REPLACE INTO {self.table_name} ({", ".join(list(self.titles.keys()))}) VALUES ({placeholders})'
            
            # Код преобразовывает списки в строку JSON для сохранения в БД
            processed_values = []
            for val in values.values():
                if isinstance(val, list):
                    processed_values.append(sub(r'^\\[(.*?)\\]$', r'{\1}', str([json.dumps(el) if isinstance(el, dict) else int(el) for el in val])))
                else:
                    processed_values.append(val)
                    
            cursor.execute(sql, [record_id] + processed_values)

            conn.commit()
            logger.info(f'Данные для id {record_id} успешно вставлены или обновлены.')
        except sqlite3.Error as e:
            logger.error(f'Ошибка при вставке или обновлении данных: {e}')
        finally:
            if conn:
                conn.close()


    def load_data_from_db(self) -> dict[str, dict[str, list[bool | int] | bool | int | str]]:
        """
        Загружает данные из базы данных в словарь.

        :return: Словарь с загруженными данными, где ключом является id записи.
        :rtype: dict[str, dict[str, list[bool | int] | bool | int | str]]
        """
        loaded_data = {}
        conn = None # Инициализация conn
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(f'SELECT {", ".join(list(self.titles.keys()))} FROM {self.table_name}')
            rows = cursor.fetchall()
            for row in rows:
                record_id = row[0]
                loaded_data[record_id] = {}
                for i, (key, value) in enumerate(list(self.titles.items())[1:], 1):
                    loaded_data[record_id][key] = self.types[value](row[i])
            logger.info(f'Данные успешно загружены из {self.table_name}.')
            return loaded_data
        except sqlite3.Error as e:
            logger.error(f'Ошибка при загрузке данных: {e}')
            return {}
        finally:
            if conn:
                conn.close()

# Database visualization
if __name__ == '__main__':
    
    N_ELEMENTS = 8 # Количество элементов по умолчанию
    
    db_manager = DataBase(db_name='UsersData.db', table_name='users_data_table', titles={'id': 'TEXT PRIMARY KEY', 'text': 'INTEGER[]',
                            'sessions_messages': 'TEXT[]', 'some': 'BOOLEAN',
                            'images': 'CHAR', 'free': 'BOOLEAN', 'basic': 'BOOLEAN',
                            'pro': 'BOOLEAN', 'incoming_tokens': 'INTEGER', 'outgoing_tokens': 'INTEGER',
                            'free_requests': 'INTEGER', 'datetime_sub': 'DATETIME', 'promocode': 'BOOLEAN', 'ref': 'TEXT'})
    db_manager.create()
    loaded_db = db_manager.load_data_from_db()
    
    user_id = input('Введите id пользователя: ')
    if user_id:
        user_data = None
        if 'pro' in user_id:
            user_data = {'text': [0] * N_ELEMENTS, 'sessions_messages': [], 'some': False, 'images': '', 'free': False, 'basic': True, 'pro': True, 'incoming_tokens': 1.7 * 10**5, 'outgoing_tokens': 5 * 10**5, 'free_requests': 10, 'datetime_sub': datetime.now().replace(microsecond=0) + relativedelta(months=1), 'promocode': False, 'ref': ''}
        elif 'admin' in user_id:
           user_data =  {'text': [0] * N_ELEMENTS, 'sessions_messages': [], 'some': False, 'images': '', 'free': False, 'basic': True, 'pro': True, 'incoming_tokens': 100 * 10**5, 'outgoing_tokens': 100 * 10**5, 'free_requests': 1000, 'datetime_sub': datetime.now().replace(microsecond=0) + relativedelta(years=5), 'promocode': False, 'ref': ''}
        else:
           user_data =  {'text': [0] * N_ELEMENTS, 'sessions_messages': [], 'some': False, 'images': '', 'free': False, 'basic': False, 'pro': False, 'incoming_tokens': 0, 'outgoing_tokens': 0, 'free_requests': 10, 'datetime_sub': datetime.now().replace(microsecond=0) + relativedelta(days=1), 'promocode': False, 'ref': ''}
        
        if user_data:
           loaded_db[user_id.split()[0]] = user_data
           db_manager.insert_or_update_data(user_id.split()[0], loaded_db[user_id.split()[0]])