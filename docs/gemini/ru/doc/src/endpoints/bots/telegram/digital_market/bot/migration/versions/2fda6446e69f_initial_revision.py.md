# Модуль миграции базы данных: initial_revision

## Обзор

Модуль `initial_revision.py` представляет собой файл миграции базы данных, созданный с использованием Alembic. Он определяет структуру базы данных для бота Telegram, предназначенного для цифрового рынка. Файл содержит функции `upgrade` и `downgrade`, которые позволяют соответственно применить и отменить изменения схемы базы данных.

## Подробнее

Этот файл миграции создает таблицы `categories`, `users`, `products` и `purchases`, определяя их структуру и связи между ними. Он является частью системы управления миграциями Alembic, которая позволяет автоматически обновлять схему базы данных при изменении модели данных приложения.

## Классы

В данном файле классы отсутствуют.

## Функции

### `upgrade`

```python
def upgrade() -> None:
    ...
```

**Назначение**: Функция `upgrade` выполняет обновление схемы базы данных, создавая необходимые таблицы и устанавливая ограничения.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Отсутствуют явные исключения, но Alembic может вызывать исключения при ошибках в процессе миграции.

**Как работает функция**:
1. Функция использует объект `op` из библиотеки `alembic` для выполнения операций с базой данных.
2. Создается таблица `categories` со столбцами `category_name` (Text, not nullable), `id` (Integer, primary key, autoincrement), `created_at` (TIMESTAMP, default CURRENT_TIMESTAMP) и `updated_at` (TIMESTAMP, default CURRENT_TIMESTAMP).
3. Создается таблица `users` со столбцами `telegram_id` (BigInteger, not nullable, unique), `username` (String), `first_name` (String), `last_name` (String), `id` (Integer, primary key, autoincrement), `created_at` (TIMESTAMP, default CURRENT_TIMESTAMP) и `updated_at` (TIMESTAMP, default CURRENT_TIMESTAMP).
4. Создается таблица `products` со столбцами `name` (Text, not nullable), `description` (Text, not nullable), `price` (Integer, not nullable), `file_id` (Text), `category_id` (Integer, not nullable), `id` (Integer, primary key, autoincrement), `created_at` (TIMESTAMP, default CURRENT_TIMESTAMP) и `updated_at` (TIMESTAMP, default CURRENT_TIMESTAMP). Устанавливается внешний ключ `category_id`, ссылающийся на таблицу `categories`.
5. Создается таблица `purchases` со столбцами `user_id` (Integer, not nullable), `product_id` (Integer, not nullable), `price` (Integer, not nullable), `id` (Integer, primary key, autoincrement), `created_at` (TIMESTAMP, default CURRENT_TIMESTAMP) и `updated_at` (TIMESTAMP, default CURRENT_TIMESTAMP). Устанавливаются внешние ключи `product_id`, ссылающийся на таблицу `products`, и `user_id`, ссылающийся на таблицу `users`.

**ASII flowchart**:

```
Начало
    ↓
Создание таблицы categories
    ↓
Создание таблицы users
    ↓
Создание таблицы products
    ↓
Создание таблицы purchases
    ↓
Конец
```

**Примеры**:
```python
# Непосредственный вызов функции upgrade не требуется, Alembic управляет этим процессом.
# upgrade()
```

### `downgrade`

```python
def downgrade() -> None:
    ...
```

**Назначение**: Функция `downgrade` выполняет откат схемы базы данных, удаляя таблицы, созданные функцией `upgrade`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Отсутствуют явные исключения, но Alembic может вызывать исключения при ошибках в процессе миграции.

**Как работает функция**:
1. Функция использует объект `op` из библиотеки `alembic` для выполнения операций с базой данных.
2. Удаляется таблица `purchases`.
3. Удаляется таблица `products`.
4. Удаляется таблица `users`.
5. Удаляется таблица `categories`.

**ASII flowchart**:

```
Начало
    ↓
Удаление таблицы purchases
    ↓
Удаление таблицы products
    ↓
Удаление таблицы users
    ↓
Удаление таблицы categories
    ↓
Конец
```

**Примеры**:
```python
# Непосредственный вызов функции downgrade не требуется, Alembic управляет этим процессом.
# downgrade()