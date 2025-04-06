# Модуль для работы с базой данных Telegram-бота ToolBox
======================================================

Модуль содержит класс :class:`DataBase`, который используется для создания, управления и визуализации базы данных пользователей Telegram-бота.

Пример использования
----------------------

```python
>>> base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
>>> base.create()
>>> db = base.load_data_from_db()
```

## Обзор

Модуль предоставляет функциональность для создания, вставки/обновления данных и загрузки данных из базы данных SQLite. Он также содержит пример визуализации базы данных.

## Подробнее

Этот модуль предназначен для работы с базой данных SQLite, используемой Telegram-ботом ToolBox. Он обеспечивает абстракцию для выполнения операций CRUD (Create, Read, Update, Delete) с данными пользователей. Класс `DataBase` инкапсулирует логику подключения к базе данных, создания таблиц, вставки и обновления данных, а также загрузки данных в структуру Python (словарь).  Пример использования демонстрирует создание экземпляра класса `DataBase`, создание таблицы, загрузку данных и добавление или обновление записи в базе данных.

## Классы

### `DataBase`

**Описание**: Класс для управления базой данных SQLite.

**Принцип работы**:
Класс `DataBase` предоставляет интерфейс для работы с базой данных SQLite. При инициализации класса устанавливаются имя базы данных, имя таблицы и заголовки столбцов таблицы. Класс содержит методы для создания таблицы, вставки и обновления данных, а также загрузки данных из таблицы в словарь Python.

**Аттрибуты**:
- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы в базе данных.
- `titles` (dict[str, str]): Словарь, определяющий имена столбцов и их типы данных.
- `types` (dict[str, Callable]): Словарь, содержащий функции преобразования типов данных из базы данных.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `DataBase`.
- `create`: Создает таблицу в базе данных, если она не существует.
- `insert_or_update_data`: Вставляет или обновляет данные в таблице.
- `load_data_from_db`: Загружает данные из таблицы в словарь.

## Функции

### `__init__`

```python
def __init__(self, db_name: str, table_name: str, titles: dict[str, str]) -> None:
    """Инициализирует экземпляр класса DataBase.

    Args:
        db_name (str): Имя файла базы данных.
        table_name (str): Имя таблицы в базе данных.
        titles (dict[str, str]): Словарь, определяющий имена столбцов и их типы данных.

    Returns:
        None
    """
    ...
```

**Назначение**: Инициализирует объект класса `DataBase` с указанными параметрами.

**Параметры**:
- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы в базе данных.
- `titles` (dict[str, str]): Словарь, определяющий структуру таблицы (имена столбцов и их типы данных).

**Возвращает**:
- `None`

**Как работает функция**:

1.  Присваивает входные параметры (`db_name`, `table_name`, `titles`) соответствующим атрибутам объекта `DataBase`.
2.  Определяет словарь `types`, который содержит лямбда-функции для преобразования типов данных, полученных из базы данных, в соответствующие типы Python. Этот словарь используется при загрузке данных из базы данных для правильной интерпретации и преобразования значений.

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
    """Создает таблицу в базе данных, если она не существует.

    Args:
        None

    Returns:
        None
    """
    ...
```

**Назначение**: Создает таблицу в базе данных, если она еще не существует.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Как работает функция**:

1.  Устанавливает соединение с базой данных SQLite, используя имя базы данных, хранящееся в атрибуте `self.db_name`.
2.  Создает объект курсора для выполнения SQL-запросов.
3.  Выполняет SQL-запрос `CREATE TABLE IF NOT EXISTS`, который создает таблицу с именем `self.table_name`, если она еще не существует. Структура таблицы определяется на основе словаря `self.titles`, который содержит имена столбцов и их типы данных.
4.  Закрывает соединение с базой данных.

```ascii
      Начало
        ↓
Соединение с БД
        ↓
   Создание курсора
        ↓
 Создание таблицы
        ↓
   Закрытие соединения
        ↓
      Конец
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
    """Вставляет или обновляет данные в таблице.

    Args:
        record_id (str): Значение первичного ключа записи.
        values (dict[str, list[bool|int]|bool|int|str]): Словарь, содержащий имена столбцов и их значения для вставки или обновления.

    Returns:
        None
    """
    ...
```

**Назначение**: Вставляет новую запись в таблицу или обновляет существующую запись, если запись с указанным `record_id` уже существует.

**Параметры**:
- `record_id` (str): Значение первичного ключа записи.
- `values` (dict[str, list[bool|int]|bool|int|str]): Словарь, содержащий данные для вставки или обновления. Ключи словаря соответствуют именам столбцов в таблице, а значения - значениям, которые необходимо вставить или обновить.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Устанавливает соединение с базой данных SQLite.
2.  Создает объект курсора для выполнения SQL-запросов.
3.  Формирует SQL-запрос `REPLACE INTO`, который позволяет вставить новую запись или обновить существующую запись с заданным `record_id`.
4.  Подготавливает значения для вставки или обновления, преобразуя списки в строки JSON и экранируя специальные символы.
5.  Выполняет SQL-запрос с подготовленными значениями.
6.  Сохраняет изменения в базе данных и закрывает соединение.

```ascii
      Начало
        ↓
Соединение с БД
        ↓
   Создание курсора
        ↓
Формирование SQL-запроса
        ↓
  Подготовка значений
        ↓
   Выполнение запроса
        ↓
Сохранение изменений
        ↓
   Закрытие соединения
        ↓
      Конец
```

**Примеры**:

```python
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
base.create()
db = base.load_data_from_db()
N = 8
uid = "some_user_id"
db[uid] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": False, "pro": False, "incoming_tokens": 0, "outgoing_tokens": 0, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(days=1), "promocode": False, "ref": ""}
base.insert_or_update_data(uid, db[uid])
```

### `load_data_from_db`

```python
def load_data_from_db(self) -> dict[str, dict[str, list[bool|int]|bool|int|str]]:
    """Загружает данные из таблицы в словарь.

    Args:
        None

    Returns:
        dict[str, dict[str, list[bool|int]|bool|int|str]]: Словарь, содержащий данные из таблицы.
            Ключи внешнего словаря соответствуют значениям первичного ключа (столбец 'id').
            Значениями внешнего словаря являются словари, представляющие строки таблицы.
            Ключи внутренних словарей соответствуют именам столбцов, а значения - значениям в этих столбцах.
    """
    ...
```

**Назначение**: Загружает данные из таблицы базы данных в словарь Python.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `dict[str, dict[str, list[bool|int]|bool|int|str]]`: Словарь, содержащий данные из таблицы.

**Как работает функция**:

1.  Инициализирует пустой словарь `loaded_data`, который будет содержать загруженные данные.
2.  Устанавливает соединение с базой данных SQLite.
3.  Создает объект курсора для выполнения SQL-запросов.
4.  Выполняет SQL-запрос `SELECT`, который выбирает все столбцы из таблицы `self.table_name`.
5.  Извлекает все строки из результата запроса с помощью метода `fetchall()`.
6.  Итерируется по каждой строке в результате запроса.
7.  Для каждой строки извлекает значение первичного ключа (столбец 'id') и создает запись во внешнем словаре `loaded_data` с этим значением в качестве ключа.
8.  Для каждого столбца в строке (начиная со второго столбца, так как первый столбец - это первичный ключ) извлекает имя столбца из словаря `self.titles` и значение из строки.
9.  Преобразует значение столбца в соответствующий тип данных, используя функции преобразования, определенные в словаре `self.types`.
10. Добавляет имя столбца и преобразованное значение во внутренний словарь, который представляет строку таблицы.
11. После обработки всех строк и столбцов закрывает соединение с базой данных.
12. Возвращает словарь `loaded_data`, содержащий загруженные данные.

```ascii
      Начало
        ↓
Инициализация словаря
        ↓
Соединение с БД
        ↓
   Создание курсора
        ↓
    Выполнение SQL-запроса
        ↓
  Извлечение всех строк
        ↓
    Итерация по строкам
        ↓
  Извлечение значений
        ↓
Преобразование типов
        ↓
Заполнение словаря
        ↓
   Закрытие соединения
        ↓
Возврат словаря
        ↓
      Конец
```

**Примеры**:

```python
base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
base.create()
db = base.load_data_from_db()
```