# Модуль ToolBox_DataBase

## Обзор

Модуль `ToolBox_DataBase.py` предоставляет класс `DataBase` для работы с базой данных `SQLite`. Он включает функции для создания таблицы, вставки и обновления данных, а также загрузки данных из базы данных в формате словаря. Этот модуль предназначен для управления данными пользователей, включая их сообщения, токены, подписки и другие параметры.

## Подробней

Модуль `ToolBox_DataBase.py` предназначен для упрощения взаимодействия с базой данных `SQLite`. Он предоставляет абстракцию над низкоуровневыми операциями `SQLite`, позволяя легко создавать, читать, обновлять и удалять данные. Класс `DataBase` позволяет определять структуру таблицы, типы данных и автоматически преобразовывать данные при чтении из базы данных. Модуль также содержит пример использования класса `DataBase` для создания и заполнения базы данных пользовательскими данными.

## Классы

### `DataBase`

**Описание**: Класс для работы с базой данных `SQLite`.

**Методы**:
- `__init__`: Инициализирует объект `DataBase` с именем базы данных, именем таблицы и заголовками столбцов.
- `create`: Создает таблицу в базе данных, если она не существует.
- `insert_or_update_data`: Вставляет или обновляет данные в таблице.
- `load_data_from_db`: Загружает данные из таблицы в словарь.

**Параметры**:
- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы в базе данных.
- `titles` (dict[str, str]): Словарь, определяющий имена и типы столбцов в таблице.

**Примеры**
```python
# Пример создания объекта DataBase
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                    "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                    "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                    "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                    "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
```

## Функции

### `__init__`

```python
def __init__(self, db_name: str, table_name: str, titles: dict[str, str]) -> None:
    """
    Args:
        db_name (str): Имя файла базы данных.
        table_name (str): Имя таблицы в базе данных.
        titles (dict[str, str]): Словарь, определяющий имена и типы столбцов в таблице.

    Returns:
        None

    Raises:
        None

    Example:
        >>> base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
        ...             "sessions_messages": "TEXT[]", "some": "BOOLEAN",
        ...             "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
        ...             "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
        ...             "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
        >>> print(base.db_name)
        UsersData.db
    """
```

**Описание**: Инициализирует объект `DataBase` с именем базы данных, именем таблицы и заголовками столбцов.

**Параметры**:
- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы в базе данных.
- `titles` (dict[str, str]): Словарь, определяющий имена и типы столбцов в таблице.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
# Пример создания объекта DataBase
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                    "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                    "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                    "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                    "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
```

### `create`

```python
def create(self) -> None:
    """
    Args:
        None

    Returns:
        None

    Raises:
        sqlite3.Error: Если возникает ошибка при создании таблицы.

    Example:
        >>> base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
        ...             "sessions_messages": "TEXT[]", "some": "BOOLEAN",
        ...             "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
        ...             "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
        ...             "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
        >>> base.create()
    """
```

**Описание**: Создает таблицу в базе данных, если она не существует.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- `sqlite3.Error`: Если возникает ошибка при создании таблицы.

**Примеры**:
```python
# Пример создания таблицы
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                    "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                    "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                    "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                    "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
base.create()
```

### `insert_or_update_data`

```python
def insert_or_update_data(self, record_id: str, values: dict[str, list[bool|int]|bool|int|str]) -> None:
    """
    Args:
        record_id (str): Идентификатор записи.
        values (dict[str, list[bool|int]|bool|int|str]): Словарь со значениями для вставки или обновления.

    Returns:
        None

    Raises:
        sqlite3.Error: Если возникает ошибка при вставке или обновлении данных.

    Example:
        >>> base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
        ...             "sessions_messages": "TEXT[]", "some": "BOOLEAN",
        ...             "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
        ...             "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
        ...             "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
        >>> base.create()
        >>> base.insert_or_update_data('user1', {"text": [0, 0, 0, 0, 0, 0, 0, 0], "sessions_messages": [], "some": False, "images": "", "free": False, "basic": False, "pro": False, "incoming_tokens": 0, "outgoing_tokens": 0, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(days=1), "promocode": False, "ref": ""})
    """
```

**Описание**: Вставляет или обновляет данные в таблице.

**Параметры**:
- `record_id` (str): Идентификатор записи.
- `values` (dict[str, list[bool|int]|bool|int|str]): Словарь со значениями для вставки или обновления.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `sqlite3.Error`: Если возникает ошибка при вставке или обновлении данных.

**Примеры**:
```python
# Пример вставки или обновления данных
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                    "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                    "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                    "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                    "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
base.create()
base.insert_or_update_data('user1', {"text": [0, 0, 0, 0, 0, 0, 0, 0], "sessions_messages": [], "some": False, "images": "", "free": False, "basic": False, "pro": False, "incoming_tokens": 0, "outgoing_tokens": 0, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(days=1), "promocode": False, "ref": ""})
```

### `load_data_from_db`

```python
def load_data_from_db(self) -> dict[str, dict[str, list[bool|int]|bool|int|str]]:
    """
    Args:
        None

    Returns:
        dict[str, dict[str, list[bool|int]|bool|int|str]]: Словарь с данными из базы данных.

    Raises:
        sqlite3.Error: Если возникает ошибка при загрузке данных.

    Example:
        >>> base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
        ...             "sessions_messages": "TEXT[]", "some": "BOOLEAN",
        ...             "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
        ...             "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
        ...             "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
        >>> base.create()
        >>> data = base.load_data_from_db()
        >>> print(data)
        {}
    """
```

**Описание**: Загружает данные из таблицы в словарь.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `dict[str, dict[str, list[bool|int]|bool|int|str]]`: Словарь с данными из базы данных.

**Вызывает исключения**:
- `sqlite3.Error`: Если возникает ошибка при загрузке данных.

**Примеры**:
```python
# Пример загрузки данных из базы данных
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                    "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                    "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                    "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                    "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
base.create()
data = base.load_data_from_db()