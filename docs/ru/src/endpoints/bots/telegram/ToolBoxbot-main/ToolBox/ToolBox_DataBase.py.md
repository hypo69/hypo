# Модуль `ToolBox_DataBase.py`

## Обзор

Модуль `ToolBox_DataBase.py` предоставляет класс `DataBase` для управления базой данных SQLite. Он обеспечивает создание таблицы, вставку, обновление и загрузку данных. Модуль предназначен для использования в боте `ToolBox` для хранения и извлечения пользовательских данных.

## Подробней

Модуль содержит класс `DataBase`, который инициализируется с именем базы данных, именем таблицы и словарем, определяющим структуру таблицы (имена и типы столбцов). Класс предоставляет методы для создания таблицы, вставки или обновления данных, а также для загрузки данных из базы данных в словарь. В основной части модуля (`if __name__ == "__main__":`) демонстрируется пример использования класса `DataBase` для создания базы данных, добавления и обновления записей пользователей.

## Классы

### `DataBase`

**Описание**: Класс для управления базой данных SQLite.

**Как работает класс**:
Класс `DataBase` предоставляет интерфейс для взаимодействия с базой данных SQLite. При инициализации класс принимает имя базы данных, имя таблицы и словарь `titles`, определяющий структуру таблицы. Метод `create` создает таблицу, если она еще не существует. Метод `insert_or_update_data` вставляет новую запись или обновляет существующую. Метод `load_data_from_db` загружает данные из таблицы в словарь. Типы данных преобразуются в соответствующие типы Python с использованием словаря `types`.

**Методы**:
- `__init__`: Инициализирует объект `DataBase` с именем базы данных, именем таблицы и структурой таблицы.
- `create`: Создает таблицу в базе данных, если она еще не существует.
- `insert_or_update_data`: Вставляет или обновляет данные в таблице.
- `load_data_from_db`: Загружает данные из таблицы в словарь.

#### `__init__`

```python
def __init__(self, db_name: str, table_name: str, titles: dict[str, str]) -> None:
    """
    Args:
        db_name (str): Имя базы данных.
        table_name (str): Имя таблицы.
        titles (dict[str, str]): Словарь, определяющий структуру таблицы (имена и типы столбцов).

    Returns:
        None

    Raises:
        None
    """
```

**Описание**: Инициализирует объект `DataBase`.

**Как работает функция**:
Функция инициализирует объект `DataBase`, сохраняя имя базы данных, имя таблицы и структуру таблицы в атрибутах экземпляра. Также определяется словарь `types`, который содержит функции для преобразования строковых значений из базы данных в соответствующие типы Python.

**Параметры**:
- `db_name` (str): Имя базы данных.
- `table_name` (str): Имя таблицы.
- `titles` (dict[str, str]): Словарь, определяющий структуру таблицы (имена и типы столбцов).

#### `create`

```python
def create(self) -> None:
    """
    Args:
        None

    Returns:
        None

    Raises:
        sqlite3.Error: Если возникает ошибка при создании таблицы.
    """
```

**Описание**: Создает таблицу в базе данных, если она еще не существует.

**Как работает функция**:
Функция устанавливает соединение с базой данных SQLite и выполняет SQL-запрос для создания таблицы, если она еще не существует. Структура таблицы определяется словарем `self.titles`.

**Параметры**:
- Нет

#### `insert_or_update_data`

```python
def insert_or_update_data(self, record_id: str, values: dict[str, list[bool|int]|bool|int|str]) -> None:
    """
    Args:
        record_id (str): Идентификатор записи.
        values (dict[str, list[bool|int]|bool|int|str]): Словарь значений для вставки или обновления.

    Returns:
        None

    Raises:
        sqlite3.Error: Если возникает ошибка при вставке или обновлении данных.
    """
```

**Описание**: Вставляет или обновляет данные в таблице.

**Как работает функция**:
Функция устанавливает соединение с базой данных SQLite и выполняет SQL-запрос для вставки новой записи или обновления существующей записи с заданным идентификатором `record_id`.  Если запись с указанным `record_id` уже существует, она будет перезаписана.  Значения для вставки или обновления берутся из словаря `values`, переданного в качестве аргумента.  Если значением является список, то оно преобразуется в строку JSON.

**Параметры**:
- `record_id` (str): Идентификатор записи.
- `values` (dict[str, list[bool|int]|bool|int|str]): Словарь значений для вставки или обновления.

#### `load_data_from_db`

```python
def load_data_from_db(self) -> dict[str, dict[str, list[bool|int]|bool|int|str]]:
    """
    Args:
        None

    Returns:
        dict[str, dict[str, list[bool|int]|bool|int|str]]: Словарь, содержащий данные из базы данных.

    Raises:
        sqlite3.Error: Если возникает ошибка при загрузке данных.
    """
```

**Описание**: Загружает данные из таблицы в словарь.

**Как работает функция**:
Функция устанавливает соединение с базой данных SQLite и выполняет SQL-запрос для извлечения всех записей из таблицы. Затем данные преобразуются в словарь, где ключом является идентификатор записи, а значением - словарь, содержащий значения столбцов.  Значения столбцов преобразуются в соответствующие типы Python с использованием словаря `self.types`.

**Параметры**:
- Нет

**Возвращает**:
- `dict[str, dict[str, list[bool|int]|bool|int|str]]`: Словарь, содержащий данные из базы данных.

## Функции

### `main` (в блоке `if __name__ == "__main__":`)

```python
if __name__ == "__main__":
    base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
    base.create(); db = base.load_data_from_db(); N = 8
    uid = input()
    if uid != '':
        if "pro" in uid:
            db[uid.split()[0]] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": True, "pro": True, "incoming_tokens": 1.7*10**5, "outgoing_tokens": 5*10**5, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(months=1), "promocode": False, "ref": ""}
        elif 'admin' in uid:
            db[uid.split()[0]] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": True, "pro": True, "incoming_tokens": 100*10**5, "outgoing_tokens": 100*10**5, "free_requests": 1000, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(years=5), "promocode": False, "ref": ""}
        else:
            db[uid] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": False, "pro": False, "incoming_tokens": 0, "outgoing_tokens": 0, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(days=1), "promocode": False, "ref": ""}
        base.insert_or_update_data(uid.split()[0], db[uid.split()[0]])
```

**Описание**: Пример использования класса `DataBase`.

**Как работает функция**:
В блоке `if __name__ == "__main__":` создается экземпляр класса `DataBase` с именем базы данных "UsersData.db", именем таблицы "users_data_table" и структурой таблицы, определенной в словаре `titles`. Затем создается таблица, загружаются данные из базы данных, запрашивается ввод пользователя и, в зависимости от введенных данных, создается или обновляется запись пользователя.

**Параметры**:
- Нет

**Примеры**:

Примеры создания и работы с базой данных:

```python
    base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
    base.create()
    db = base.load_data_from_db()
    uid = input()
    if uid != '':
        if "pro" in uid:
            db[uid.split()[0]] = {"text": [0]*8, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": True, "pro": True, "incoming_tokens": 1.7*10**5, "outgoing_tokens": 5*10**5, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(months=1), "promocode": False, "ref": ""}
        elif 'admin' in uid:
            db[uid.split()[0]] = {"text": [0]*8, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": True, "pro": True, "incoming_tokens": 100*10**5, "outgoing_tokens": 100*10**5, "free_requests": 1000, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(years=5), "promocode": False, "ref": ""}
        else:
            db[uid] = {"text": [0]*8, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": False, "pro": False, "incoming_tokens": 0, "outgoing_tokens": 0, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(days=1), "promocode": False, "ref": ""}
        base.insert_or_update_data(uid.split()[0], db[uid.split()[0]])