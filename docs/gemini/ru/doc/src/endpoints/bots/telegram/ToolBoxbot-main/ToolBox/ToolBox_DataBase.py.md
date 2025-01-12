# Модуль `ToolBox_DataBase`

## Обзор

Модуль `ToolBox_DataBase` предоставляет класс `DataBase` для работы с SQLite базами данных. Он включает в себя функции для создания таблиц, вставки, обновления и загрузки данных, а также обеспечивает преобразование типов данных.

## Содержание

1.  [Класс `DataBase`](#класс-database)
    -   [Инициализация `__init__`](#инициализация-__init__)
    -   [Создание базы данных `create`](#создание-базы-данных-create)
    -   [Вставка или обновление данных `insert_or_update_data`](#вставка-или-обновление-данных-insert_or_update_data)
    -   [Загрузка данных из базы `load_data_from_db`](#загрузка-данных-из-базы-load_data_from_db)

## Классы

### `DataBase`

**Описание**: Класс для управления базой данных SQLite.

**Методы**:
- [`__init__`](#инициализация-__init__): Инициализирует объект `DataBase`.
- [`create`](#создание-базы-данных-create): Создаёт таблицу в базе данных.
- [`insert_or_update_data`](#вставка-или-обновление-данных-insert_or_update_data): Вставляет или обновляет данные в таблицу.
- [`load_data_from_db`](#загрузка-данных-из-базы-load_data_from_db): Загружает данные из таблицы в словарь.

#### Инициализация `__init__`
```python
def __init__(self, db_name: str, table_name: str, titles: dict[str, str]) -> None:
```

**Описание**: Инициализирует объект `DataBase` с именем базы данных, именем таблицы и заголовками столбцов.

**Параметры**:
- `db_name` (str): Имя файла базы данных.
- `table_name` (str): Имя таблицы в базе данных.
- `titles` (dict[str, str]): Словарь, где ключи - названия столбцов, а значения - их типы.

**Возвращает**:
- `None`

#### Создание базы данных `create`
```python
def create(self) -> None:
```

**Описание**: Создаёт таблицу в базе данных, если она не существует.

**Параметры**:
- `self` (DataBase): Экземпляр класса DataBase.

**Возвращает**:
- `None`

#### Вставка или обновление данных `insert_or_update_data`
```python
def insert_or_update_data(self, record_id: str, values: dict[str, list[bool|int]|bool|int|str]) -> None:
```

**Описание**: Вставляет или обновляет данные в таблице. Если запись с `record_id` уже существует, она будет обновлена.

**Параметры**:
- `record_id` (str): Идентификатор записи.
- `values` (dict[str, list[bool|int]|bool|int|str]): Словарь значений для вставки или обновления, где ключи - имена столбцов, а значения - данные.

**Возвращает**:
- `None`

#### Загрузка данных из базы `load_data_from_db`
```python
def load_data_from_db(self) -> dict[str, dict[str, list[bool|int]|bool|int|str]]:
```

**Описание**: Загружает данные из таблицы в словарь, где ключи - идентификаторы записей, а значения - словари с данными для каждой записи.

**Параметры**:
- `self` (DataBase): Экземпляр класса DataBase.

**Возвращает**:
- `dict[str, dict[str, list[bool|int]|bool|int|str]]`: Словарь с загруженными данными.

## Примеры использования

### Создание и использование базы данных
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

В этом примере демонстрируется создание объекта `DataBase`, создание таблицы, загрузка данных, а также вставка или обновление данных в таблице на основе пользовательского ввода.