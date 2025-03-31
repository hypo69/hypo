# Документация для модуля `ToolBox_DataBase.py`

## Обзор

Модуль `ToolBox_DataBase.py` предоставляет класс `DataBase` для работы с базой данных SQLite. Он включает функции для создания базы данных, вставки и обновления данных, а также загрузки данных из базы данных в словарь.

## Подробней

Этот модуль предназначен для управления данными, связанными с пользователями, в контексте Telegram-бота. Он позволяет хранить и извлекать информацию о пользователях, такую как их сообщения, изображения, статус подписки и использование токенов.

## Классы

### `DataBase`

**Описание**: Класс для управления базой данных SQLite.

**Методы**:

- `__init__`: Инициализирует объект `DataBase` с именем базы данных, именем таблицы и заголовками столбцов.
- `create`: Создает таблицу в базе данных, если она не существует.
- `insert_or_update_data`: Вставляет или обновляет данные в таблице.
- `load_data_from_db`: Загружает данные из таблицы в словарь.

**Параметры**:

- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы.
- `titles` (dict[str, str]): Словарь, определяющий столбцы таблицы и их типы данных.

**Примеры**

```python
base = DataBase(
    db_name="UsersData.db",
    table_name="users_data_table",
    titles={
        "id": "TEXT PRIMARY KEY",
        "text": "INTEGER[]",
        "sessions_messages": "TEXT[]",
        "some": "BOOLEAN",
        "images": "CHAR",
        "free": "BOOLEAN",
        "basic": "BOOLEAN",
        "pro": "BOOLEAN",
        "incoming_tokens": "INTEGER",
        "outgoing_tokens": "INTEGER",
        "free_requests": "INTEGER",
        "datetime_sub": "DATETIME",
        "promocode": "BOOLEAN",
        "ref": "TEXT",
    },
)
base.create()
db = base.load_data_from_db()
```

## Функции

### `__init__`

```python
def __init__(self, db_name: str, table_name: str, titles: dict[str, str]) -> None:
    """
    Args:
        db_name (str): Имя файла базы данных.
        table_name (str): Имя таблицы.
        titles (dict[str, str]): Словарь, определяющий столбцы таблицы и их типы данных.

    Returns:
        None:
    """
```

**Описание**: Инициализирует объект `DataBase` с именем базы данных, именем таблицы и заголовками столбцов.

**Параметры**:

- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы.
- `titles` (dict[str, str]): Словарь, определяющий столбцы таблицы и их типы данных.

**Примеры**:

```python
base = DataBase(
    db_name="UsersData.db",
    table_name="users_data_table",
    titles={
        "id": "TEXT PRIMARY KEY",
        "text": "INTEGER[]",
        "sessions_messages": "TEXT[]",
        "some": "BOOLEAN",
        "images": "CHAR",
        "free": "BOOLEAN",
        "basic": "BOOLEAN",
        "pro": "BOOLEAN",
        "incoming_tokens": "INTEGER",
        "outgoing_tokens": "INTEGER",
        "free_requests": "INTEGER",
        "datetime_sub": "DATETIME",
        "promocode": "BOOLEAN",
        "ref": "TEXT",
    },
)
```

### `create`

```python
def create(self) -> None:
    """
    Args:
        self (DataBase): Экземпляр класса `DataBase`.

    Returns:
        None:

    Raises:
         sqlite3.Error: Возникает, если есть ошибка при создании таблицы.
    """
```

**Описание**: Создает таблицу в базе данных, если она не существует.

**Параметры**:

- `self` (DataBase): Экземпляр класса `DataBase`.

**Примеры**:

```python
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
        self (DataBase): Экземпляр класса `DataBase`.
        record_id (str): Уникальный идентификатор записи.
        values (dict[str, list[bool|int]|bool|int|str]): Словарь со значениями для вставки или обновления.

    Returns:
        None:

    Raises:
        sqlite3.Error: Возникает, если есть ошибка при вставке или обновлении данных.
    """
```

**Описание**: Вставляет или обновляет данные в таблице.

**Параметры**:

- `self` (DataBase): Экземпляр класса `DataBase`.
- `record_id` (str): Уникальный идентификатор записи.
- `values` (dict[str, list[bool|int]|bool|int|str]): Словарь со значениями для вставки или обновления.

**Примеры**:

```python
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
db = base.load_data_from_db()
N = 8
uid = "test_user"
db[uid] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": False, "pro": False, "incoming_tokens": 0, "outgoing_tokens": 0, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(days=1), "promocode": False, "ref": ""}
base.insert_or_update_data(uid, db[uid])
```

### `load_data_from_db`

```python
def load_data_from_db(self) -> dict[str, dict[str, list[bool|int]|bool|int|str]]:
    """
    Args:
        self (DataBase): Экземпляр класса `DataBase`.

    Returns:
        dict[str, dict[str, list[bool|int]|bool|int|str]]: Словарь с загруженными данными из базы данных.

    Raises:
        sqlite3.Error: Возникает, если есть ошибка при загрузке данных.
    """
```

**Описание**: Загружает данные из таблицы в словарь.

**Параметры**:

- `self` (DataBase): Экземпляр класса `DataBase`.

**Возвращает**:

- `dict[str, dict[str, list[bool|int]|bool|int|str]]`: Словарь с загруженными данными из базы данных.

**Примеры**:

```python
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
db = base.load_data_from_db()
```