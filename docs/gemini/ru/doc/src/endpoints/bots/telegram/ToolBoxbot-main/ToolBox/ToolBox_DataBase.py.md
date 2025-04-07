# Модуль для работы с базой данных Telegram бота ToolBox
=======================================================

Модуль содержит класс :class:`DataBase`, который используется для создания, управления и загрузки данных из базы данных SQLite для Telegram-бота ToolBox.

## Обзор

Этот модуль предоставляет класс `DataBase` для взаимодействия с базой данных SQLite. Он включает в себя методы для создания таблицы, вставки и обновления данных, а также загрузки данных в виде словаря. Модуль также содержит определения типов данных, используемых в базе данных.

## Подробней

Модуль предназначен для упрощения работы с базой данных SQLite в контексте Telegram-бота ToolBox. Он предоставляет удобный интерфейс для выполнения основных операций, таких как создание таблицы, добавление и обновление данных, а также загрузка данных в формате, пригодном для использования в боте.

## Классы

### `DataBase`

**Описание**: Класс для управления базой данных SQLite.

**Принцип работы**:
Класс `DataBase` предоставляет интерфейс для взаимодействия с базой данных SQLite. При инициализации класса создается подключение к базе данных, определяется таблица для работы и задаются типы данных для столбцов таблицы. Класс предоставляет методы для создания таблицы, вставки и обновления данных, а также загрузки данных из базы данных в виде словаря.

**Атрибуты**:
- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы в базе данных.
- `titles` (dict[str, str]): Словарь, определяющий имена столбцов и типы данных для таблицы.
- `types` (dict[str, function]): Словарь, определяющий функции для преобразования типов данных при загрузке данных из базы данных.

**Методы**:
- `__init__`: Инициализирует объект класса `DataBase`.
- `create`: Создает таблицу в базе данных, если она не существует.
- `insert_or_update_data`: Вставляет или обновляет данные в таблице.
- `load_data_from_db`: Загружает данные из таблицы в виде словаря.

### `__init__`

```python
    def __init__(self, db_name: str, table_name: str, titles: dict[str, str]) -> None:
        """
        Args:
            db_name (str): Имя файла базы данных.
            table_name (str): Имя таблицы в базе данных.
            titles (dict[str, str]): Словарь, определяющий структуру таблицы (имя столбца: тип данных).

        Returns:
            None

        Raises:
            None

        """
```

**Назначение**: Инициализирует объект класса `DataBase`.

**Параметры**:
- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы в базе данных.
- `titles` (dict[str, str]): Словарь, определяющий имена столбцов и типы данных для таблицы.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Сохраняет имя базы данных в атрибуте `self.db_name`.
2.  Сохраняет имя таблицы в атрибуте `self.table_name`.
3.  Сохраняет структуру таблицы (словарь `titles`) в атрибуте `self.titles`.
4.  Определяет словарь `self.types`, который содержит функции для преобразования типов данных при загрузке данных из базы данных.

```
  __init__
  │
  ├── db_name = db_name
  │
  ├── table_name = table_name
  │
  ├── titles = titles
  │
  └── types = {...}
```

**Примеры**:

```python
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
        """
```

**Назначение**: Создает таблицу в базе данных, если она еще не существует.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Как работает функция**:

1.  Устанавливает соединение с базой данных SQLite.
2.  Создает объект `cursor` для выполнения SQL-запросов.
3.  Выполняет SQL-запрос `CREATE TABLE IF NOT EXISTS`, чтобы создать таблицу, если она не существует. Структура таблицы определяется на основе словаря `self.titles`, который содержит имена столбцов и типы данных.
4.  Закрывает соединение с базой данных.

```
  create
  │
  ├── conn = sqlite3.connect(self.db_name)
  │   
  ├── cursor = conn.cursor()
  │
  ├── cursor.execute(CREATE TABLE IF NOT EXISTS)
  │
  └── conn.close()
```

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
            record_id (str): Идентификатор записи, который будет использоваться в качестве первичного ключа.
            values (dict[str, list[bool|int]|bool|int|str]): Словарь, содержащий данные для вставки или обновления.

        Returns:
            None

        Raises:
            sqlite3.Error: Если возникает ошибка при выполнении SQL-запроса.
        """
```

**Назначение**: Вставляет новую запись в таблицу или обновляет существующую запись с указанным `record_id`.

**Параметры**:
- `record_id` (str): Идентификатор записи, который будет использоваться в качестве первичного ключа.
- `values` (dict[str, list[bool|int]|bool|int|str]): Словарь, содержащий данные для вставки или обновления.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Устанавливает соединение с базой данных SQLite.
2.  Создает объект `cursor` для выполнения SQL-запросов.
3.  Формирует строку с плейсхолдерами для SQL-запроса.
4.  Формирует SQL-запрос `REPLACE INTO`, который вставляет новую запись, если `record_id` не существует, или обновляет существующую запись, если `record_id` уже существует.
5.  Выполняет SQL-запрос с использованием переданных данных.
6.  Сохраняет изменения и закрывает соединение с базой данных.

```
  insert_or_update_data
  │
  ├── conn = sqlite3.connect(self.db_name)
  │
  ├── cursor = conn.cursor()
  │
  ├── placeholders = ...
  │
  ├── sql = f"REPLACE INTO ..."
  │
  ├── cursor.execute(sql, ...)
  │
  ├── conn.commit()
  │
  └── conn.close()
```

**Примеры**:

```python
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
db = base.load_data_from_db(); N = 8
uid = input()
if uid != '':
    db[uid] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": False, "pro": False, "incoming_tokens": 0, "outgoing_tokens": 0, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(days=1), "promocode": False, "ref": ""}
    base.insert_or_update_data(uid, db[uid])
```

### `load_data_from_db`

```python
    def load_data_from_db(self) -> dict[str, dict[str, list[bool|int]|bool|int|str]]:
        """
        Args:
            None

        Returns:
            dict[str, dict[str, list[bool|int]|bool|int|str]]: Словарь, содержащий данные из базы данных, где ключом является идентификатор записи.

        Raises:
            sqlite3.Error: Если возникает ошибка при выполнении SQL-запроса.
        """
```

**Назначение**: Загружает данные из таблицы в виде словаря.

**Параметры**:
- `None`

**Возвращает**:
- `dict[str, dict[str, list[bool|int]|bool|int|str]]`: Словарь, содержащий данные из базы данных, где ключом является идентификатор записи.

**Как работает функция**:

1.  Устанавливает соединение с базой данных SQLite.
2.  Создает объект `cursor` для выполнения SQL-запросов.
3.  Выполняет SQL-запрос `SELECT`, чтобы выбрать все столбцы из таблицы.
4.  Получает все строки из результата запроса.
5.  Для каждой строки создает запись в словаре `loaded_data`, где ключом является идентификатор записи (значение первого столбца).
6.  Для каждого столбца в строке, начиная со второго столбца, преобразует значение столбца с использованием функции преобразования, определенной в словаре `self.types`.
7.  Сохраняет преобразованное значение в словаре для текущей записи.
8.  Закрывает соединение с базой данных.
9.  Возвращает словарь `loaded_data`.

```
  load_data_from_db
  │
  ├── loaded_data = dict()
  │
  ├── conn = sqlite3.connect(self.db_name)
  │
  ├── cursor = conn.cursor()
  │
  ├── cursor.execute(f"SELECT ... FROM {self.table_name}")
  │
  ├── rows = cursor.fetchall()
  │
  ├── for row in rows:
  │   │
  │   ├── id = row[0]
  │   │
  │   ├── loaded_data[id] = dict()
  │   │
  │   └── for i, (key, value) in enumerate(list(self.titles.items())[1:], 1):
  │       │
  │       └── loaded_data[id][key] = self.types[value](row[i])
  │
  ├── conn.close()
  │
  └── return loaded_data
```

**Примеры**:

```python
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
db = base.load_data_from_db()
print(db)
```

## Функции

### `DataBase visualization`

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

**Назначение**: Демонстрация работы с базой данных.

**Как работает функция**:
1. Создается экземпляр класса `DataBase` с указанием имени базы данных, имени таблицы и структуры таблицы.
2. Вызывается метод `create` для создания таблицы, если она еще не существует.
3. Вызывается метод `load_data_from_db` для загрузки данных из таблицы в словарь `db`.
4. Запрашивается ввод данных от пользователя (`uid`).
5. В зависимости от введенных данных, создается новая запись в словаре `db` с различными значениями для столбцов.
6. Вызывается метод `insert_or_update_data` для вставки или обновления записи в таблице.

```
  DataBase visualization
  │
  ├── base = DataBase(...)
  │
  ├── base.create()
  │
  ├── db = base.load_data_from_db()
  │
  ├── uid = input()
  │
  ├── if uid != '':
  │   │
  │   ├── if "pro" in uid:
  │   │   │
  │   └── elif 'admin' in uid:
  │   │   │
  │   └── else:
  │   │   │
  │   └── base.insert_or_update_data(uid.split()[0], db[uid.split()[0]])
```

**Примеры**:
Для запуска этого примера необходимо запустить скрипт `ToolBox_DataBase.py`
1.  Ввод `test_user` создаст нового пользователя с базовыми параметрами.
2.  Ввод `pro test_user` создаст пользователя с pro-тарифом.
3.  Ввод `admin test_user` создаст пользователя с правами администратора.
```python
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